import allure
from selenium.webdriver.common.by import By

from base import BaseAction


class LoginPage(BaseAction):

    username_edit_text = By.XPATH, "text,请输入手机号码"
    password_edit_text = By.ID, "com.tpshop.malls:id/edit_password"
    login_button = By.ID, "com.tpshop.malls:id/btn_login"
    # 显示密码的按钮
    show_password_button = By.ID, "com.tpshop.malls:id/img_view_pwd"

    @allure.step(title="输入用户名")
    def input_username(self, text):
        allure.attach('用户名', text)
        self.input(self.username_edit_text, text)

    @allure.step(title="输入密码")
    def input_password(self, text):
        allure.attach('密码 ' + text, "")
        self.input(self.password_edit_text, text)

    @allure.step(title="点击登录")
    def click_login(self):
        self.click(self.login_button)

    def login(self):
        """
        只要调用这个函数
        就能登录
        进入登录界面之后 调用
        :return:
        """
        self.input_username("18503080305")
        self.input_password("123000")
        self.click_login()

    def is_login_button_enabled(self):
        return self.is_feature_enabled(self.login_button)

    def click_show_password(self):
        self.click(self.show_password_button)
