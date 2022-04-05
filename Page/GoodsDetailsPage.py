import logging
import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Base.base import BasePage,UtilsDriver



class GoodsDetailsPage(BasePage):
    def __init__(self,broswer):
        super().__init__(broswer)

        self.goods_size = By.XPATH, "//span[text()='尺寸：']/../../li[2]/a"
        self.dispatching = By.XPATH, "//*[@id='dispatching_select']"
        self.goods_num = By.XPATH, '//*[@id="number"]'
        self.buy_now = By.XPATH, "//a[1][contains(text(),'立即购买')]"
        self.add_cart = By.XPATH, "//a[2][contains(text(),'加入购物车')]"
        self.my_cart = By.XPATH, "//span[contains(text(),'我的购物车')]"
        self.tips_page = By.XPATH, "//*[@id='layui-layer-iframe1']"
        self.tips_continue_shopping = By.XPATH, "//a[contains(text(),'继续购物')]"
        self.tips_close = By.XPATH, "//*[@class='layui-layer-setwin']/a"
        self.add_success_text =By.XPATH,'//*[@id="addCartBox"]/div[1]/div/span'

    def find_area(self, area):
        try:
            wait = WebDriverWait(self.driver, 10, 1)
            element = wait.until(
                lambda x: x.find_element(By.XPATH, f"//ul[@class='area-list']/li/a[contains(text(),'{area}')]"))
            return element
        except Exception as e:
            raise e

    def find_tips_page(self):
        self.driver.switch_to.frame(0)

    def find_default_content(self):
        self.driver.switch_to.default_content()

    def find_goods_size(self):
        # logging.info(f"定位商品尺寸，定位元素{self.goods_size}")
        return self.find_elements(self.goods_size)

    def find_dispatching(self):
        dispatching_options = Select(self.find_element(self.dispatching))
        return dispatching_options

    def find_googs_num(self):
        return self.find_element(self.goods_num)

    def find_buy_now(self):
        return self.find_element(self.buy_now)

    def find_add_cart(self):
        return self.find_element(self.add_cart)

    def find_my_cart(self):
        return self.find_element(self.my_cart)

    def find_tips_continue_shopping(self):
        return self.find_element(self.tips_continue_shopping)

    def find_tips_close(self):
        return self.find_element(self.tips_close)

    def find_add_success_text(self):
        return self.find_element(self.add_success_text)


class GoodsDetailsHandle(BasePage):
    def __init__(self,broswer):
        super().__init__(broswer)
        self.goods_details_handle = GoodsDetailsPage(broswer)

    @allure.step("选择配送地址")
    def select_area(self, area):
        self.goods_details_handle.find_area(area).click()

    @allure.step("选择尺寸")
    def select_goods_size(self, index):
        self.goods_details_handle.find_goods_size()[index].click()

    @allure.step("选择物流")
    def select_dispatching(self, option):
        self.goods_details_handle.find_dispatching().select_by_index(option)
        '''[0]:申通物流,[1]:顺丰物流,[2]:中通快递'''

    @allure.step("输入商品数量")
    def input_goods_num(self, num):
        self.input_text(self.goods_details_handle.find_googs_num(), num)

    @allure.step("点击立即购买")
    def click_by_now(self):
        self.goods_details_handle.find_buy_now().clixk()

    @allure.step("点击添加购物车")
    def click_add_cart(self):
        self.goods_details_handle.find_add_cart().click()

    @allure.step("点击我的购物车")
    def click_my_cart(self):
        self.goods_details_handle.find_my_cart().click()
        allure.attach(UtilsDriver.get_driver().get_screenshot_as_png(), "我的购物车", allure.attachment_type.PNG)

    @allure.step("切换到温馨提示")
    def switch_to_tips(self):
        self.goods_details_handle.find_tips_page()

    @allure.step("切回商品详情主页面")
    def switch_to_default_page(self):
        self.goods_details_handle.find_default_content()

    @allure.step("点击继续购物")
    def click_tips_continue_shopping(self):
        self.goods_details_handle.find_tips_continue_shopping().click()

    @allure.step("关闭温馨提示")
    def click_tips_close(self):
        self.goods_details_handle.find_tips_close().click()

    @allure.step("获取添加成功信息")
    def assert_add_success_text(self):
        return self.goods_details_handle.find_add_success_text().text


class GoodsDetailsProxy:

    add_success_text = None

    def __init__(self,broswer):
        self.goods_details_proxy = GoodsDetailsHandle(broswer)

    def assert_add_success(self):
        self.add_success_text = self.goods_details_proxy.assert_add_success_text()
        return self.add_success_text

    def add_goods(self, option, index, province="江苏省", city="南京市", area="浦口区"):
        '''

        :param option: [0]:申通物流,[1]:顺丰物流,[2]:中通快递
        :param index: 商品尺寸
        :param num: 商品数量
        :param province: 省
        :param city: 市
        :param area: 区
        :return:
        '''
        # 选择配送省份
        # self.goods_details_proxy.select_area(province)
        # 选择配送市
        # self.goods_details_proxy.select_area(city)
        # 选择配送区
        # self.goods_details_proxy.select_area(area)
        # 选择快递
        self.goods_details_proxy.select_dispatching(option)
        # 选择尺寸
        self.goods_details_proxy.select_goods_size(index)
        # 输入购买数量
        # self.goods_details_proxy.input_goods_num(num)
        # 点击加入购物车
        self.goods_details_proxy.click_add_cart()
        time.sleep(2)
        self.goods_details_proxy.switch_to_tips()
        self.assert_add_success()
        # print(self.add_success_text)
        self.goods_details_proxy.click_tips_continue_shopping()
        time.sleep(2)
        self.goods_details_proxy.switch_to_default_page()
        # 点击我的购物车
        self.goods_details_proxy.click_my_cart()



if __name__ == "__main__":
    GoodsDetailsProxy(broswer='chrome').add_goods(2, 0)
