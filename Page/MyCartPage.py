from selenium.webdriver.common.by import By

from Base.base import BasePage
import allure


class MyCartPage(BasePage):

    def __init__(self):
        super().__init__()

        # 我的购物车_url
        self.my_cart_url = 'http://localhost:8089/Home/Cart/index.html'
        # 去结算
        self.checkout_btn = By.XPATH, "//a[contains(text(),'去结算')]"
        # 继续购物
        self.continue_shopping_btn = By.XPATH, "//a[contains(text(),'继续购物')]"
        # 商品勾选框
        self.goods_checkbox = By.XPATH, "//input[@name='checkItem']"
        # 全选
        self.check_cart_all = By.XPATH, ".//*[@class='checkCart checkCartAll']"
        # 删除商品
        self.remove_goods = By.XPATH, "//*[@id='removeGoods']"
        # 商品数量
        self.change_quantity = By.XPATH, "//*[contains(@id,'changeQuantity')]"
        # 商品详情链接
        self.goods_deatails_link = By.XPATH, "//*[contains(@id,'edge')]/td[3]/p[1]/a"

    def find_my_cart_url(self):
        self.driver.get(self.my_cart_url)

    def find_checkout_btn(self):
        return self.find_element(self.checkout_btn)

    def find_continue_shopping_btn(self):
        return self.find_element(self.continue_shopping_btn)

    def find_goods_checkbox(self):
        return self.find_elements(self.goods_checkbox)

    def find_check_cart_all(self):
        return self.find_element(self.check_cart_all)

    def find_remove_goods(self):
        return self.find_element(self.remove_goods)

    def find_change_quantity(self):
        return self.find_elements(self.change_quantity)

    def find_goods_deatails_link(self):
        return self.find_elements(self.goods_deatails_link)


class MyCartHandle(BasePage):

    def __init__(self):
        super().__init__()
        self.my_cart_handle = MyCartPage()

    @allure.step("跳转至我的购物车")
    def skip_to_my_cart_url(self):
        self.my_cart_handle.find_my_cart_url()

    @allure.step('点击去结算')
    def click_checkout_btn(self):
        self.my_cart_handle.find_checkout_btn().click()

    @allure.step('点击继续购物')
    def click_continue_shopping_btn(self):
        self.my_cart_handle.find_continue_shopping_btn().click()

    @allure.step('选择商品')
    def click_goods_checkbox(self, checkbox_index):
        self.my_cart_handle.find_goods_checkbox()[checkbox_index].click()

    @allure.step('全选/取消全选')
    def click_check_cart_all(self):
        self.my_cart_handle.find_check_cart_all().click()

    @allure.step('删除选中的商品')
    def click_remove_goods(self):
        self.my_cart_handle.find_remove_goods().click()

    @allure.step('修改商品数量')
    def input_change_quantity(self, index, num):
        self.input_text(self.my_cart_handle.find_change_quantity()[index], num)

    @allure.step('跳转至商品详情')
    def click_goods_deatails_link(self, goods_index):
        self.my_cart_handle.find_goods_deatails_link()[goods_index].click()


class MyCartProxy:
    def __init__(self):
        self.my_cart_proxy = MyCartHandle()

    def checkout_goods(self, checkbox_index, index, num):
        self.my_cart_proxy.click_check_cart_all()
        self.my_cart_proxy.click_goods_checkbox(checkbox_index)
        self.my_cart_proxy.input_change_quantity(index, num)
        self.my_cart_proxy.click_checkout_btn()
