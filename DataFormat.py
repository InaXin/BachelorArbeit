from DatabaseProcessor import *
import pandas as pd
import os
import json


class DataFormat:

    def __init__(self,excel_path:str):
        self.excel_file = pd.ExcelFile(excel_path)
        self.dataframe_product = self.excel_file.parse(self.excel_file.sheet_names[0])
        self.dict_category_number = self.format_category_id()

    ###################all category number########################################################################
    def format_category_id(self):
        databaseProcessor = DatabaseProcesser("localhost","root","6857","IdealoPreis")
        max_category_id = databaseProcessor.get_max_category_id()
        category_id = max_category_id + 1
        dict_category_number = dict()
        for category_name in self.dataframe_product['Kategorie 1']:
            if category_name is not None and category_name not in dict_category_number.keys():
                dict_category_number[category_name] = databaseProcessor.get_category_id(category_name)
                if dict_category_number[category_name] == -1:
                    dict_category_number[category_name] = category_id
                    category_id = category_id + 1
        for category_name in self.dataframe_product['Kategorie 2']:
            if category_name is not None and category_name not in dict_category_number.keys():
                dict_category_number[category_name] = databaseProcessor.get_category_id(category_name)
                if dict_category_number[category_name] == -1:
                    dict_category_number[category_name] = category_id
                    category_id = category_id + 1
        for category_name in self.dataframe_product['Kategorie 3']:
            if category_name is not None and category_name not in dict_category_number.keys():
                dict_category_number[category_name] = databaseProcessor.get_category_id(category_name)
                if dict_category_number[category_name] == -1:
                    dict_category_number[category_name] = category_id
                    category_id = category_id + 1
        for category_name in self.dataframe_product['Kategorie 4']:
            if category_name is not None and category_name not in dict_category_number.keys():
                dict_category_number[category_name] = databaseProcessor.get_category_id(category_name)
                if dict_category_number[category_name] == -1:
                    dict_category_number[category_name] = category_id
                    category_id = category_id + 1
        for category_name in self.dataframe_product['Kategorie 5']:
            if category_name is not None and category_name not in dict_category_number.keys():
                dict_category_number[category_name] = databaseProcessor.get_category_id(category_name)
                if dict_category_number[category_name] == -1:
                    dict_category_number[category_name] = category_id
                    category_id = category_id + 1
        for category_name in self.dataframe_product['Kategorie 6']:
            if category_name is not None and category_name not in dict_category_number.keys():
                dict_category_number[category_name] = databaseProcessor.get_category_id(category_name)
                if dict_category_number[category_name] == -1:
                    dict_category_number[category_name] = category_id
                    category_id = category_id + 1
        for category_name in self.dataframe_product['Kategorie 7']:
            if category_name is not None and category_name not in dict_category_number.keys():
                dict_category_number[category_name] = databaseProcessor.get_category_id(category_name)
                if dict_category_number[category_name] == -1:
                    dict_category_number[category_name] = category_id
                    category_id = category_id + 1
        databaseProcessor.close()
        return dict_category_number

    ##################category dataframe###########################################################################
    def get_category(self):
        dataframe_category = pd.DataFrame(columns=['category_id', 'category_name', 'super_category_id'])
        dict_current = dict()
        for curent_category_name in self.dict_category_number.keys():
            if curent_category_name in self.dataframe_product['Kategorie 1'].values:
                dict_current['category_id'] = self.dict_category_number[curent_category_name]
                dict_current['category_name'] = curent_category_name
                dataframe_category = dataframe_category.append(dict_current, ignore_index=True)
                dict_current.clear()
                continue
            if curent_category_name in self.dataframe_product['Kategorie 2'].values:
                dict_current['category_id'] = self.dict_category_number[curent_category_name]
                dict_current['category_name'] = curent_category_name
                dict_current['super_category_id'] = self.dict_category_number[self.dataframe_product[self.dataframe_product['Kategorie 2'] == curent_category_name]['Kategorie 1'].values[0]]
                dataframe_category = dataframe_category.append(dict_current, ignore_index=True)
                dict_current.clear()
                continue
            if curent_category_name in self.dataframe_product['Kategorie 3'].values:
                dict_current['category_id'] = self.dict_category_number[curent_category_name]
                dict_current['category_name'] = curent_category_name
                dict_current['super_category_id'] = self.dict_category_number[self.dataframe_product[self.dataframe_product['Kategorie 3'] == curent_category_name]['Kategorie 2'].values[0]]
                dataframe_category = dataframe_category.append(dict_current, ignore_index=True)
                dict_current.clear()
                continue
            if curent_category_name in self.dataframe_product['Kategorie 4'].values:
                dict_current['category_id'] = self.dict_category_number[curent_category_name]
                dict_current['category_name'] = curent_category_name
                dict_current['super_category_id'] = self.dict_category_number[self.dataframe_product[self.dataframe_product['Kategorie 4'] == curent_category_name]['Kategorie 3'].values[0]]
                dataframe_category = dataframe_category.append(dict_current, ignore_index=True)
                dict_current.clear()
                continue
            if curent_category_name in self.dataframe_product['Kategorie 5'].values:
                dict_current['category_id'] = self.dict_category_number[curent_category_name]
                dict_current['category_name'] = curent_category_name
                dict_current['super_category_id'] = self.dict_category_number[self.dataframe_product[self.dataframe_product['Kategorie 5'] == curent_category_name]['Kategorie 4'].values[0]]
                dataframe_category = dataframe_category.append(dict_current, ignore_index=True)
                dict_current.clear()
                continue
            if curent_category_name in self.dataframe_product['Kategorie 6'].values:
                dict_current['category_id'] = self.dict_category_number[curent_category_name]
                dict_current['category_name'] = curent_category_name
                dict_current['super_category_id'] = self.dict_category_number[self.dataframe_product[self.dataframe_product['Kategorie 6'] == curent_category_name]['Kategorie 5'].values[0]]
                dataframe_category = dataframe_category.append(dict_current, ignore_index=True)
                dict_current.clear()
                continue
            if curent_category_name in self.dataframe_product['Kategorie 7'].values:
                dict_current['category_id'] = self.dict_category_number[curent_category_name]
                dict_current['category_name'] = curent_category_name
                dict_current['super_category_id'] = self.dict_category_number[self.dataframe_product[self.dataframe_product['Kategorie 7'] == curent_category_name]['Kategorie 6'].values[0]]
                dataframe_category = dataframe_category.append(dict_current, ignore_index=True)
                dict_current.clear()
                continue
        return dataframe_category

    ###############################product dataframe######################################################################
    def get_product(self):
        dict_current = dict()
        dict_category_number = self.format_category_id()
        dataframe_product_category = pd.DataFrame(columns=['product_id', 'product_name', 'category_id'])
        for row_index in range(len(self.dataframe_product)):
            dict_current['product_id'] = self.dataframe_product['Produkt_ID'][row_index]
            dict_current['product_name'] = self.dataframe_product['Produkt_Name'][row_index]
            category_id = 0
            if pd.notna(self.dataframe_product['Kategorie 1'][row_index]):
                category_id = dict_category_number[self.dataframe_product['Kategorie 1'][row_index]]
            if pd.notna(self.dataframe_product['Kategorie 2'][row_index]):
                category_id = dict_category_number[self.dataframe_product['Kategorie 2'][row_index]]
            if pd.notna(self.dataframe_product['Kategorie 3'][row_index]):
                category_id = dict_category_number[self.dataframe_product['Kategorie 3'][row_index]]
            if pd.notna(self.dataframe_product['Kategorie 4'][row_index]):
                category_id = dict_category_number[self.dataframe_product['Kategorie 4'][row_index]]
            if pd.notna(self.dataframe_product['Kategorie 5'][row_index]):
                category_id = dict_category_number[self.dataframe_product['Kategorie 5'][row_index]]
            if pd.notna(self.dataframe_product['Kategorie 6'][row_index]):
                category_id = dict_category_number[self.dataframe_product['Kategorie 6'][row_index]]
            if pd.notna(self.dataframe_product['Kategorie 7'][row_index]):
                category_id = dict_category_number[self.dataframe_product['Kategorie 7'][row_index]]
            dict_current['category_id'] = category_id
            dataframe_product_category = dataframe_product_category.append(dict_current, ignore_index=True)
            dict_current.clear()
        return dataframe_product_category

    #####################################product url#############################################################
    def get_product_price(self):
        dataframe_product_price = pd.DataFrame(columns=['product_id','product_price','price_date'])
        dict_price = dict()
        for index in range(len(self.dataframe_product)):
            try:
                product_id = self.dataframe_product['Produkt_ID'][index]
                #print('product_id',product_id)
                temp_url = 'https://www.idealo.de/offerpage/pricechart/api/{}?period=P1Y'.format(product_id)
                with os.popen('curl -k {}'.format(temp_url)) as p:
                    result = p.read()
                    dict_result = json.loads(result)
                    #print('dict_result',dict_result)
                    data_result = dict_result['data']
                   # print('data_result',data_result)
                    for temp_data in data_result:
                        current_date = temp_data['x']
                        current_price = temp_data['y']
                        dict_price.clear()
                        dict_price['product_id'] = product_id
                        dict_price['product_price'] = current_price
                        dict_price['price_date'] = current_date
                        dataframe_product_price = dataframe_product_price.append(dict_price,ignore_index=True)
            except Exception as e:
                pass
        return dataframe_product_price





