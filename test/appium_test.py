# _*_ coding: utf-8 _*_
__author__ = "吴飞鸿"
__date__ = "2019/7/19 16:42"

# 考研帮app登陆、滑动
import time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

cap = {
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.tal.kaoyan",
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
  "noReset": True
}

# 连接 appium 服务器，并打开应用
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=cap)


def get_size(driver):
    """获取driver窗口大小"""
    size = driver.get_window_size()
    return size['width'], size['height']

# 操作应用
try:
    # 第一次打开，出现app简介，点击跳过
    if WebDriverWait(driver, 3).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_skip']")):
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_skip']").click()
except:
    pass


try:
    # 第一次登陆，要求登陆界面填写账号密码
    if WebDriverWait(driver, 3).until(lambda x: x.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']")):
        driver.find_element_by_xpath(
          "//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']").send_keys("q915263031")
        time.sleep(0.5)
        driver.find_element_by_xpath(
          "//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_password_edittext']").send_keys("qq915263031")
        time.sleep(0.7)
        driver.find_element_by_xpath(
          "//android.widget.Button[@resource-id='com.tal.kaoyan:id/login_login_btn']").click()
except:
    pass

# 进入“研讯”
driver.find_element_by_xpath(
    "//android.view.ViewGroup[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.RelativeLayout[3]/\
    android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()
if WebDriverWait(driver, 3).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/myapptitle_Title']")):
    x, y = get_size(driver)
    x1 = int(x*0.48)
    y1 = int(y*0.76)
    y2 = int(y*0.23)
    for i in range(100):
        time.sleep(1)
        driver.swipe(x1, y1, x1, y2)



