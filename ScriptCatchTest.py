# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# # utag_data = [{"site_tld": "de",
# #               "page_type": "OFFERS_OF_PRODUCT",
# #               "client_ip": "91.15.216.212",
# #               "site_currency": "EUR",
# #               "page_levels": ["Elektroartikel", "Haushaltselektronik", "Elektro-Großgeräte", "Backöfen",
# #                               "Neff BVR 5522 N"],
# #               "product_code": 4621842,
# #               "product_ids": [4621842],
# #               "product_names": ["Neff BVR 5522 N"],
# #               "product_category_ids": [19194],
# #               "product_available_since": "20141013",
# #               "number_of_offers": 31,
# #               "number_of_checkout_offers": 8,
# #               "number_of_variants": 1,
# #               "prices_last_updated": "2020-10-17T11:16",
# #               "index_of_first_checkout_offer": 1,
# #               "number_of_shoe_sizes": 0,
# #               "promoline": False}]
#
# chrome_driver = webdriver.Chrome(executable_path='chrome_driver/chromedriver')
#
# url = "https://www.idealo.de/preisvergleich/OffersOfProduct/4578824_-hb674gb-1-siemens.html"
#
# chrome_driver.get(url)
#
# time.sleep(5)
#
#
# product_info_tag_name = chrome_driver.find_element_by_id('tagManagerDataLayer').tag_name
# #product_info = chrome_driver.find_element(By.ID,'tagManagerDataLayer').text
# #product_info = chrome_driver.execute_script('tagManagerDataLayer')
# #product_info = chrome_driver.find_element_by_id('tagManagerDataLayer').text
# #product_info = chrome_driver.find_element_by_tag_name('script') #product_info: <selenium.webdriver.remote.webelement.WebElement (session="bd95e98b8aa99d7ae4e9a6471132a74d", element="83dad329-c1f6-4694-8c41-917233c60e32")>
# product_info = chrome_driver.find_element_by_id('tagManagerDataLayer')
# print("product_info_tag_name:",product_info_tag_name)
# print("product_info:",product_info)
#
# #print(chrome_driver.get_cookie('cookie'))
#
# chrome_driver.quit()

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import json

# # utag_data = [{"site_tld": "de",
# #               "page_type": "OFFERS_OF_PRODUCT",
# #               "client_ip": "91.15.216.212",
# #               "site_currency": "EUR",
# #               "page_levels": ["Elektroartikel", "Haushaltselektronik", "Elektro-Großgeräte", "Backöfen",
# #                               "Neff BVR 5522 N"],
# #               "product_code": 4621842,
# #               "product_ids": [4621842],
# #               "product_names": ["Neff BVR 5522 N"],
# #               "product_category_ids": [19194],
# #               "product_available_since": "20141013",
# #               "number_of_offers": 31,
# #               "number_of_checkout_offers": 8,
# #               "number_of_variants": 1,
# #               "prices_last_updated": "2020-10-17T11:16",
# #               "index_of_first_checkout_offer": 1,
# #               "number_of_shoe_sizes": 0,
# #               "promoline": False}]
#
# chrome_driver = webdriver.Chrome(executable_path='chrome_driver/chromedriver')
#
# url = "https://www.idealo.de/preisvergleich/OffersOfProduct/4578824_-hb674gb-1-siemens.html"
#
# chrome_driver.get(url)
#
# time.sleep(5)
#
#
# #product_info_tag_name = chrome_driver.find_element_by_id('tagManagerDataLayer').tag_name
#
# current_html = chrome_driver.page_source
# bs=BeautifulSoup(current_html,'html.parser')
# # print(bs)
# product_info = str.split(bs.find("script",{"id":"tagManagerDataLayer"}).string,'=')[1]
# product_info = product_info[0:product_info.find(';')]
#
# json_product = js.loads(product_info)
# print(json_product[0]['product_ids'])
#
# chrome_driver.quit()

def product_info(url):
    # utag_data = [{"site_tld": "de",
    #               "page_type": "OFFERS_OF_PRODUCT",
    #               "client_ip": "91.15.216.212",
    #               "site_currency": "EUR",
    #               "page_levels": ["Elektroartikel", "Haushaltselektronik", "Elektro-Großgeräte", "Backöfen",
    #                               "Neff BVR 5522 N"],
    #               "product_code": 4621842,
    #               "product_ids": [4621842],
    #               "product_names": ["Neff BVR 5522 N"],
    #               "product_category_ids": [19194],
    #               "product_available_since": "20141013",
    #               "number_of_offers": 31,
    #               "number_of_checkout_offers": 8,
    #               "number_of_variants": 1,
    #               "prices_last_updated": "2020-10-17T11:16",
    #               "index_of_first_checkout_offer": 1,
    #               "number_of_shoe_sizes": 0,
    #               "promoline": False
    chrome_driver = webdriver.Chrome(executable_path='chrome_driver/chromedriver')
    chrome_driver.get(url)
    time.sleep(5)

    current_html = chrome_driver.page_source
    bs = BeautifulSoup(current_html, 'html.parser')
    # print(bs)
    product_info = str.split(bs.find("script", {"id": "tagManagerDataLayer"}).string, '=')[1]
    #print("product_info:",product_info)
    product_info = product_info[0:product_info.find(';')]
    #print("product_info:",product_info)
    json_product = json.loads(product_info)
    #print("page_levels:",json_product[0]['page_levels'])
    #print("product_ids:",json_product[0]['product_ids'])
    dict_product_info = {}
    dict_product_info['Kategorie 1']= json_product[0]['page_levels'][0]
    dict_product_info['Kategorie 2'] = json_product[0]['page_levels'][1]
    dict_product_info['Kategorie 3'] = json_product[0]['page_levels'][2]
    dict_product_info['Kategorie 4'] = '\''+json_product[0]['page_levels'][3]+'\''
    dict_product_info['Produkt_Name'] = json_product[0]['page_levels'][4]
    dict_product_info['Produkt_ID'] = str(json_product[0]['product_ids'][0])
    print("dict_product_info:",dict_product_info)
    return dict_product_info

#### save data in Excel csv file
import os.path
# from os import path
# dict_info = product_info('https://www.idealo.de/preisvergleich/OffersOfProduct/4578824_-hb674gb-1-siemens.html')
# fname = "IdealoProductInfo.csv"
# FileExist = 1
# if not path.exists(fname):
#     FileExist = 0
# f = open(fname,"a",encoding='utf-8')
# if FileExist == 0:
#     f.write("Kategorie 1, Kategorie 2, Kategorie 3, Kategorie 4, Produkt_Name, Produkt_ID")
#     f.write("\n"+dict_info['Kategorie 1']+";"+ dict_info['Kategorie 2']+";"+dict_info['Kategorie 3']+";"+dict_info['Kategorie 4']+";"
#             +dict_info['Produkt_Name']+";"+dict_info['Produkt_ID'])


if __name__ == '__main__':
    product_info('https://www.idealo.de/preisvergleich/OffersOfProduct/4626516_-hbg675b-1-bosch.html')

