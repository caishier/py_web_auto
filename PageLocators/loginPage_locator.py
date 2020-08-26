#!/usr/bin/python3
# _*_ coding: utf-8 _*_
# @Time : 2020/8/26 19:36 
# @Author : caixuan 
# @File : loginPage_locator.py
# @desc


from selenium.webdriver.common.by import By

class LoginPageLocators:
    # 用户名输入框
    user = (By.XPATH, "//input[@placeholder='请输入邮箱/手机号']")
    # 密码输入框
    passwd = (By.XPATH, "//input[@placeholder='请输入密码']")
    # 登录按钮
    login_button = (By.XPATH, "//button[@class='ivu-btn ivu-btn-primary ivu-btn-long']")