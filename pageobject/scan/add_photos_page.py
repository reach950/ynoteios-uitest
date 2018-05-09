#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""文档扫描添加照片页面"""

__author__ = 'kejie'

from pageobject.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class AddPhotosPage(BasePage):

    # 相册按钮
    album_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeNavigationBar/XCUIElementTypeButton[4]')

    # 引导提示确认按钮
    guide_button_loc = (MobileBy.ACCESSIBILITY_ID, '知道了')

    # 拍照扫描按钮
    photograph_button_loc = (MobileBy.IOS_CLASS_CHAIN, 'XCUIElementTypeWindow/**/XCUIElementTypeButton[5]')

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

    # 如果需要摄像头和相册的系统权限，选是
    def get_camera_album_right(self):
        if '好' in self.get_alert_buttons():
            self.click_alert_button('好')
