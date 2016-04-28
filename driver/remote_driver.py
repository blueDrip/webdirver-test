#!/usr/lib/python2.7
#coding:utf-8

import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymouse import PyMouse

service = service.Service('/home/chris/Documents/chromedriver')
service.start()
capabilities = {'chrome.binary': '/path/to/custom/chrome'}
browser = webdriver.Remote(service.service_url, capabilities)
browser.delete_all_cookies()
browser.get('https://login.taobao.com')

browser.maximize_window()

mouse = PyMouse()
print mouse.position()

# browser.find_element_by_link_text('亲，请登录').click()
#
# wait = WebDriverWait(browser, 30)
# element = wait.until(EC.element_to_be_clickable((By.ID,'J_SubmitStatic')))


ele_input_name = browser.find_element_by_id('TPL_username_1')
x = ele_input_name.location['x']
y = ele_input_name.location['y']

mouse.move(x, y)
# ActionChains(browser).move_to_element(ele_input_name).perform()
# ele_input_name.send_keys('15313349378')
# time.sleep(2)
#
# ele_input_pwd = browser.find_element_by_id('TPL_password_1')
# ActionChains(browser).move_to_element(ele_input_pwd).perform()
# ele_input_pwd.click()
#
# ele_move_ele = browser.find_element_by_id('_n1z')
#
# ele_slider_container = browser.find_element_by_id('nocaptcha')
#
# if ele_slider_container.is_displayed():
#
#     ele_move_ele = browser.find_element_by_id('_n1z')

    # ActionChains(browser).click_and_hold(ele_move_ele).move_to_element_with_offset(ele_move_ele, 301, 10).release().perform()

# browser.find_element_by_id('J_SubmitStatic').click()