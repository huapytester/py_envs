# -*- coding:utf-8 -*-

from selenium import webdriver

# 实例化一个chrome配置对象
chrome_opt = webdriver.ChromeOptions()

# 设置默认浏览器最大化
chrome_opt.add_argument("--start-maximized")
'''
--incognito            设置隐身模式
--user-agent=iphone    模拟手机登录
'''
# 设置chrome默认不加载图片
chrome_opt.add_experimental_option('prefs', {'profile.managed_default_content_settings.images': 2})
# 设置chrome默认不加载js
chrome_opt.add_experimental_option('prefs', {'profile.managed_default_content_settings.javascript': 2})

browser = webdriver.Chrome(chrome_options=chrome_opt)

browser.get('http://www.taobao.com/')


