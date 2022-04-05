import time

import allure
from selenium.webdriver.common.by import By

import config
from Base.base import BasePage

class HomePage(BasePage):
    def __init__(self,broswer):
        super(HomePage, self).__init__(broswer)
        # home主页
        self.home_url = config.read_config("URL", 'Home')
        # 家用电器元素组
        self.appliance_items = (By.XPATH, "//div[4]/div[2]/div[@class='floor-goods-list']/a")
        # 我的购物车
        self.my_cart = By.XPATH, "//span[text()='我的购物车']"
        # 我的订单
        self.my_order = (By.XPATH, "//a[text()='我的订单']")

    def find_appliance_items(self):
        return self.find_elements(self.appliance_items)

    def find_my_cart(self):
        return self.find_element(self.my_cart)

    def find_my_order(self):
        return self.find_element(self.my_order)

    def home_page(self):
        # self.driver.execute_script(f'window.open("{self.home_url}")')
        self.driver.get('http://localhost:8089/Home/Index/index.html')
        # time.sleep(2)
        # self.driver.switch_to.window(self.driver.window_handles[-1])


class HomeHandle(BasePage):
    def __init__(self,broswer):
        super().__init__(broswer)
        self.home_handle = HomePage(broswer)

    @allure.step("跳转至主页")
    def login_home_page(self):
        self.home_handle.home_page()

    @allure.step("点击我的购物车")
    def click_my_cart(self):
        self.home_handle.find_my_cart().click()

    @allure.step("点击我的订单")
    def click_my_order(self):
        self.home_handle.find_my_order().click()

    @allure.step("选择商品")
    def select_appliance_items(self, index):
        self.home_handle.find_appliance_items()[index].click()


class HomeProxy:

    def __init__(self,broswer):
        self.home_proxy = HomeHandle(broswer)

    def select_goods(self, index):
        self.home_proxy.login_home_page()
        # self.home_proxy.click_my_order()
        self.home_proxy.select_appliance_items(index)


if __name__ == '__main__':
    HomeProxy(broswer='chrome').select_goods(0)
