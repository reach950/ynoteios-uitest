#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""登录页面"""

__author__ = 'kejie'

from pageobject.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class LoginPage(BasePage):

    # 账号输入框
    account_input_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextField')

    # 密码输入框
    password_input_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeSecureTextField')

    # 登录按钮
    login_button_loc = (MobileBy.ACCESSIBILITY_ID, '登录')

    # 网易通行证登录
    def login_by_netease_email(self, user_id, password):
        self.send_keys(self.account_input_loc, user_id)
        self.send_keys(self.password_input_loc, password)
        self.tap_element(self.login_button_loc)
