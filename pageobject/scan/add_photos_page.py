#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""文档扫描添加照片页面"""

__author__ = 'kejie'

from pageobject.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class AddPhotosPage(BasePage):

    # 返回按钮
    return_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeNavigationBar/XCUIElementTypeButton[1]')

    # 相册按钮
    album_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeNavigationBar/XCUIElementTypeButton[4]')

    # 引导图片
    guide_pic_loc = (MobileBy.ACCESSIBILITY_ID, 'scan_guide')

    # 引导提示确认按钮
    guide_button_loc = (MobileBy.ACCESSIBILITY_ID, '知道了')

    # 拍照扫描按钮
    photograph_button_loc = (MobileBy.IOS_CLASS_CHAIN, 'XCUIElementTypeWindow/**/XCUIElementTypeButton[-1]')

    # 完成按钮
    complete_button_loc = (MobileBy.ACCESSIBILITY_ID, '完成')

    # 点击引导确认按钮
    def tap_guide_button(self):
        self.tap_element(self.guide_button_loc)

    # 点击拍照扫描按钮
    def tap_photograph_button(self):
        self.tap_element(self.photograph_button_loc)

    # 点击相册
    def tap_album_button(self):
        self.tap_element(self.album_button_loc)

    # 点击完成
    def tap_complete_button(self):
        self.tap_element(self.complete_button_loc)

    # 是否显示文档扫描引导
    def is_scan_guide_display(self):
        if self.find_element(self.guide_pic_loc, check_display=False, wait=10):
            return True
        else:
            return False

    # 点击返回
    def tap_return_button(self):
        self.tap_element(self.return_button_loc)
