import logging

import allure
from selenium.webdriver.common.by import By

import config
from Base.base import BasePage


# 主页登录-对象库层
class HomeLoginPage(BasePage):

    def __init__(self):
        super(HomeLoginPage, self).__init__()
        # home登录页面
        self.home_login_url = config.read_config("URL", 'Home_Login')
        # 用户名
        self.username = By.XPATH, "//*[@id='username']"
        # 密码
        self.password = By.XPATH, "//*[@id='password']"
        # 验证码
        self.verify_code = By.XPATH, "//*[@id='verify_code']"
        # 登录按钮
        self.login_btn = By.XPATH, "//*[@name='sbtbutton']"

        self.home_btn = By.XPATH, "/html/body/div[2]/div/div[3]/ul/li[1]/a"

    def find_home_btn(self):
        return self.find_element(self.home_btn)

    # 定位用户名元素
    def find_username(self):
        return self.find_element(self.username)

    # 定位密码元素
    def find_password(self):
        return self.find_element(self.password)

    # 定位验证码元素
    def find_verify_code(self):
        return self.find_element(self.verify_code)

    # 定位登录按钮元素
    def find_login_btn(self):
        return self.find_element(self.login_btn)

    # 打开home登录页面 home_login_page(self):
    def home_login_page(self):
        self.driver.get(self.home_login_url)


# 主页登录-操作层
class HomePageHandle(BasePage):

    def __init__(self):
        super().__init__()
        self.home_login_handle = HomeLoginPage()

    # 打开home登录页面
    @allure.step("打开home登录页面")
    def login_home_page(self):
        self.home_login_handle.home_login_page()

    # 输入用户名
    @allure.step("输入用户名")
    def input_username(self, text):
        self.input_text(self.home_login_handle.find_username(), text)

    # 输入密码
    @allure.step("输入密码")
    def input_password(self, text):
        self.input_text(self.home_login_handle.find_password(), text)

    # 输入验证码
    @allure.step("输入验证码")
    def input_verify_code(self, text):
        self.input_text(self.home_login_handle.find_verify_code(), text)

    # 点击登录按钮
    @allure.step("点击登录按钮")
    def click_lohin_btn(self):
        self.home_login_handle.find_login_btn().click()

    @allure.step("点击主页")
    def click_home_btn(self):
        self.home_login_handle.find_home_btn().click()


# 主页登录-业务层
class HomeLoginProxy:

    def __init__(self):
        self.home_login_proxy = HomePageHandle()

    # 用户登录
    def login_home(self, username='13488888888', password='123456', verify_code='8888'):
        self.home_login_proxy.login_home_page()
        self.home_login_proxy.input_username(username)
        self.home_login_proxy.input_password(password)
        self.home_login_proxy.input_verify_code(verify_code)
        self.home_login_proxy.click_lohin_btn()
        # self.home_login_proxy.click_home_btn()


if __name__ == "__main__":
    HomeLoginProxy().login_home()
