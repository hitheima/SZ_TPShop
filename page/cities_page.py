import random

import allure
import time
from selenium.webdriver.common.by import By

from base import BaseAction

class CitiesPage(BaseAction):

    # 城市特征
    city_feature = By.ID, "com.tpshop.malls:id/tv_city"

    # 确定
    commit_button = By.XPATH, "text,确定"

    # 省份特征
    province_button = By.ID, "com.tpshop.malls:id/rb_province"

    # def click_jilin(self):
    #     # 6 1 0 0

    def click_random_cities(self):
        time.sleep(1)
        for i in range(4):
            cities_elements = self.find_elements(self.city_feature)
            random.sample(cities_elements, 1)[0].click()
            time.sleep(1)

    def click_commit(self):
        self.click(self.commit_button)
        # if self.is_toast_exist("地址信息不完整"):
        #     self.click(self.province_button)
        #     self.click_random_cities()
