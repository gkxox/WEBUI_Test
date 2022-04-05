from selenium.webdriver.common.by import By

from Base.base import BasePage


# 管理员登录页-对象库存
class AdminLoginPage(BasePage):

    def __init__(self,broswer):
        super().__init__(broswer)
        # 管理员登录页面url
        self.admin_login_url = 'http://localhost:8089/Admin/Admin/login'
        # 用户名
        self.username = By.XPATH, "//*[@name='username']"
        # 密码
        self.password = By.XPATH, "//*[@name='password']"
        # 验证码
        self.verify_code = By.XPATH, "//*[@name='vertify']"
        # 登录按钮
        self.login_btn = By.XPATH, "//*[@name='submit']"

    def find_username(self):
        return self.find_element(self.username)

    def find_password(self):
        return self.find_element(self.password)

    def find_verify_code(self):
        return self.find_element(self.verify_code)

    def find_login_btn(self):
        return self.find_element(self.login_btn)

    # 打开管理员登陆页面
    def admin_login_page(self):
        self.driver.get(self.admin_login_url)


class AdminLoginHandle(BasePage):

    def __init__(self,broswer):
        super().__init__(broswer)
        self.admin_login_handle = AdminLoginPage(broswer)

    def input_username(self, username):
        self.input_text(self.admin_login_handle.find_username(), username)

    def input_password(self, password):
        self.input_text(self.admin_login_handle.find_password(), password)

    def inout_verify_code(self, verify_code):
        self.input_text(self.admin_login_handle.find_verify_code(), verify_code)

    def click_login_btn(self):
        self.admin_login_handle.find_login_btn().click()

    def login_admin_page(self):
        self.admin_login_handle.admin_login_page()


class AdminLoginProxy:

    def __init__(self,broswer):
        self.admin_login_proxy = AdminLoginHandle(broswer)

    def login_admin(self, username='admin', password='123456', verify_code='8888'):
        self.admin_login_proxy.login_admin_page()
        self.admin_login_proxy.input_username(username)
        self.admin_login_proxy.input_password(password)
        self.admin_login_proxy.inout_verify_code(verify_code)
        self.admin_login_proxy.click_login_btn()


if __name__ == '__main__':
    AdminLoginProxy().login_admin()
