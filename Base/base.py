from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utils import UtilsDriver


# 对象库层基类
class BasePage:

    def __init__(self):
        self.driver = UtilsDriver.get_driver()

    # 定位元素
    def find_element(self, locator):
        try:
            wait = WebDriverWait(driver=self.driver, timeout=10, poll_frequency=0.5)
            element = wait.until(lambda x: x.find_element(*locator))
            return element
        except Exception as e:
            raise e

    # 定位一组元素
    def find_elements(self, locator):
        try:
            wait = WebDriverWait(driver=self.driver, timeout=10, poll_frequency=0.5)
            elements = wait.until(lambda x: x.find_elements(*locator))
            return elements
        except Exception as e:
            raise e

    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)



# 操作层基类
# class BaseHandle:
#
#     def input_text(self, element, text):
#         element.clear()
#         element.send_keys(text)

