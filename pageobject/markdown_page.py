#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""markdown详情页面"""

__author__ = 'kejie'

from pageobject.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class MarkdownPage(BasePage):

    # markdown标题
    md_title_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextField')

    # 预览按钮
    md_preview_loc = (MobileBy.ACCESSIBILITY_ID, '预览')

    # 返回按钮
    md_return_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeNavigationBar/XCUIElementTypeButton[1]')

    # 编辑按钮
    md_edit_loc = (MobileBy.ACCESSIBILITY_ID, 'markdown edit')

    # 输入md标题
    def input_md_title(self, value):
        self.send_keys(self.md_title_loc, value)

    # 点击预览按钮
    def tap_preview_button(self):
        self.tap_element(self.md_preview_loc)

    # 点击编辑按钮
    def tap_edit_button(self):
        self.tap_element(self.md_edit_loc)

    # 点击返回按钮
    def tap_return_button(self):
        self.tap_element(self.md_return_loc)

    # 检查markdown是否在编辑状态
    def is_md_edit(self):
        return self.find_element(self.md_preview_loc).is_displayed()

    # 检查markdown是否在预览状态
    def is_md_preview(self):
        return self.find_element(self.md_edit_loc).is_displayed()