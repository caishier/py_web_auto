#!/usr/bin/python3
# _*_ coding: utf-8 _*_
# @Time : 2020/8/26 19:48 
# @Author : caixuan 
# @File : dir_config.py
# @desc


import os

#框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

testdatas_dir =  os.path.join(base_dir,"TestDatas")

testcases_dir =  os.path.join(base_dir,"TestCases")

htmlreport_dir =  os.path.join(base_dir,"Outputs/reports")

logs_dir =  os.path.join(base_dir,"Outputs/logs")

# config_dir =  os.path.join(base_dir,"Config")

screenshot_dir = os.path.join(base_dir,"Outputs/screenshots")
print(screenshot_dir)