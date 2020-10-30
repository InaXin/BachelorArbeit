from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import json
import pandas as pd

def productInfoCatch(url):

    chrome_driver = webdriver.Chrome(executable_path='chrome_driver/chromedriver')
    chrome_driver.get(url)
    time.sleep(2)
    # all products in first page
    # //*[@id="productcategory"]/main/div[3]/div[2]/div[3]/div[1]/a
    # //*[@id="productcategory"]/main/div[3]/div[2]/div[3]/div[2]/a
    # //*[@id="productcategory"]/main/div[3]/div[2]/div[3]/div[3]/a
    # ........
    # //*[@id="productcategory"]/main/div[3]/div[2]/div[3]/div[36]/a
    web_element = chrome_driver.find_element_by_xpath('//*[@id="productcategory"]/main/div[3]/div[2]/div[3]')
    list_a = web_element.find_elements(By.TAG_NAME, "a")

    datastore = []
    for index in range(len(list_a)):
        try:
            current_xPath = '//*[@id="productcategory"]/main/div[3]/div[2]/div[3]/div['+str(index+1)+']/a'

            current_a = chrome_driver.find_element_by_xpath(current_xPath)
            current_href = current_a.get_property('href')
            current_product = 'window.open(\"' + current_href + '\");'

            now_handle = chrome_driver.current_window_handle
            #print('now_handle',now_handle)

            chrome_driver.execute_script(current_product)
            chrome_driver.implicitly_wait(2)
            all_handles = chrome_driver.window_handles
            #print('all_handles',all_handles)
            for handle in all_handles:
                if now_handle != handle:
                    chrome_driver.switch_to.window(handle)
                    current_html = chrome_driver.page_source
                    bs = BeautifulSoup(current_html, 'html.parser')
                    # print(bs)
                    product_info = str.split(bs.find("script", {"id": "tagManagerDataLayer"}).string, '=')[1]
                    product_info = product_info[0:product_info.find(';')]
                    json_product = json.loads(product_info)

                    result_info = json_product[0]['page_levels']
                    #print("     "+"page_levels:",json_product[0]['page_levels'])
                    #print("     "+"product_ids:", json_product[0]['product_ids'])
                    result_info.append(str(json_product[0]['product_ids'][0]))
                    datastore.append(result_info)
                    # dict_product_info = {}
                    # for i in range(4):
                    #     if json_product[0]['page_levels'][i] is not None:
                    #         dict_product_info['Kategorie'+str(i+1)] = json_product[0]['page_levels'][i]
                    #     else:
                    #         dict_product_info['Kategorie' + str(i + 1)] = None
                    # dict_product_info['Produkt_Name'] = json_product[0]['page_levels'][-1]
                    # dict_product_info['Produkt_ID'] = str(json_product[0]['product_ids'][0])
                    # print("     "+"dict_product_info:", dict_product_info)
                    # datastore.append(dict_product_info)
                    chrome_driver.close()
            chrome_driver.switch_to.window(now_handle)
        except Exception as e:
            pass
    #print('datastore',datastore)
    chrome_driver.quit()
    print('datastore',datastore)
    return datastore

excel_html = pd.ExcelFile('TestInfo.xlsx')
dataframe_html = excel_html.parse(excel_html.sheet_names[0])

#print(dataframe_html['ProductCategory'])
current_result = []
for current_html in dataframe_html['ProductCategory']:
    #Backöfen last page
    #//*[@id="productcategory"]/main/div[3]/div[2]/nav/ul/li[4]/a
    #Bartschneider & Haarschneider
    #//*[@id="productcategory"]/main/div[3]/div[2]/nav/ul/li[4]/a
    chrome_driver = webdriver.Chrome(executable_path='chrome_driver/chromedriver')
    chrome_driver.get(current_html)
    time.sleep(2)

    current_last_page = chrome_driver.find_element_by_xpath('//*[@id="productcategory"]/main/div[3]/div[2]/nav/ul/li[4]/a').text
    current_last_page = int(current_last_page)
    #print('current_last_page',type(current_last_page),current_last_page)

    #product info in first page
    current_result_first_page = productInfoCatch(current_html)
    current_result.append(current_result_first_page)
    #product info from second page to last page
    #for index in range(current_last_page-1):
    for index in range(1):
        change_str = 'I16-'+str(15*(index+1))
        str_list = list(current_html)
        str_list.insert(-5, change_str)
        new_html = ''.join(str_list)
        #print('new_html', new_html)
        current_result_other_page = productInfoCatch(new_html)
        current_result.append(current_result_other_page)

    #print('current_result',current_result)

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
    dataframe_temp.to_excel('DataToexcelTest.xlsx',index = False)