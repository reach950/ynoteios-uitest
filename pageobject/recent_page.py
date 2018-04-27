#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""最新列表页面"""

__author__ = 'kejie'

from pageobject.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy
from pageobject import TabBar, CreateButtonsLayer


class RecentPage(BasePage):

    # 新创建笔记标题
    first_note_title_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell/XCUIElementTypeStaticText[2]')

    # 第一个文件
    first_file = (MobileBy.CLASS_NAME, 'XCUIElementTypeCell')

    # 删除按钮
    delete_button = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell/XCUIElementTypeButton[3]')

    # 打开创建笔记页面
    def open_create_note(self):
        self.tap_element(TabBar.create_button_loc)
        self.tap_element(CreateButtonsLayer.create_note_buuton_loc)

    # 获取新创建笔记的标题
    def get_first_note_title(self):
        return self.find_element(self.first_note_title_loc).get_attribute('value')

    # 删除第一个文件
    def delete_first_file(self):
        self.swipe('left', self.first_file)
        self.tap_element(self.delete_button)
