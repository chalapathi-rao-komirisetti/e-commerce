from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

def Saco(input1):

    url = 'https://www.saco.sa/en/'

    item_list = [input1]

    finaldict = dict()
    counttemp = 0

    for iii in item_list:

        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(5)

        PageNum = 0

        LoopFlag = True

        while (LoopFlag):

            driver.get('{}en/All-Saco-Categories/c/MC?q={}%3Arelevance&page={}'.format(driver.current_url.split('en/')[0],iii.replace(' ', '+'), PageNum))

            PageNum = PageNum + 1

            time.sleep(30)

            for i, ii in zip(driver.find_elements(By.XPATH, '//img[@class="img-fluid"]')[::2],driver.find_elements(By.XPATH, '//div[@class="price"]')[::2]):
                print(i.get_attribute('src'))
                print(i.get_attribute('title'))
                print(PageNum)
                print('\n')
                finaldict[counttemp] = ['Saco', iii, i.get_attribute('title'), i.get_attribute('src'), ii.text.split()[1]]
                counttemp = counttemp + 1

            time.sleep(5)

            driver.delete_all_cookies()

            LoopFlag = False
    l = []

    for i in finaldict.keys():
        print(l.append(finaldict[i]))

    data = pd.DataFrame(l, columns=['Product Source', 'Product Category', 'Product Name', 'Product Image', 'Product Price'])

    return data
#Saco('Iphone 14 plus 256 Gb starlight')