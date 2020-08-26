#!/usr/bin/python3
# _*_ coding: utf-8 _*_
# @Time : 2020/8/21 21:37 
# @Author : caixuan 
# @File : basePage.py
# @desc

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
import os
import datetime

from Common.dir_config import screenshot_dir
from Common import logger  # 直接执行了logger里的代码。设置日志输出。

class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver


    # 等待元素可见
    def wait_ele_visible(self,loc,img_desc,timeout=30,frequency=0.5):
        start = datetime.datetime.now()  # 用datetime模块获取时间
        try:
            WebDriverWait(self.driver,timeout,frequency).until(EC.visibility_of_element_located(loc))
        except:
            # 日志
            logging.exception("等待元素 {} 可见 失败！".format(loc))
            # 截图
            self.save_img(img_desc)
            raise   # 抛出异常，让用例识别到异常将用例状态为失败。
        else:
            end = datetime.datetime.now()  # 用datetime模块获取当前时间
            logging.info("等待 {}  元素  {} 可见成功。耗时：{}".format(img_desc,loc,end-start))

    # 等待元素存在
    def wait_ele_exists(self, loc, img_desc, timeout=30, frequency=0.5):
        start = datetime.datetime.now()  # 用datetime模块获取时间
        try:
            WebDriverWait(self.driver, timeout, frequency).until(EC.presence_of_element_located(loc))
        except:
            # 日志
            logging.exception("等待元素 {} 存在 失败！".format(loc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。
        else:
            end = datetime.datetime.now()  # 用datetime模块获取当前时间
            logging.info("等待 {}  元素  {} 存在成功。耗时：{}".format(img_desc, loc, end - start))

    # 查找元素
    def get_element(self,loc,img_desc):
        try:
            ele = self.driver.find_element(*loc)
        except:
            # 日志
            logging.exception("查找  {} 元素 {} 失败！".format(img_desc,loc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。
        else:
            logging.info("查找  {} 元素 {} 成功！".format(img_desc,loc))
            return ele


    def click_element(self,loc,img_desc,timeout=30,frequency=0.5):
        # 先等待可见
        self.wait_ele_visible(loc,img_desc,timeout,frequency)
        # 再查找元素
        ele = self.get_element(loc,img_desc)
        # 操作
        try:
            ele.click()  # 点击操作
            logging.info("点击  {} 元素 {} 成功！".format(img_desc, loc))
        except:
            # 日志
            logging.exception("点击  {} 元素 {} 失败！".format(img_desc, loc))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。


    def input_text(self,loc,value,img_desc,timeout=30,frequency=0.5):
        # 先等待可见
        self.wait_ele_visible(loc, img_desc, timeout, frequency)
        # 再查找元素
        ele = self.get_element(loc, img_desc)
        # 操作
        try:
            ele.send_keys(value)  # 点击操作
            logging.info("在 {} 元素 {} 上输入文本值：{} 成功！".format(img_desc,loc,value))
        except:
            # 日志
            logging.exception("在 {} 元素 {} 上输入文本值：{} 失败！".format(img_desc,loc,value))
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态为失败。

    # 获取元素的属性值
    def get_element_attribute(self, loc, attr_name, img_desc,timeout=30,frequency=0.5):
        self.wait_ele_exists(loc,img_desc,timeout,frequency)  # 等待元素存在
        ele = self.get_element(loc, img_desc) # 查找元素
        # 获取属性
        try:
            attr_value = ele.get_attribute(attr_name)
        except:
            # 日志
            logging.exception("获取 {} 元素 {} 的属性 {} 失败！".format(img_desc,loc, attr_name))
            # 截图
            self.save_img(img_desc)
            raise
        else:
            logging.info("获取 {} 元素 {} 的属性 {} 值为:{}".format(img_desc, loc, attr_name, attr_value))
            return attr_value

    # 获取元素的文本值。
    def get_text(self, loc, img_desc,timeout=30,frequency=0.5):
        self.wait_ele_exists(loc, img_desc, timeout, frequency)  # 等待元素存在
        ele = self.get_element(loc, img_desc) # 查找元素
        # 获取属性
        try:
            text = ele.text
        except:
            # 日志
            logging.exception("获取 {} 元素 {} 的文本失败！".format(img_desc, loc))
            # 截图
            self.save_img(img_desc)
            raise
        else:
            logging.info("获取 {} 元素 {} 的文本值为:{}".format(img_desc, loc, text))
            return text



    def save_img(self,img_description):
        """
        :param img_description: 图片的描述 。格式为 页面名称_功能名
        :return:
        """
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        # 时间戳 time模块  不要有:
        filepath = "{}_{}.png".format(img_description, now)
        img_path = os.path.join(screenshot_dir,filepath)
        try:
            self.driver.save_screenshot(img_path)
        except:
            logging.exception("网页截图失败！")
        else:
            logging.info("截图成功，截图存放在：{}".format(img_path))

    def switch_iframe(self,refrence,img_desc):
        """
        :param refrence: 识别iframe。可以是iframe的下标、name属性、WebElement对象、元组形式的定位表达。
        :return: 无
        """
        try:
            WebDriverWait(self.driver,10).until(EC.frame_to_be_available_and_switch_to_it(refrence))
        except:
            # 日志
            logging.exception("切换到 {} 的iframe: {} 失败！".format(img_desc, refrence))
            # 截图
            self.save_img(img_desc)
            raise
        else:
            logging.exception("切换到 {} 的iframe: {} 成功！".format(img_desc, refrence))