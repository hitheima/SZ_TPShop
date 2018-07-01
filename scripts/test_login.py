from base import init_driver
from page import Page

class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_login1(self):
        print("hehe")

        # 主页点击我的
        self.page.home.click_mine()
        # 我的点击登录
        self.page.mine.click_login_signup()
        # 登录页面输入用户名
        # self.page.login.xxxxx
        # 登录页面输入密码
        # 登录页面点击登录

        assert 1
