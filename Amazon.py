from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

def Amazon(input1):
    
    url = 'https://www.amazon.sa/?language=en_AE'
    
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    
    classes = [
        'sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 AdHolder sg-col s-widget-spacing-small sg-col-4-of-20',
        'sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20']
    
    product_price = []
    
    final_dict = dict()
    count_dict = 0
    
    item_list = [input1]
    
    for iii3 in item_list:
    
        a = driver.find_element(by='id', value='twotabsearchtextbox')
        b = driver.find_element(by='id', value='nav-search-submit-button')
    
        a.clear()
    
        a.send_keys(iii3)
    
        time.sleep(5)
    
        b.click()
    
        LoopFlag = True
    
        try:
            while (LoopFlag):
    
                time.sleep(5)
                driver.current_url

                temp = []
    
                for i in classes:
                    temp = temp + driver.find_elements(By.XPATH, '//div[@class="{}"]'.format(i))
    
                temptemp = []
    
                for i in temp:
                    temptemp.append(i.text)
    
                for i in temptemp:
                    if 'SAR' not in i:
                        print("Deleted Item is : ", i)
                        del temptemp[temptemp.index(i)]
    
                IMG_OBJ = driver.find_elements(By.XPATH, '//img[@class="s-image"]')
                
                for i in IMG_OBJ:
                    for ii in temptemp:
                        if i.get_attribute('alt').replace("Sponsored Ad – ", "").replace("...", "") in ii:
                            for iii in ii.split('\n'):
                                tempvar = ii.split('\n')
                                if ('SAR' in iii and '.' not in iii and len(str(iii).split()) == 1 and '-' not in tempvar[
                                    tempvar.index(iii) + 1] and iii.replace(',', '')[
                                                                3:].isnumeric()):  # and '-' not in tempvar[tempvar.index(ii)+1]

                                    final_dict[count_dict] = ['AMAZON', iii3,
                                                              i.get_attribute('alt').replace("Sponsored Ad – ", ""), float(iii[3:].replace(',', '') + '.' + str(tempvar[tempvar.index(iii) + 1]).split()[0][:2]), i.get_attribute('src')]
                                    count_dict = count_dict + 1
                                    break
    
                            break
    
                time.sleep(5)
                NextButton = driver.find_element(By.PARTIAL_LINK_TEXT, 'Next')
                NextButton.click()
                LoopFlag = NextButton.is_enabled
    
                LoopFlag = False

                driver.delete_all_cookies()
    
        except NoSuchElementException:
            print('\n')
            print('ERROR ERROR ERROR ERROR')
            LoopFlag = False
            pass
    
    temp = []
    
    for i in final_dict.keys():
        temp.append(final_dict[i])
    
    data = pd.DataFrame(data=temp,columns=['Product Source', 'Product Category', 'Product Name', 'Product Price', 'Product Image'])
    
    data.to_excel('main_result.xlsx')

    return data
#amazon('iphone 14 plus 256 gb starlight')