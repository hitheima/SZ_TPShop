from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def click(self, feature):
        """
        根据某个特征，进行查找并且点击
        :param feature: 特征
        :return:
        """
        self.find_element(feature).click()

    def input(self, feature, text):
        """
        根据某个特征，进行查找并且输入对应的文字
        :param feature: 特征
        :param text: 文字
        :return:
        """
        self.find_element(feature).send_keys(text)

    def find_element(self, feature, timeout=5.0, poll=1.0):
        """
        根据特征，找元素
        :param feature: 特征
        :return: 元素
        """
        by = feature[0]
        value = feature[1]
        if by == By.XPATH:
            value = self.__make_xpath_with_feature(value)
            print(value)
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_element(by, value))

    def find_elements(self, feature, timeout=5.0, poll=1.0):
        """
        根据特征，找元素
        :param feature: 特征
        :return: 元素
        """
        by = feature[0]
        value = feature[1]
        if by == By.XPATH:
            value = self.__make_xpath_with_feature(value)
            print(value)
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_elements(by, value))

    @staticmethod
    def __make_xpath_with_unit_feature(xpath_value):
        """
        拼接xpath中间的部分
        :param loc:
        :return:
        """
        key_index = 0
        value_index = 1
        option_index = 2

        res_value = ""
        args = xpath_value.split(",")
        if len(args) == 3:
            if args[option_index] == "1":
                res_value += "@%s='%s' and " % (args[key_index], args[value_index])
            elif args[option_index] == "0":
                res_value += "contains(@%s,'%s') and " % (args[key_index], args[value_index])
        elif len(args) == 2:
            res_value += "contains(@%s,'%s') and " % (args[key_index], args[value_index])

        return res_value

    def __make_xpath_with_feature(self, xpath_value):

        xpath_start = "//*["
        xpath_end = "]"
        res_value = ""

        if isinstance(xpath_value, str):

            # 系统的xpath
            if xpath_value.startswith("/"):
                return xpath_value

            res_value = self.__make_xpath_with_unit_feature(xpath_value)

        elif isinstance(xpath_value, tuple):
            for i in xpath_value:
                res_value += self.__make_xpath_with_unit_feature(i)

        res_value = res_value.rstrip(" and ")

        res_value = xpath_start + res_value + xpath_end

        return res_value

    def find_toast(self, message, timeout=3):
        """
        # message: 预期要获取的toast的部分消息
        """
        message = "//*[contains(@text,'" + message + "')]"  # 使用包含的方式定位

        return self.find_element((By.XPATH, message), timeout=timeout, poll=0.1).text

    def is_toast_exist(self, message):
        """
        判断toast的部分消息是否存在
        :param message:
        :return:
        """
        try:
            self.find_toast(message)
            return True
        except Exception:
            return False

    def is_feature_enabled(self, feature):
        if self.find_element(feature).get_attribute("enabled") == "true":
            return True
        else:
            return False

    def is_feature_exist(self, feature):
        try:
            self.find_element(feature)
            return True
        except Exception:
            return False

    def press_key_code(self, key_code):
        """
        执行keycode
        并且会根据有没有使用automationName这个key
        执行对应的发送时间方法
        :param key_code:
        :return:
        """
        if "automationName" in self.driver.capabilities.keys():
            self.driver.press_keycode(key_code)
        else:
            self.driver.keyevent(key_code)

    def scroll_page_one_time(self, dir="up"):

        # 滑动
        screen_width = self.driver.get_window_size()["width"]
        screen_height = self.driver.get_window_size()["height"]

        center_x = screen_width * 0.5
        center_y = screen_height * 0.5

        start_x, start_y, end_x, end_y = 0, 0, 0, 0

        if dir == "up" or "down":
            start_x = center_x
            start_y = screen_height * 0.75
            end_x = center_x
            end_y = screen_height * 0.25
        if dir == "left" or "right":
            start_x = screen_width * 0.75
            start_y = center_y
            end_x = screen_width * 0.25
            end_y = center_y

        if dir == "up" or "left":
            self.driver.swipe(start_x, start_y, end_x, end_y, 3000)
        elif dir == "down" or "right":
            self.driver.swipe(end_x, end_y, start_x, start_y, 3000)
        else:
            raise Exception("dir参数只能使用 up/down/left/right")

    def is_scroll_page_until_feature(self, feature, element_text, dir="up"):
        """
        滑动当前页面，直到某组feature的元素，是否有element_text的文字
        :param feature: 元素的特征
        :param element_text: 寻找的元素的文字内容
        :param dir: 方向 up:从下往上 down:从上往下 left:从右往左 right:从左往右
        :return:
        """
        old = ""
        while True:
            new = ""
            eles = self.find_elements(feature)

            for i in eles:
                text = i.text
                new += text

                if text == element_text:
                    return True

            if old == new:
                return False
            else:
                old = new

            self.scroll_page_one_time(dir)




