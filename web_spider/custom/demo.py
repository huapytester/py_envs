# -*- coding:utf-8 -*-

import requests
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from scrapy.selector import Selector

# 使用selenium和scrapy的selector提取元素
# browser = webdriver.Chrome()
# browser.get('https://www.lagou.com/jobs/3382067.html')
# text = browser.page_source.encode('utf-8')
#
# value_selector = Selector(text=text)
# value = value_selector.css('.job_request').extract()
# print(value)
#
# browser.quit()

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/#signin')
browser.find_element_by_css_selector('.signin-switch-password').click()
username = browser.find_element_by_name('account')
username.click()
username.send_keys('18616272151')
password = browser.find_element_by_name('password')
password.click()
password.send_keys('Happy1023')

# 智能等待
WebDriverWait(browser, 10, 1).until(lambda x: browser.find_element_by_css_selector('.AppHeader-profileAvatar'))

# with open('demo.html', 'w') as fp:
#     fp.write(browser.page_source)
for i in range(3):
    # 滚动条到最下面
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(3)

