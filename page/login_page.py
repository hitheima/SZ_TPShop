import allure
from selenium.webdriver.common.by import By

from base import BaseAction


class LoginPage(BaseAction):

    username_edit_text = By.XPATH, "text,请输入手机号码"
    password_edit_text = By.ID, "com.tpshop.malls:id/edit_password"
    login_button = By.ID, "com.tpshop.malls:id/btn_login"

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