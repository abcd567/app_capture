# _*_ coding: utf-8 _*_
__author__ = "吴飞鸿"
__date__ = "2019/7/22 0:16"


import time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

cap = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.ss.android.ugc.aweme",
    "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
    # .main.MainActivity
    "noReset": True,
    "unicodekeyboard": True,
    "resetkeyboard": True
}
# appium连接手机
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=cap)


def get_size(driver):
    """获取driver窗口大小"""
    size = driver.get_window_size()
    return size['width'], size['height']

# 操作应用
try:
    # 未成年人提醒
    if WebDriverWait(driver, 60).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.ss.android.ugc.aweme:id/dgc']")):
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.ss.android.ugc.aweme:id/dgc']").click()
except:
    pass

try:
    # 搜索框
    if WebDriverWait(driver, 60).until(lambda x: x.find_element_by_xpath('//android.widget.Button[@content-desc="搜索"]')):
        driver.find_element_by_xpath('//android.widget.Button[@content-desc="搜索"]').click()
except:
    pass

try:
    # 输入抖音id
    if WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/\
    android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/\
    android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.View')):

        # driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/\
        # android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/\
        # android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.View').click()

        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/\
        android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/\
        android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.View').send_keys("youdi")
except:
    pass

try:
    # 点击搜索
    if WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/\
    android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/\
    android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView')):
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/\
        android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/\
        android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView').click()
except:
    pass


try:
    # 点击用户
    if WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/\
    android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/\
    android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/\
    android.support.v7.app.ActionBar.Tab[3]')):
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/\
        android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/\
        android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/\
        android.support.v7.app.ActionBar.Tab[3]').click()
except:
    pass

try:
    # 点击第一个搜索结果
    if WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/\
    android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/\
    android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/\
    android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/\
    android.widget.RelativeLayout/android.widget.LinearLayout')):
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/\
        android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/\
        android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/\
        android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/\
        android.widget.LinearLayout').click()
except:
    pass

try:
    # 点击粉丝列表
    if WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/\
    com.bytedance.ies.dmt.ui.sliding.DmtSlidingPaneLayout/android.widget.LinearLayout/android.widget.FrameLayout/\
    android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/\
    android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/\
    android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/\
    android.widget.LinearLayout[4]/android.widget.LinearLayout[3]/android.widget.TextView[1]')):
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/com.bytedance.ies.dmt.ui.sliding.DmtSlidingPaneLayout/\
        android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/\
        android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/\
        android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/\
        android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.LinearLayout[3]/\
        android.widget.TextView[1]').click()
except:
    pass


# 滑动粉丝列表
if WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/\
android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/\
android.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/\
android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]')):
    x, y = get_size(driver)
    x1 = int(x*0.48)
    y1 = int(y*0.90)
    y2 = int(y*0.15)
    while True:
        if '没有更多了' in driver.page_source:
            break
        time.sleep(3)
        driver.swipe(x1, y1, x1, y2)

