#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""最新列表页面"""

__author__ = 'kejie'

from pageobject.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class RecentPage(BasePage):

    # tabbar的创建按钮
    create_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTabBar/**/XCUIElementTypeButton[3]')

    # 关闭创建列表按钮
    create_close_button_loc = (MobileBy.ACCESSIBILITY_ID, 'create note close')

    # 创建笔记按钮
    create_note_buuton_loc = (MobileBy.ACCESSIBILITY_ID, 'newNote-note')

    # 新创建笔记标题
    first_note_title_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell/XCUIElementTypeStaticText[2]')

    # 最新文件
    first_file = (MobileBy.CLASS_NAME, 'XCUIElementTypeCell')

    # 删除按钮
    delete_button = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell/XCUIElementTypeButton[3]')

    # 点击创建按钮
    def tap_create_button(self):
        self.tap_element(self.create_button_loc)

    # 点击创建笔记按钮
    def tap_create_note_button(self):
        self.tap_element(self.create_note_buuton_loc)

    # 浮层是否显示
    def supernatant_is_display(self):
        return self.find_element(self.create_close_button_loc).is_displayed()

    # 获取新创建笔记的标题
    def get_first_note_title(self):
        return self.find_element(self.first_note_title_loc).get_attribute('value')

    # 向左滑动最新文件
    def swipe_left_first_file(self):
        self.swipe('left', self.first_file)

    # 点击删除按钮
    def tap_delete_button(self):
        self.tap_element(self.delete_button)
