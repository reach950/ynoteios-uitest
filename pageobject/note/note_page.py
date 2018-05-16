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

    # 分享按钮
    share_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeNavigationBar/XCUIElementTypeButton[-2]')

    # 复制分享链接按钮
    copy_share_link_loc = (MobileBy.ACCESSIBILITY_ID, 'copyShareLink')

    # 复制成功提示
    copy_share_link_success_loc = (MobileBy.ACCESSIBILITY_ID, '链接复制成功')

    # 输入笔记标题
    def input_note_title(self, value):
        self.send_keys(self.note_title_loc, value)

    # 点击完成
    def tap_complete_button(self):
        self.tap_element(self.complete_button_loc)

    # 点击返回
    def tap_return_button(self):
        self.tap_element(self.return_button_loc)

    # 点击分享
    def tap_share_button(self):
        self.tap_element(self.share_button_loc)

    # 复制分享链接
    def copy_share_link(self):
        self.tap_element(self.copy_share_link_loc)

    # 检查是否显示复制链接成功的提示
    def is_copy_share_link_success(self):
        if self.find_element(self.copy_share_link_success_loc):
            return True
        else:
            return False
