import random

import pytest
from selenium.webdriver.common.by import By

from base import init_driver
from page import Page
from base import analyze_data


class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_address(self):
        self.page.home.click_mine()
        # 判断登录状态
        if not self.page.mine.is_login():  # 如果没有登录
            # 进入登录界面
            self.page.mine.click_login_signup()
            # 登录
            self.page.login.login()

        if not self.page.mine.is_feture_exist_scroll_page(self.page.mine.address_feature):
            assert False

        # 点击收货地址
        self.page.mine.click_address()
        # 新建地址
        self.page.address.click_new_address()
        # 收货人
        self.page.address_detail.input_name("hao")
        # 收货人 手机
        self.page.address_detail.input_mobile("18503080300")
        # 收货人 地区
        self.page.address_detail.click_region()
        # 输入四个地址城市
        self.page.cities.click_random_cities()
        # 点击确定
        self.page.cities.click_commit()
        # 收货人 详细地址
        self.page.address_detail.input_address("2单元 404")
        # 保存
        self.page.address_detail.click_save_address()
        # 判断是否添加成功
        assert self.page.address.is_toast_exist("添加成功")









