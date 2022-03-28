from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r'C:\Users\gkxox\Desktop\TPShop_UI\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://localhost:8089/Home/Index/index.html')
ele = driver.find_elements(By.XPATH, "//div[4]/div[2]/div[@class='floor-goods-list']/a")
ele[0].click()