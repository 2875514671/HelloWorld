# coding=utf-8
import time
from appium import webdriver
# webdriver的是一个Web应用程序测试自动化工具，用来验证程序是否如预期的那样执行。它不依赖于任何特定的测试框架，所以它可以用于单元测试或者一个老式的“main”方法中
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'Android Emulator'  # 通过adb devices -l查看设备标识
desired_caps['appPackage'] = 'com.android.calculator2'   # app的包名
desired_caps['appActivity'] = '.Calculator'   # 启动时的Activity

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 连接设备并打开应用

driver.find_element_by_name("1").click()  # 点击所定位的元素  element 元素

driver.find_element_by_name("5").click()

driver.find_element_by_name("+").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("×").click()

driver.find_element_by_name("7").click()

driver.find_element_by_name("÷").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("2").click()

driver.find_element_by_name("−").click()

driver.find_element_by_name("4").click()

driver.find_element_by_name("3").click()

driver.find_element_by_name("+").click()

driver.find_element_by_name("6").click()

driver.find_element_by_name("8").click()

driver.find_element_by_name("=").click()

time.sleep(1)
driver.quit()