from base import init_driver
from page import Page

class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_login(self):
        # 主页点击我的
        self.page.home.click_mine()
        # 我的点击登录
        self.page.mine.click_login_signup()
        # 登录页面输入用户名
        self.page.login.input_username("18503080305")
        # 登录页面输入密码
        self.page.login.input_password("123000")
        # 登录页面点击登录
        self.page.login.click_login()

        assert self.page.login.is_toast_exist("登录成功")


