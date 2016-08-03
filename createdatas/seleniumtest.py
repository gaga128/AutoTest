# -*- coding: utf-8 -*-
#****************************************************************
# main.py
# Author     : JIA
# Version    : 1.0
# Date       : 2016-05-30
# Description: 造数据
#***************************************************************
import os
from selenium import webdriver

# chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# os.environ["webdriver.chrome.driver"] = chromedriver     ####webdriver.chrome.driver.系统属性指定chromrDriver。exe所在位置，相当于配置环境变量,已配置环境变量可以不写这一段
# driver1 = webdriver.Chrome(chromedriver)

option =webdriver.ChromeOptions()
option.add_argument('test-type')
driver = webdriver.Chrome(chrome_options=option)
driver.get('http://dev.data.social-touch.com:30053/')

user_element = driver.find_element_by_id('username')
user_element.send_keys('admin@admin.com')
pawd_element=driver.find_element_by_id('userpass')
pawd_element.send_keys('QL7u7XT9kE')

login_element=driver.find_element_by_class_name('login-go')
login_element.click()
login_element.is_enabled()


select_element=driver.find_element_by_class_name('selectPlat')
select_element.click()
select_element.is_enabled()