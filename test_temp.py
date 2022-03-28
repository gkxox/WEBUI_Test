import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait




driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://localhost:8089/Home/user/login.html')

def find_ele(lacator):

     return WebDriverWait(driver,10,1).until(lambda x:x.find_element(*lacator))

find_ele((By.XPATH,'//*[@id="username"]')).send_keys("13488888888")
find_ele((By.XPATH,'//*[@id="password"]')).send_keys('123456')
find_ele((By.XPATH,'//*[@id="verify_code"]')).send_keys('8888')
find_ele((By.XPATH,'//*[@id="loginform"]/div/div[6]/a')).click()
time.sleep(2)
driver.get('http://localhost:8089/Home/Goods/goodsInfo/id/65.html')

ele =find_ele((By.XPATH,'//*[@id="number"]'))
js = "arguments[0].value=''"
driver.execute_script(js,ele)


# find_ele((By.XPATH,'//*[@id="join_cart"]')).click()
time.sleep(2)
# driver.switch_to.frame(0)
# print(find_ele((By.XPATH, '//*[@id="addCartBox"]/div[1]/div/span')).text)
# find_ele((By.XPATH,'//*[@id="addCartBox"]/div[1]/div/div/a[1]')).click()
# time.sleep(2)
# driver.switch_to.default_content()
#
# time.sleep(2)
find_ele((By.XPATH,'//*[@id="number"]')).send_keys('2')
# driver.quit()

