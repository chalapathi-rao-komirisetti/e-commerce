from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def JarirBookStore(input1):

    driver = webdriver.Chrome()
    driver2 = webdriver.Chrome()

    driver.maximize_window()
    driver2.maximize_window()

    item_list = [input1]

    count = 0
    finaldict = dict()

    driver.get('https://www.jarir.com/sa-en/catalogsearch/result?search=school-bags')
    driver2.get('https://www.jarir.com/sa-en/catalogsearch/result?search=school-bags')

    time.sleep(30)
    time.sleep(30)

    driver.find_element(By.XPATH, '//button[@class="button button--standard button__contrylangSelector"]').click()
    driver2.find_element(By.XPATH, '//button[@class="button button--standard button__contrylangSelector"]').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//button[@class="button button--secondary button--fluid ar-number"]').click()
    driver2.find_element(By.XPATH, '//button[@class="button button--secondary button--fluid ar-number"]').click()

    time.sleep(30)

    a = driver.find_element(By.XPATH, '//div[@class="input search-form__input-wrapper"]')
    a = a.find_element(By.TAG_NAME,'input')

    a.clear()

    a.send_keys(input1)

    time.sleep(5)

    a.send_keys(Keys.ENTER)

    time.sleep(2)

    for iii in item_list:

        time.sleep(15)

        html = driver.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.END)

        time.sleep(5)

        driver.find_element(By.XPATH, '//button[@class="button button--floating-small button--floating-white"]').click()
        for i in driver.find_elements(By.XPATH, '//a[@class="product-tile__link"]'):
            try:
                driver2.get(i.get_attribute('href'))
                time.sleep(15)

                finaldict[count] = ['JarirBookstore', iii,driver2.find_element(By.XPATH, '//h2[@class="product-title__title"]').text + ' ' + driver2.find_element(By.XPATH,'//p[@class="product-title__info product-title__info--pdp"]').text,driver2.find_elements(By.XPATH, '//div[@class="product-view__price"]')[0].text.split('\n')[0],
                                    'https://' + driver2.find_elements(By.XPATH, '//img[@class="image image--contain"]')[1].get_attribute('data-src').split('https://')[2]]

                count = count + 1
                print('\n')

            except NoSuchElementException:
                print('\n')
                print('ERROR ERROR ERROR ERROR')
                pass

    l = []

    for i in finaldict.keys():
        print(l.append(finaldict[i]))

    data = pd.DataFrame(l, columns=['Product Source', 'Product Category', 'Product Name', 'Product Price', 'Product Image'])

    data.to_excel('C:/Users/ASUS/Documents/main result 5.xlsx')

    return data

#JarirBookStore('rich dad poor dad')