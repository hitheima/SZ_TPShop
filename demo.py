from appium import webdriver

# server 启动参数
desired_caps = dict()
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app的信息
desired_caps['appPackage'] = 'com.tpshop.malls'
desired_caps['appActivity'] = '.SPMainActivity'
# 解决输入中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# toast
desired_caps['automationName'] = 'Uiautomator2'

# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# print(driver.capabilities)
# print("----")
# print(driver.capabilities.keys())
# print("----")
# print(driver.capabilities.values())


if driver.capabilities["automationName"] == "Uiautomator2":
    print("111")
else:
    print("222")

if "1" in ["1", "2", "3"]:
    print("111")
else:
    print("222")






