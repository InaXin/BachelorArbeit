from selenium import webdriver
import pandas as pd
import time
from bs4 import BeautifulSoup


class PageTurning:

    def __init__(self,excel_path:str):
        self.excel_file = pd.ExcelFile(excel_path)
        self.dataframe_html = self.excel_file.parse(self.excel_file.sheet_names[0])

    def pageTurning(self):
        dataframe_html = self.dataframe_html
        list_new_html = []
        for current_html in dataframe_html['ProductCategory']:
            print(current_html)
            chrome_driver = webdriver.Chrome(executable_path='chrome_driver/chromedriver')
            chrome_driver.get(current_html)
            time.sleep(2)
            current_html_source = chrome_driver.page_source
            bs = BeautifulSoup(current_html_source,'html.parser')
            current_last_page_nummer = int(bs.find_all("li", {"class": "pagination-item"})[-2].find("a").text.strip())

            # product info from second page to last page
            # for index in range(current_last_page-1):
            for index in range(current_last_page_nummer-1):  ### second page to last page
                change_str = 'I16-' + str(15 * (index + 1))
                str_list = list(current_html)
                str_list.insert(-5, change_str)
                new_html = ''.join(str_list)
                list_new_html.append(new_html)

        df = pd.DataFrame(list_new_html, columns=['ProductCategory'])
        df.to_excel("Daten_Html(Second-LastPage)/(2.-last)AllProductCategoryHtmlDropDuplicates(1-100).xlsx", index=False)


if __name__ == '__main__':
    pageTurning = PageTurning('Daten_Html/AllProductCategoryHtmlDropDuplicates(1-100).xlsx')
    pageTurning.pageTurning()