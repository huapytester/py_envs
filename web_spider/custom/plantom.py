# -*- coding:utf-8 -*-

from selenium import webdriver

browser = webdriver.PhantomJS(executable_path=r'F:\迅雷下载\phantomjs-2.1.1-windows\bin\phantomjs.exe')

browser.get('https://gabygaby.taobao.com/dc-3786.htm?spm=a211ds.2163.182.3.14416edee7wqZK')

print(browser.title)

browser.quit()