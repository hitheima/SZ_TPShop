import allure
from selenium.webdriver.common.by import By

from base import BaseAction


class MinePage(BaseAction):
    login_signup_button = By.XPATH, "text,登录/注册"
    # 齿轮按钮
    setting_button = By.ID, "com.tpshop.malls:id/setting_btn"

    # 设置/登录的标题
    title_feature = By.ID, "com.tpshop.malls:id/titlebar_title_txtv"

    @allure.step(title="我的页面点击登录/注册按钮")
    def click_login_signup(self):
        self.click(self.login_signup_button)

    def click_setting(self):
        self.click(self.setting_button)

    def is_login(self):
        self.click_setting()

        is_login = self.find_element(self.title_feature).text == "设置"

        # 按返回键 回到原来的界面
        self.press_key_code(4)

        return is_login

        # if self.find_element(self.title_feature).text == "设置":
        #     return True
        # else:
        #     return False
        #
        # if self.find_element(self.title_feature).text == "登录":
        #
        #     return False
        # else:
        #     return True



