from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

chrome_driver = webdriver.Chrome(executable_path='chrome_driver/chromedriver')

chrome_driver.get("https://www.idealo.de/")

###click "Kategorien" button
category_path = '//*[@id="mainproductcategory"]/header/div[3]/div/div[1]/div/a'
chrome_driver.find_element_by_xpath(category_path).click()
time.sleep(2)

#Elektroartikel
#//*[@id="mainproductcategory"]/header/div[3]/div/div[1]/div/div/nav/ul[1]/li[1]/a
#//*[@id="mainproductcategory"]/header/div[3]/div/div[1]/div[1]/div/div/nav/ul[1]/li[1]/a
#Sport&Outdoor
#//*[@id="mainproductcategory"]/header/div[3]/div/div[1]/div[1]/div/div/nav/ul[1]/li[2]/a
#...........
list_html = []
web_element1 = chrome_driver.find_element_by_xpath('//*[@id="mainproductcategory"]/header/div[3]/div/div[1]/div/div/nav/ul[1]')
#list li of super 11 categories
list_li1 = web_element1.find_elements(By.TAG_NAME, "li")
print("list_li:",list_li1)
for index1 in range(len(list_li1)):
    current_xPath1 ='//*[@id="mainproductcategory"]/header/div[3]/div/div[1]/div/div/nav/ul[1]/li['+str(index1+1)+']/a'
    print (str(index1+1)+'. '+chrome_driver.find_element_by_xpath(current_xPath1).text)

    chrome_driver.find_element_by_xpath(current_xPath1).click()

    time.sleep(2)
    #Elektroartikel
        #Backöfen
        #//*[@id="mainproductcategory"]/header/div[3]/div/div[1]/div/div/nav/ul[2]/li[1]/a
        #//*[@id="mainproductcategory"]/header/div[3]/div/div[1]/div[1]/div/div/nav/ul[2]/li[1]/a
        #Bartschneider & Haarschneider
        #//*[@id="mainproductcategory"]/header/div[3]/div/div[1]/div[1]/div/div/nav/ul[2]/li[2]/a
        #Computer
        #//*[@id="mainproductcategory"]/header/div[3]/div/div[1]/div[1]/div/div/nav/ul[2]/li[3]/a
        #Drohnen
        #//*[@id="mainproductcategory"]/header/div[3]/div/div[1]/div[1]/div/div/nav/ul[2]/li[4]/a
        #.............
    #Sport&Outdoor
        #E-Bikes
        #//*[@id="mainproductcategory"]/header/div[3]/div/div[1]/div[1]/div/div/nav/ul[3]/li[1]/a
        # E-Scooter
        #//*[@id="mainproductcategory"]/header/div[3]/div/div[1]/div[1]/div/div/nav/ul[3]/li[2]/a
        #..............
        #mehr
        #//*[@id="mainproductcategory"]/header/div[3]/div/div[1]/div[1]/div/div/nav/ul[3]/li[21]/a
    #..............
    web_element2 = chrome_driver.find_element_by_xpath('//*[@id="mainproductcategory"]/header/div[3]/div/div[1]/div/div/nav/ul[2]')
    list_li2 = web_element2.find_elements(By.TAG_NAME, "li")
    for index2 in range(len(list_li2)):
        try:
            current_xPath2 = '//*[@id="mainproductcategory"]/header/div[3]/div/div[1]/div/div/nav/ul['+ str(index1+2)+']/li['+str(index2+1)+']/a'
            print('     '+str(index2+1)+')'+ chrome_driver.find_element_by_xpath(current_xPath2).text)
            current_a = chrome_driver.find_element_by_xpath(current_xPath2)
            current_href = current_a.get_property('href')
            list_html.append(current_href)
        except Exception as e:
            pass
print("list_html",list_html)
print(len(list_html))
chrome_driver.quit()

df = pd.DataFrame(list_html, columns=['ProductCategory'])

df.to_excel("Daten_Html/IdealoProductCategoryHtml.xlsx", index=False)