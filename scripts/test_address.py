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

        # 点击收货地址

