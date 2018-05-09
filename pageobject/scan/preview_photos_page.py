#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""文档扫描图片预览页面"""

__author__ = 'kejie'

from pageobject.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class PreviewPhotosPage(BasePage):

    # scan文件标题
    scan_title_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextField')

    # 完成按钮
    complete_button_loc = (MobileBy.ACCESSIBILITY_ID, '完成')

    # 输入scan标题
    def input_scan_title(self, value):
        self.send_keys(self.scan_title_loc, value)

    # 点击完成
    def tap_complete_button(self):
        self.tap_element(self.complete_button_loc)
