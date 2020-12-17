import pymysql
import json
from DataFormat import *
import pandas as pd
import os

class DatabaseProcesser:

    def __init__(self,database_url,user,password,shema_name):
        self.db = pymysql.connect(database_url,user,password,shema_name)
########################################create table Product#######################################
    def create_product_table(self, db):
        cursor = db.cursor()

        cursor.execute("drop table if exists Product")

        sql = """ create table Product(
                    product_id varchar(30) primary key,
                    product_name varchar(255) unique,
                    category_id varchar (30)
                    )"""
        cursor.execute(sql)

#######################################create table Product_Price####################################
    def create_price_table(self,db):
        cursor = db.cursor()

        cursor.execute("drop table if exists Product_Price")

        sql = """ create table Product_Price(
                 product_id varchar(30),
                 product_price double,
                 price_date date,
                 primary key(product_id,price_date)
                 )"""
        cursor.execute(sql)

######################################crate Table Category############################################
    def create_category_table(self, db):
        cursor = db.cursor()

        cursor.execute("drop table if exists Category")

        sql = """ create table Category(
                    category_id varchar(30) primary key,
                    category_name varchar(255),
                    super_category_id varchar (30)
                    )"""
        cursor.execute(sql)

################################# insert price and date for one row###########################################################
    def insert_price(self,dict_price):
        product_id = dict_price['product_id']
        product_price = dict_price['product_price']
        price_date = dict_price['price_date']
        sql = """insert into product_price values(%s,%s,%s)""" % (product_id , product_price, "\'" + price_date + "\'")
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print('##############ProductProcesser.insert_price(self,dict_price)##############')
            print(e)
            print('##############ProductProcesser.insert_price(self,dict_price)##############')
            self.db.rollback()

################################# insert price and date for all rows###########################################################
    def insert_all_prices(self,dataframe_product_price):
        dict_price = dict()
        for i in range(len(dataframe_product_price)):
            dict_price.clear()
            dict_price['product_id'] = dataframe_product_price['product_id'][i]
            dict_price['product_price'] = dataframe_product_price['product_price'][i]
            dict_price['price_date'] = dataframe_product_price['price_date'][i]
            self.insert_price(dict_price)

###################################insert category#################################################################
    def insert_category(self,dataframe_category):
        for row_index in range(len(dataframe_category)):
            category_id = dataframe_category['category_id'][row_index]
            category_name = dataframe_category['category_name'][row_index]
            super_category_id = 0
            if pd.notna(dataframe_category['super_category_id'][row_index]):
                super_category_id = dataframe_category['super_category_id'][row_index]
            sql = """insert into category values (%s,%s,%s)""" % (category_id, '\"' + category_name + '\"', super_category_id)
            cursor = self.db.cursor()
            try:
                cursor.execute(sql)
                self.db.commit()
            except Exception as e:
                print('##############ProductProcesser.insert_category(self,dataframe_category)################################')
                print(e)
                print('##############ProductProcesser.insert_category(self,dataframe_category)################################')
                self.db.rollback()

#########################################insert product########################################################
    def insert_product(self,dataframe_product_category):
        for row_index in range(len(dataframe_product_category)):
            product_id = dataframe_product_category['product_id'][row_index]
            product_name = dataframe_product_category['product_name'][row_index]
            category_id = dataframe_product_category['category_id'][row_index]
            if '"' in product_name:
                sql = """insert into product values (%s,%s,%s)""" % (product_id, '\'' + product_name + '\'', category_id)
            else:
                sql = """insert into product values (%s,%s,%s)""" % (product_id, '\"' + product_name + '\"', category_id)
            cursor = self.db.cursor()
            try:
                print(sql)
                cursor.execute(sql)
                self.db.commit()
            except Exception as e:
                print('###############ProductProcesser.insert_product(self,dataframe_product_category)##############')
                print(e)
                print('#################ProductProcessor.insert_product(self,dataframe_product_category)#############')
                self.db.rollback()

#######################################max_category_id################################################
    def get_max_category_id(self):
        current_result = 0
        cursor = self.db.cursor()
        sql = """select max(convert(category_id,signed)) from category"""
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            for row in result:
                current_result = row
                break
        except Exception as e:
            pass
        if current_result == None:
            current_result = 0
        return current_result
#######################################category_id by category_name################################################
    def get_category_id(self,category_name):
        current_result = -1
        cursor = self.db.cursor()
        sql = "select category_id from category where category_name = '%s'"%category_name
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            for row in result:
                current_result = row
                break
        except Exception as e:
            pass

        return current_result

#######################################average price by product################################################
    def get_average_price_byProduct(self,productID):
        cursor = self.db.cursor()

        sql = """select avg(product_price),product_id from Product_Price where product_id = %s group by product_id"""% str(productID)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                avg_price_product = row[0]
                product_id = row[1]
                print("avg_price_product: %s,product_id: %s" % (avg_price_product, product_id))
        except:
            print("Error: unable to fetch data")

#####################################average price by date#####################################################
    def get_average_price_byDate(self,priceDate):
        cursor = self.db.cursor()

        sql = """select avg(product_price),price_date from Product_Price where price_date = %s group by price_date"""% priceDate
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                avg_price_date = row[0]
                price_date = row[1]
                print("avg_price_date: %s, price_date: %s"%(avg_price_date,price_date))
        except:
            print("Error: unable to fetch data")

#######################################average price by all date after data cleaning#############################################
    def get_average_price_all_date(self):
        cursor = self.db.cursor()

        sql = """select avg(product_price),price_date from Product_Price where product_id in (select product_id from Product_Price group by product_id 
                 having count(distinct(price_date))=(select count(distinct(price_date)) from Product_Price)) group by price_date"""
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            avg_price_all_date = []
            date_all_date = []
            for row in results:
                avg_price_all_date.append(row[0])
                date_all_date.append(row[1])
            print("avg_price_all_date",avg_price_all_date)
            print("date_all_date",date_all_date)
            return date_all_date,avg_price_all_date
        except:
            print("Error: unable to fetch data")

 ####################################### average price by Date accroding each category####################################
    def get_average_eachCategory(self, categoryId):
        cursor = self.db.cursor()

        sql = """select avg(product_price),price_date from product_price_clean where product_id in 
                 (select product_id from Product where category_id in 
                 (SELECT category_id FROM category WHERE FIND_IN_SET(category_id, getChild(%s))AND category_id != %s )) 
                 group by price_date""" % (categoryId,categoryId)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            avg_price_eachCategory = []
            date_Date = []
            for row in results:
                avg_price_eachCategory.append(row[0])
                date_Date.append(row[1])
                #print("avg_price_eachCategory", avg_price_eachCategory)
                #print("date_Date", date_Date)
            return date_Date, avg_price_eachCategory
        except:
            print("Error: unable to fetch data")

########################################all top categories########################################################
    def get_top_category(self):
        cursor = self.db.cursor()

        sql = """select category_id,category_name from Category where super_category_id = 0 """
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            top_category = dict()
            for row in results:
                top_category[row[0]]=row[1]
            print("top_category",top_category)
            return top_category
        except:
            print("Error: unable to fetch data")

################################each product price############################################
    def get_product_price(self,productID):
        cursor = self.db.cursor()
        sql = """ select price_date,product_price from Product_Price where product_id = %s""" % str(productID)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            product_date = []
            product_price = []
            for row in results:
                product_date.append(row[0])
                product_price.append(row[1])
            print("product_date",product_date)
            print("product_price",product_price)
            return product_date,product_price
        except:
            print("Error: unable to fetch data")
    def close(self):
        self.db.close()

########################################main()####################################################################
if __name__ == "__main__":
    databaseProcessor = DatabaseProcesser("localhost","root","6857","IdealoPreis")
    dataFormat = DataFormat('Daten/Json(ProductsInfo(201-300))ToExcel(6).xlsx')

    datarame_category = dataFormat.get_category()
    dataframe_product_category = dataFormat.get_product()
    dataframe_product_price = dataFormat.get_product_price()

######################insert price in mysql############################
    databaseProcessor.insert_all_prices(dataframe_product_price)

#################insert category in mysql##############################
   # databaseProcessor.insert_category(datarame_category)

#####################insert product in mysql##########################
   # databaseProcessor.insert_product(dataframe_product_category)

    ############get_average_price_byDate(self,priceDate)##############
    #databaseProcessor.get_average_price_byDate("\'" + '2020-01-20' + "\'")

    ############get_average_price_allDate(self)#######################
    #databaseProcessor.get_average_price_all_date()

    ############get_average_eachCategory(self, categoryId)##############
    #databaseProcessor.get_average_eachCategory(4)

    #############get_top_category(self)##########################
    #databaseProcessor.get_top_category()

    ########################get_product_price(self,productID)#############
    #databaseProcessor.get_product_price('6509891')

    ############database close##################################
    databaseProcessor.close()