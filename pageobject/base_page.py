#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""页面对象的基类"""

__author__ = 'kejie'

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
import logging
import time
import json


class BasePage:

    def __init__(self, appium_driver):
        self.driver = appium_driver  # type:webdriver.Remote

    # 重新封装单个元素定位方法
    def find_element(self, loc, check_display=True, wait=15) -> webdriver.WebElement:
        """

        :param loc:
        :param check_display: image元素的isVisible属性一直是No，需要改为False
        :param wait:
        :return:
        """
        try:
            if check_display:
                WebDriverWait(self.driver, wait).until(lambda driver: driver.find_element(*loc).is_displayed())
            else:
                WebDriverWait(self.driver, wait).until(lambda driver: driver.find_element(*loc))
            return self.driver.find_element(*loc)
        except WebDriverException:
            logging.error(u'{} 页面中未能找到 {} 元素！'.format(self, loc))

    # 重新封装一组元素定位方法
    def find_elements(self, loc, wait=15):
        try:
            WebDriverWait(self.driver, wait).until(lambda driver: driver.find_elements(*loc))
            return self.driver.find_elements(*loc)
        except WebDriverException:
            logging.error(u'{} 页面中未能找到 {} 元素！'.format(self, loc))

    # 重新封装元素点击操作
    def tap_element(self, loc, check_display=True):
        ele = self.find_element(loc, check_display)
        rect = json.loads(ele.get_attribute('rect'))
        x = rect['width'] / 2
        y = rect['height'] / 2
        self.driver.execute_script('mobile: tap', {'x': x, 'y': y, 'element': ele})

    # 重新封装窗口点击操作
    def tap_window(self, x, y):
        self.driver.execute_script('mobile: tap', {'x': x, 'y': y})

    # 重新封装输入操作
    def send_keys(self, loc, value, check_display=True):
        ele = self.find_element(loc, check_display)
        try:
            ele.clear()
            ele.set_value(value)
        except WebDriverException:
            logging.error(u'{} 页面中 {} 元素输入文本失败！'.format(self, loc))

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

    # 重新封装拖放操作
    def drag_from_to_for_duration(self, from_x, from_y, to_x, to_y, duration=1.0, loc=None):
        """
        通过坐标执行拖放手势
        :param from_x: 起始拖动点的x坐标（类型为float）
        :param from_y: 起始拖动点的y坐标（类型为float）
        :param to_x: 结束拖动点的x坐标（类型为float）
        :param to_y: 结束拖动点的y坐标（类型为float）
        :param duration: 持续时间：范围[0.5，60]内的秒数
        :param loc: 元素定位，空值时所有坐标为绝对屏幕坐标，有值时所有坐标将相对计算在屏幕上的这个元素位置
        :return:
        """
        if loc:
            self.driver.execute_script(
                'mobile: dragFromToForDuration', {'duration': duration, 'fromX': from_x, 'fromY': from_y, 'toX': to_x,
                                                  'toY': to_y, 'element': self.find_element(loc)})
        else:
            self.driver.execute_script(
                'mobile: dragFromToForDuration', {'duration': duration, 'fromX': from_x, 'fromY': from_y, 'toX': to_x,
                                                  'toY': to_y})

    def get_alert_buttons(self):
        """
        获取当前警告框的按钮名称
        :return:
        """
        return self.driver.execute_script('mobile: alert', {'action': 'getButtons'})

    def click_alert_button(self, button_lable, action='accept'):
        """
        警告框处理
        :param button_lable: 警告框按钮的标签文本
        :param action: 按钮处理，只支持accept，dismiss两个值
        :return:
        """
        self.driver.execute_script('mobile: alert', {'action': action, 'buttonLabel': button_lable})

    def set_clipboard_text(self, text):
        """
        设置剪切板内容，默认UTF-8，只支持模拟器，真机不支持
        :param text:
        :return:
        """
        self.driver.execute_script("mobile: setPasteboard", {'content': text, 'encoding': 'UTF-8'})

    def get_clipboard_text(self):
        """
        获取剪切板内容，默认UTF-8，只支持模拟器，真机不支持
        :return:
        """
        return self.driver.execute_script('mobile: getPasteboard', {'encoding': 'UTF-8'})

    def accept_alert(self, timeout=5.0):
        """
        如果弹出警告框，就接受
        :return:
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.is_alert_exist():
                buttons = self.get_alert_buttons()
                btns = {u'好', u'允许', 'Allow', 'OK'}.intersection(buttons)
                if len(btns) == 0:
                    raise RuntimeError(u'警告框无法接受, buttons: {}'.format(', '.join(buttons)))
                self.click_alert_button(list(btns)[0])
                return
            else:
                time.sleep(0.5)

    def is_alert_exist(self):
        try:
            self.get_alert_buttons()
        except WebDriverException:
            return False
        else:
            return True


if __name__ == '__main__':
    pass
