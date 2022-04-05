import os
import time

import allure
import pytest
import logging

import config
from Base.base import UtilsDriver
from Page import HomePage,HomeLoginPage,GoodsDetailsPage,MyCartPage

@pytest.mark.run(order=1001)
class TestOrder:

    def setup_class(self):
        self.broswer = 'firefox'
        self.home_login_proxy = HomeLoginPage.HomeLoginProxy(self.broswer)
        self.home_proxy = HomePage.HomeProxy(self.broswer)
        self.goods_details_proxy = GoodsDetailsPage.GoodsDetailsProxy(self.broswer)
        self.my_cart_page_proxy = MyCartPage.MyCartProxy(self.broswer)
        self.driver = UtilsDriver.get_driver(self.broswer)


    def teardown_class(self):
        UtilsDriver.quit_driver()

    @allure.title("前台下单")
    @allure.description("购买流程测试：登录==》挑选商品==》加入购物车==》支付方式（货到付款）==》生成订单")
    def test_01(self):

        time.sleep(2)
        self.home_login_proxy.login_home()
        time.sleep(2)
        self.home_proxy.select_goods(2)
        self.goods_details_proxy.add_goods(option=1, index=1)
        if self.goods_details_proxy.add_success_text:
            assert '添加成功' in self.goods_details_proxy.add_success_text
            logging.info('商品添加成功')
            self.driver.get_screenshot_as_file(config.base_dir() + '/Screenshot/商品添加成功.png')
        else:
            logging.error('商品添加失败')
            self.driver.get_screenshot_as_file(config.base_dir() + '/Screenshot/商品添加失败.png')

        # time.sleep(2)
        # self.my_cart_page_proxy.checkout_goods(1,0,2)
        # time.sleep(2)
        # self.driver.get_screenshot_as_file(config.base_dir() + '/Screenshot/结算商品.png')
