from selenium.webdriver.common.by import By

from base import BaseAction


class LoginPage(BaseAction):

    username_edit_text = By.XPATH, "text,请输入手机号码"
    password_edit_text = By.ID, "com.tpshop.malls:id/edit_password"
    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    def input_username(self, text):
        self.input(self.username_edit_text, text)

    def input_password(self, text):
        self.input(self.password_edit_text, text)

    def click_login(self):
        self.click(self.login_button)