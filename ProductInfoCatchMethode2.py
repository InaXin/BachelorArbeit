from selenium import webdriver
import time
from bs4 import BeautifulSoup
import json
import os
import pandas as pd

def productInfoCatch2(url):

    chrome_driver = webdriver.Chrome(executable_path = 'chrome_driver/chromedriver')
    chrome_driver.get(url)
    time.sleep(2)

    current_html = chrome_driver.page_source
    bs = BeautifulSoup(current_html,'html.parser')

    ###category scraping
    product_info = str.split(bs.find("script", {"id": "tagManagerDataLayer"}).string, '=')[1]
    product_info = product_info[0:product_info.find(';')]
    json_product = json.loads(product_info)
    category_list = json_product[0]["page_levels"]
    print("category_list",category_list)

    id_name_list = bs.find_all("div", {"class":"offerList-item-imageWrapper"})
    print("len_id_name_list",len(id_name_list))

    result_id_list = []
    result_name_list = []
    index = 1
    for current_id_name in id_name_list:
        current_id_name = str(current_id_name.find("img"))
        #print(current_id_name)

        ###product id scraping
        if '/de_DE' in current_id_name:
            current_id = str(current_id_name[current_id_name.find("product/"):current_id_name.find("/de_DE")])
        elif '/s1' in current_id_name:
            current_id = str(current_id_name[current_id_name.find("Product/"):current_id_name.find("/s1")])
        else:
            current_id = "IDNoFound"

        if current_id != "IDNoFound":
            current_id = current_id[:current_id.rfind("/"):-1][::-1]

        ###product name scraping
        current_name = str(current_id_name[current_id_name.find("title="):current_id_name.find('/>')])[7:-1]
        if current_name == '':
            current_name = 'NameNoFound'

        print('current_id',str(index)+")",current_id)
        print('current_name',str(index)+")",current_name)
        index = index+1
        result_id_list.append(current_id)
        result_name_list.append(current_name)
    print("result_id_list",result_id_list)
    print(len(result_id_list))
    print("result_name-list",result_name_list)
    print(len(result_name_list))

    ###last page nummer scraping
    #current_last_page_nummer = int(bs.find_all("li", {"class": "pagination-item"})[-2].find("a").text.strip())

    chrome_driver.quit()

    result_product_info = []
    for i in range (len(result_id_list)):
        result_temp = []
        result_temp.append(result_id_list[i])
        result_temp.append(result_name_list[i])
        for category in category_list:
            result_temp.append(category)
        result_temp.append(url)
        result_product_info.append(result_temp)
    print("result_product_info", result_product_info)
    print(len(result_product_info))

    return result_product_info

#print(productInfoCatch2('https://www.idealo.de/preisvergleich/ProductCategory/3832.html'))

#=================read ProductCategory html Excel output proudct info======================
excel_file_name = 'Test.xlsx'
excel_html = pd.ExcelFile(excel_file_name)
dataframe_html = excel_html.parse(excel_html.sheet_names[0])

current_result = []
for current_html in dataframe_html['ProductCategory']:
    try:
        current_result_first_page_info = productInfoCatch2(current_html)
        current_result.append(current_result_first_page_info)
    except Exception as e:
        pass
print('current_result:',current_result)

#================ save data to json==========================================================
json_file_name = 'Test.json'
a = []
if not os.path.isfile(json_file_name):
    a.append(current_result)
    with open(json_file_name, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(a,ensure_ascii=False,indent=4))
else:
    with open(json_file_name) as feedsjson:
        feeds = json.load(feedsjson)
        #print('feeds',feeds)

    feeds.append(current_result)
    with open(json_file_name, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(feeds,ensure_ascii=False,indent=4))

