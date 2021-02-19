from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd


### sub html scraping recursion
list_html = []
def get_productCategory(url):
    if url.find('SubProductCategory') == -1:
        list_html.append(url)
    else:
        chrome_driver = webdriver.Chrome(executable_path='chrome_driver/chromedriver')
        chrome_driver.get(url)
        time.sleep(2)

        # //*[@id="moreMainCategories"]/ul/li[1]/a
        # //*[@id="moreMainCategories"]/ul/li[2]/a
        # .......
        # //*[@id="moreMainCategories"]/ul/li[33]
        web_element = chrome_driver.find_element_by_xpath('//*[@id="moreMainCategories"]/ul')
        list_li = web_element.find_elements(By.TAG_NAME, "li")

        for index in range(len(list_li)):
            try:
                current_xPath = '//*[@id="moreMainCategories"]/ul/li[' + str(index + 1) + ']/a'
                current_a = chrome_driver.find_element_by_xpath(current_xPath)
                current_href = current_a.get_property('href')
                get_productCategory(current_href)
            except Exception as e:
                pass
        chrome_driver.quit()
    return list_html

# result_list_html = get_productCategory('https://www.idealo.de/preisvergleich/SubProductCategory/3932.html')
# df = pd.DataFrame(result_list_html, columns=['ProductCategory'])
# df.to_excel("Test.xlsx", index=False)

excel_html = pd.ExcelFile('Daten_Html/SubProductCategoryHtml(61-70).xlsx')
dataframe_html = excel_html.parse(excel_html.sheet_names[0])

for current_html in dataframe_html['SubProductCategory']:
    result_list_html = get_productCategory(current_html)
    df = pd.DataFrame(result_list_html,columns=['ProductCategory'])
    df.to_excel("Daten_Html/SubProductCategory(61-70)ToProductCategoryHtml.xlsx",index= False)





