from selenium.webdriver.common.by import By

from base import BaseAction


class MinePage(BaseAction):

    login_signup_button = By.XPATH, "text,登录/注册"

    def click_login_signup(self):
        self.click(self.login_signup_button)