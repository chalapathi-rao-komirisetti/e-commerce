from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def Noon(input1):

    url = 'https://www.noon.com/saudi-en/'

    item_list = [input1]

    final_dict = dict()
    count = 0

    for iii in item_list:

        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(3)

        PageNum = 2

        seacrh_button = driver.find_element(by='id', value='searchBar')

        time.sleep(2)

        seacrh_button.send_keys(iii)

        time.sleep(2)

        seacrh_button.send_keys(Keys.ENTER)

        LoopFlag = True

        time.sleep(25)

        try:
            while (LoopFlag):

                driver2 = webdriver.Chrome()
                time.sleep(45)

                for i in driver.find_elements(By.XPATH, '//span[@class="sc-5e739f1b-0 gEERDr wrapper productContainer  "]'):
                    try:
                        driver2.get(i.find_element(By.TAG_NAME, 'a').get_attribute('href'))
                        time.sleep(5)

                        final_dict[count] = ['Noon', iii, driver2.find_element(By.TAG_NAME, 'h1').text,
                                             driver2.find_element(By.XPATH, '//div[@class="priceNow"]').text.split('\n')[0],
                                             driver2.find_element(By.XPATH,
                                                                  '//div[@class="swiper-container swiper-container-initialized swiper-container-vertical swiper-container-pointer-events"]').find_element(
                                                 By.TAG_NAME, 'img').get_attribute('src')]

                        count = count + 1

                    except NoSuchElementException:
                        print('\n')
                        print('ERROR ERROR ERROR ERROR')
                        pass

                driver.get(driver.current_url.split('?')[0] + '?limit=50&originalQuery=' + iii.replace(' ','%20') + '&page={}&q={}&searchDebug=false&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc'.format(PageNum, iii.replace(' ', '%20')))

                PageNum = PageNum + 1

                LoopFlag = driver.find_element(By.XPATH, '//img[@class="sc-b51db3f-1 bwDhlu"]').is_displayed()

                driver.delete_all_cookies()

                LoopFlag = False

        except NoSuchElementException:
            print('\n')
            print('ERROR ERROR ERROR ERROR')
            LoopFlag = False
            pass

        driver2.close()

    l = []

    for i in final_dict.keys():
        print(l.append(final_dict[i]))

    data = pd.DataFrame(l, columns=['Product Source', 'Product Category', 'Product Name', 'Product Price', 'Product Image'])

    return data

#Noon('Iphone 14 plus 256 gb starlight')