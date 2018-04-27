#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""页面对象的基类"""

__author__ = 'kejie'

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import logging


class BasePage:

    def __init__(self, appium_driver):
        self.driver = appium_driver  # type:webdriver.Remote

    # 重新封装单个元素定位方法
    def find_element(self, loc, wait=15) -> webdriver.WebElement:
        try:
            WebDriverWait(self.driver, wait).until(lambda driver: driver.find_element(*loc))
            return self.driver.find_element(*loc)
        except:
            logging.error(u'{} 页面中未能找到 {} 元素'.format(self, loc))

    # 重新封装一组元素定位方法
    def find_elements(self, loc):
        try:
            if len(self.driver.find_elements(*loc)):
                return self.driver.find_elements(*loc)
        except:
            logging.error(u'{} 页面中未能找到 {} 元素'.format(self, loc))

    # 重新封装元素点击操作
    def tap_element(self, loc, x=0.0, y=0.0, find_first=True):
        try:
            if find_first:
                self.find_element(loc)
            self.driver.execute_script('mobile: tap', {'x': x, 'y': y, 'element': self.find_element(loc)})
        except AttributeError:
            logging.error(u'{} 页面中未能找到 {} 元素'.format(self, loc))

    # 重新封装输入操作
    def send_keys(self, loc, value):
        try:
            self.find_element(loc).set_value(value)
        except AttributeError:
            logging.error(u'{} 页面中未能找到 {} 元素'.format(self, loc))

    # 重新封装滑动操作
    def swipe(self, direct, loc=None):
        """
        滑动
        :param direct: 滑动方向，只支持up, down, left ,right四个值
        :param loc: 元素定位，空值为滑动屏幕，有值会滑动对应的元素
        :return:
        """
        if loc:
            self.driver.execute_script('mobile: swipe', {'direction': direct, 'element': self.find_element(loc)})
        else:
            self.driver.execute_script('mobile: swipe', {'direction': direct})


if __name__ == '__main__':
    pass
