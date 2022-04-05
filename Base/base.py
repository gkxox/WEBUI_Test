from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class UtilsDriver:
    _driver = None

    __quit_driver = True  # 系统退出驱动的标识

    # 定义修改私有属性的方法
    @classmethod
    def set_quit_driver(cls, mark):
        cls.__quit_driver = mark

    @classmethod
    def get_driver(cls,broswer='chrome'):
        if not cls._driver:
            if broswer.lower() == 'chrome':
                chrome_options = webdriver.ChromeOptions()
                # chrome_options.add_argument('--headless')
                # chrome_options.add_argument("--window-size=1920x1080")
                cls._driver = webdriver.Chrome(options=chrome_options)
                cls._driver.implicitly_wait(5)
                cls._driver.maximize_window()
            elif broswer.lower() == 'firefox':
                options = webdriver.FirefoxOptions()
                # options.headless = True
                cls._driver = webdriver.Firefox(firefox_options=options)
                cls._driver.implicitly_wait(5)
                cls._driver.maximize_window()
            else:
                print("输入正确的浏览器")

        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver and cls.__quit_driver:
            cls.get_driver().quit()
            cls._driver = None



# 对象库层基类
class BasePage:

    def __init__(self,broswer):
        self.driver = UtilsDriver.get_driver(broswer)

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

