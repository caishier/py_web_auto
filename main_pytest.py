#!/usr/bin/python3
# _*_ coding: utf-8 _*_
# @Time : 2020/8/26 19:51 
# @Author : caixuan 
# @File : main_pytest.py
# @desc


import pytest


if __name__ == '__main__':
    pytest.main(["-m","smoke","--html=Outputs/report/pytest.html"])
