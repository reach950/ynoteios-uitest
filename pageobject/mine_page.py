#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""我的页面"""

__author__ = 'kejie'

from pageobject.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class MinePage(BasePage):

    # 退出登录按钮
    logout_button_loc = (MobileBy.ACCESSIBILITY_ID, '退出登录')

    # 点击退出登录
    def tap_logout_button(self):
        self.tap_element(self.logout_button_loc)
