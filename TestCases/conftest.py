#!/usr/bin/python3
# _*_ coding: utf-8 _*_
# @Time : 2020/8/24 21:20 
# @Author : caixuan 
# @File : conftest.py
# @desc


from selenium import webdriver
from TestDatas import Comm_Datas as cd
import pytest

from PageObjects.login_page import LoginPage
# conftest.py  前置后置共享的文件。不需要主动调用

# 定义前置后置  - 明确它的作用范围。 写一个函数(代码)  @pytest.fxiture

@pytest.fixture   # 声明它之下的函数是一个 pytest的  前置后置 - 函数级别的
def init_driver():
    # 前置
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(cd.web_login_url)
    yield driver      # 隔开前置后置。2、返回值
    # 后置
    driver.quit()

@pytest.fixture(scope="class")
def myFix():
    print("====我是测试类 ===  前置========")
    yield
    print("====我是测试类 ===  后置=======")


# 打开浏览器 - 访问网址    ---- 前置
# 关闭浏览器     ---- 后置

# 打开浏览器 - 访问网址  -  登陆网站    ---- 前置
# 关闭浏览器     ---- 后置
@pytest.fixture   # 声明它之下的函数是一个 pytest的  前置后置 - 函数级别的
def login_web(init_driver):  # 调用并且也代表返回值
    # 前置
    LoginPage(init_driver).login(cd.user, cd.passwd)
    yield init_driver      # 隔开前置后置。2、返回值

"""  fixture的执行顺序   login_web  包含了 init_dirver 的前置后置
init_driver 前置
login_web  前置
login_web  后置
init_driver 后置
"""

# 调用定义好的fixture
# 在测试类/测试用例的前面，使用：@pytest.mark.usefixtures("定义的fixture函数名称")
# 如果有返回值，那么fixture的函数名称，作为测试用例 的参数，将返回值传递给测试用例 。fixture的函数名称=返回值。

# @pytest.fixture(scope="module")
# def myMod():
#     print("====我是一个模块级别的 ===  前置========")
#     yield
#     print("====我是一个模块级别的 ===  后置=======")
#
#
# @pytest.fixture(scope="session",autouse=True)  # 夹的是所有测试用例。
# def myMod():
#     print("====我是一个用例会话级别的 ===  前置========")
#     yield True
#     print("====我是一个用例会话级别的 ===  后置=======")