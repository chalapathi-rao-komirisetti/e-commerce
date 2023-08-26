from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def Extras(input1):

    url = 'https://www.extra.com/en-sa/'

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)

    a = []
    aa = []
    aaa = []
    aaaaa = []

    item_list = [input1]

    final_dict = dict()

    for iii in item_list:

        count = 0

        seacrh_button = driver.find_element(by='id', value='search-input')

        seacrh_button.clear()

        seacrh_button.send_keys(iii)

        time.sleep(5)

        seacrh_button.send_keys(Keys.ENTER)

        LoopFlag = True

        try:
            while (LoopFlag):

                time.sleep(5)
                driver.get(driver.current_url.split('&pageSize=')[0] + '&pageSize=24&pg={}&sort=relevance'.format(count))

                time.sleep(15)
                for i in driver.find_elements(By.XPATH, "//span[@class='product-name-data']"):
                    print(i.text)
                    a.append(i.text)
                    aaaaa.append(iii)

                time.sleep(15)
                for i in driver.find_elements(By.XPATH, "//span[@class='price svelte-11dx6yr']"):
                    if ('/' not in i.text):
                        print(i.text)
                        aa.append(i.text)

                time.sleep(25)
                for i in driver.find_elements(By.XPATH, "//img[@class='img-hover svelte-mm371p']"):
                    print(i.get_attribute('src'))
                    aaa.append(i.get_attribute('src'))

                time.sleep(5)
                count = count + 1
                time.sleep(5)
                LoopFlag = driver.find_element(By.XPATH,'//i[@class="c_icon_new c_icon_new--chevron_right svelte-1998jhb"]').is_displayed()

                LoopFlag = False

        except NoSuchElementException:
            print('\n')
            print('ERROR ERROR ERROR ERROR')
            LoopFlag = False
            pass


    for i in range(len(a)):
        final_dict[i] = ['Extras', aaaaa[i], a[i], aa[i], aaa[i]]

    temp = []

    for i in final_dict.keys():
        temp.append(final_dict[i])

    data = pd.DataFrame(data=temp, columns=['Product Source', 'Product Category', 'Product Name', 'Product Price','Product Image'])

    data.to_excel('main_result_2.xlsx')

    return data
#Extras('Iphone 14 plus 256 gb starlight')