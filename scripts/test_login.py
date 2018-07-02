import pytest

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

    @pytest.mark.parametrize("args", analyze_data("test_login_miss_part"))
    def test_login_miss_part(self, args):
        username = args["username"]
        password = args["password"]

        # 主页点击我的
        self.page.home.click_mine()
        # 我的点击登录
        self.page.mine.click_login_signup()

        if not username == "":
            self.page.login.input_username(username)
        if not password == "":
            self.page.login.input_password(password)

        # if  真    结果真
        # if  假    结果假

        assert not self.page.login.is_login_button_enabled()

        # if self.page.login.is_login_button_enabled():
        #     assert False
        # else:
        #     assert True

        # assert not self.page.login.is_login_button_enabled()

        # if username != "":
        #     self.page.login.input_username(username)
        # if password != "":
        #     self.page.login.input_password(password)

        # if password == "":
        #     self.page.login.input_username(username)
        # if username == "":
        #     self.page.login.input_password(password)


    # def test_login_miss_username(self):
    #     # 主页点击我的
    #     self.page.home.click_mine()
    #     # 我的点击登录
    #     self.page.mine.click_login_signup()
    #
    #     self.page.login.input_username("18503080305")
    #
    #     # 判断登录按钮是否可用
    #
    # def test_login_miss_password(self):
    #     # 主页点击我的
    #     self.page.home.click_mine()
    #     # 我的点击登录
    #     self.page.mine.click_login_signup()
    #
    #     self.page.login.input_password("18503080305")
    #
    #     # 判断登录按钮是否可用







