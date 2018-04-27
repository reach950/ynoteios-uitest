#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""笔记详情页面"""

__author__ = 'kejie'

from pageobject.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class NotePage(BasePage):

    # 笔记标题
    note_title_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextField')

    # 完成按钮
    complete_button_loc = (MobileBy.ACCESSIBILITY_ID, '完成')

    # 返回按钮
    return_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeNavigationBar/XCUIElementTypeButton[1]')

    # 输入笔记标题
    def input_note_title(self, value):
        self.send_keys(self.note_title_loc, value)

    # 点击完成
    def tap_complete_button_loc(self):
        self.tap_element(self.complete_button_loc)

    # 点击返回
    def tap_return_button_loc(self):
        self.tap_element(self.return_button_loc)
