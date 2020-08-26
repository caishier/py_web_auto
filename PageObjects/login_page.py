#!/usr/bin/python3
# _*_ coding: utf-8 _*_
# @Time : 2020/8/12 21:52 
# @Author : caixuan 
# @File : login_page.py
# @desc

from PageLocators.loginPage_locator import LoginPageLocators as loc
from Common.basePage import BasePage

class LoginPage(BasePage):

    def login(self, username, password):


        # 输入用户名
        self.input_text(loc.user, username,"登陆页面_输入用户名")
        # 输入密码
        self.input_text(loc.passwd, password,"登陆页面_输入密码")
        # 点击登录按钮
        self.click_element(loc.login_button,"登陆页面_点击登陆按钮")




