from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import numpy as np

proxy_arr = [
    #'192.240.46.123:80',
    #'192.240.46.126:80',
    #'212.62.95.45:1080',
    '213.234.29.96:1080',
    #'67.201.33.70:9100',

]

chrome_options = webdriver.ChromeOptions()

proxy = np.random.choice(proxy_arr)
print(proxy)

chrome_options.add_argument('--proxy-server=http://' + proxy)

chrome_driver = webdriver.Chrome(executable_path='chrome_driver/chromedriver',chrome_options=chrome_options)

chrome_driver.get("https://www.google.com")

print(chrome_driver.page_source)