#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""相册页面"""

__author__ = 'kejie'

from pageobject.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class AlbumPage(BasePage):

    # 第一张照片
    first_photo_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeCell" AND visible == 1')

    # 完成按钮
    complete_button_loc = (MobileBy.ACCESSIBILITY_ID, '完成')

    # 点击第一张图片
    def tap_first_photo(self):
        self.tap_element(self.first_photo_loc)

    # 点击完成
    def tap_complete_button(self):
        self.tap_element(self.complete_button_loc)

    # 检查完成按钮的enable状态
    def is_complete_button_enabled(self):
        return self.find_element(self.complete_button_loc).is_enabled()
