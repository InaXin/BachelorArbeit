from selenium import webdriver
import time
from bs4 import BeautifulSoup
import json
import pandas as pd

def productInfoCatch2(url):
    chrome_driver = webdriver.Chrome(executable_path = 'chrome_driver/chromedriver')
    chrome_driver.get(url)
    time.sleep(5)

    current_html = chrome_driver.page_source
    bs = BeautifulSoup(current_html,'html.parser')

    product_info = str.split(bs.find("script", {"id": "tagManagerDataLayer"}).string, '=')[1]
    product_info = product_info[0:product_info.find(';')]
    json_product = json.loads(product_info)
    category_list = json_product[0]["page_levels"]
    #print("category_list",category_list)

    div_list = bs.find_all('div',{"class":'offerList-item'})
    #id_list = str.split(div_list[div_list.find("productId"):div_list.find("}")],":")[1]
    result_id_list = []
    for current_div in div_list:
        current_div = str(current_div)
        print("current_div",current_div)
        id = str.split(current_div[current_div.find("productId"):current_div.find('}')],':"')[1].strip()[:-1]
        print('id',id)
        print('type',type(id))
        result_id_list.append(id)
    print("result_id_list:",result_id_list)
    print(len(result_id_list))

    result_name_list = []
    name_list = bs.find_all("div", {"class":"offerList-item-imageWrapper"})
    #name_list = str.split(name_list[name_list.find("title="):name_list.find("/>")],"=")[1]

    for current_name in name_list:
        current_name = str(current_name.find("img"))
        #print("current_name",current_name)
        current_name = str.split(current_name[current_name.find("title="):current_name.find('"/>')],'="')[1]
        result_name_list.append(current_name)
    #print("result_name_list:",result_name_list)
    #print(len(result_name_list))
    chrome_driver.quit()
    result = []
    for i in range (len(result_id_list)):
        result_temp = []
        for category in category_list:
            result_temp.append(category)
        result_temp.append(result_name_list[i])
        result_temp.append(result_id_list[i])
        result.append(result_temp)
    print("result", result)
    return result

#print(productInfoCatch2('https://www.idealo.de/preisvergleich/ProductCategory/19194.html'))

file_name = 'SubHtmlExcel201-220.xlsx'
excel_html = pd.ExcelFile(file_name)
dataframe_html = excel_html.parse(excel_html.sheet_names[0])
excel_name = 'Daten/Html(%s)ToProductExcel.xlsx'% file_name[12:-5]
#print(excel_name)

current_result = []
for current_html in dataframe_html['ProductCategory']:
    try:
        current_result_first_page = productInfoCatch2(current_html)
        current_result.append(current_result_first_page)
    except Exception as e:
        pass

dataframe_temp = pd.DataFrame(columns=['Kategorie 1','Kategorie 2','Kategorie 3','Kategorie 4','Produkt_Name','Produkt_ID'])
for list_temp in current_result:
    dict_temp = dict()
    for item in list_temp:
        current_length = len(item)
        dict_temp['Produkt_ID'] = item[current_length-1]
        dict_temp['Produkt_Name'] = item[current_length-2]
        for index in range(current_length-2):
            dict_temp[dataframe_temp.columns[index]] = item[index]

        dataframe_temp = dataframe_temp.append(dict_temp,ignore_index=True)
        dict_temp.clear()
    dataframe_temp.to_excel(excel_name,index = False)


