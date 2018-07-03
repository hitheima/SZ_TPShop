import random

import pytest
from selenium.webdriver.common.by import By

from base import init_driver
from page import Page
from base import analyze_data


def random_password():
    """
    随机生成一个8位的数字的字符串
    :return:
    """
    password = ""
    for i in range(8):
        password += str(random.randint(0, 9))
    return password


def show_password_data():
    data_list = list()
    data_list.append(random_password())
    data_list.append(random_password())
    data_list.append(random_password())
    return data_list


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    # @pytest.mark.parametrize("args", analyze_data("test_login"))
    # def test_login(self, args):
    #     username = args["username"]
    #     password = args["password"]
    #     expect = args["expect"]
    #
    #     # 主页点击我的
    #     self.page.home.click_mine()
    #     # 我的点击登录
    #     self.page.mine.click_login_signup()
    #     # 登录页面输入用户名
    #     self.page.login.input_username(username)
    #     # 登录页面输入密码
    #     self.page.login.input_password(password)
    #     # 登录页面点击登录
    #     self.page.login.click_login()
    #     # 判断toast是否和数据中的expect一致
    #     assert self.page.login.is_toast_exist(expect)

    # @pytest.mark.parametrize("args", analyze_data("test_login_miss_part"))
    # def test_login_miss_part(self, args):
    #     username = args["username"]
    #     password = args["password"]
    #
    #     # 主页点击我的
    #     self.page.home.click_mine()
    #     # 我的点击登录
    #     self.page.mine.click_login_signup()
    #
    #     if not username == "":
    #         self.page.login.input_username(username)
    #     if not password == "":
    #         self.page.login.input_password(password)
    #     assert not self.page.login.is_login_button_enabled()

    # @pytest.mark.parametrize("password", show_password_data())
    # def test_show_password(self, password):
    #     password_feature = By.XPATH, "text," + password
    #
    #     # 主页点击我的
    #     self.page.home.click_mine()
    #     # 我的点击登录
    #     self.page.mine.click_login_signup()
    #     # 输入密码
    #     self.page.login.input_password(password)
    #
    #     if self.page.login.is_feature_exist(password_feature):
    #         assert False
    #     else:
    #         # 点击显示密码
    #         self.page.login.click_show_password()
    #         # 判断当初输入的密码是否存在
    #         assert self.page.login.is_feature_exist(password_feature)

