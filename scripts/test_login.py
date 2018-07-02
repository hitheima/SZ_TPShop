import pytest
from selenium.webdriver.common.by import By

from base import init_driver
from page import Page
from base import analyze_data


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

    def test_show_password(self):
        password = "xxxx"

        # 主页点击我的
        self.page.home.click_mine()
        # 我的点击登录
        self.page.mine.click_login_signup()
        # 输入密码
        self.page.login.input_password(password)
        # 点击显示密码
        self.page.login.click_show_password()

        try:
            self.page.login.find_element((By.XPATH, "text," + password))
            assert True
        except Exception:
            assert False




