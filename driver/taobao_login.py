#!/usr/lib/python2.7
#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# from selenium.webdriver.common.action_chains import ActionChains
import time


# browser = webdriver.Firefox()
# from selenium.webdriver import ActionChains
from selenium.webdriver import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-data-dir=/tmp/.com.google.Chrome.ZIBBZ7')

# chrome_options.add_argument('--user-agent=ipone')
# chrome_options.
browser = webdriver.Chrome('/home/chris/Documents/chromedriver',chrome_options=chrome_options)
# browser = webdriver.Chrome()
browser.get('https://login.taobao.com/member/login.jhtml')

# browser.maximize_window()

ele_input_name = browser.find_element_by_id('TPL_username_1')
ele_input_name.click()

browser.execute_script('document.getElementById("TPL_username_1").focus()')
# ele_input_name.send_keys('tb1045021')

ele_input_pwd = browser.find_element_by_id('TPL_password_1')
ele_input_pwd.click()
browser.execute_script('document.getElementById("TPL_password_1").focus()')
# ele_input_pwd.send_keys('xiaoxiaoyuValar')


time.sleep(5)

ele_move_ele = browser.find_element_by_id('_n1z')

print ele_move_ele

# if ele_move_ele is not None:
    # browser.find_element_by_id('J_SubmitStatic').click()

    # try:
    #
    #     # browser.find_element_by_class_name('nc-lang-cnt')
    #     action = ActionChains(browser)
    #     for count in range(1, 15):
    #         action.click_and_hold(ele_move_ele).move_to_element_with_offset(ele_move_ele, 200 + count * 5, 10).perform()
    #
    #     action.click_and_hold(ele_move_ele).move_to_element_with_offset(ele_move_ele, 301, 10).release().perform()
    #
    # except Exception as e:
    #     print '无滑块'

# browser.find_element_by_id('J_SubmitStatic').click()