#!/usr/bin/python3
# _*_ coding: utf-8 _*_
# @Time : 2020/8/12 21:52 
# @Author : caixuan 
# @File : test_login.py
# @desc

from selenium import webdriver
import pytest
from PageObjects.login_page import LoginPage
from TestDatas import login_datas as ld
from TestDatas import Comm_Datas as cd

@pytest.mark.usefixtures("init_driver")
class Test_login:

    @pytest.mark.smoke
    def test_login_success(self,init_driver):#fixture的函数名城管，作为参数传给测试用例，函数名称=fixture执行结果

        LoginPage(init_driver).login(ld.success_data["user"],ld.success_data["passwd"])

        assert init_driver.current_url == ld.success_data["check"]
