#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""最新列表页面"""

__author__ = 'kejie'

from pageobject.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy
from pageobject.page_common_module import TabBar, CreateButtonsLayer


class RecentPage(BasePage):

    # 第一个文件
    first_file = (MobileBy.CLASS_NAME, 'XCUIElementTypeCell')

    # 第一个文件的删除按钮
    delete_button = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell/XCUIElementTypeButton[3]')

    # 打开创建笔记页面
    def open_create_note(self):
        self.tap_element(TabBar.create_button_loc)
        self.tap_element(CreateButtonsLayer.create_note_buuton_loc)

    # 根据文本内容获取第一个文件的标题
    def get_first_file_title(self, text):
        first_file_title_loc = (MobileBy.IOS_CLASS_CHAIN, u'**/XCUIElementTypeCell/XCUIElementTypeStaticText'
                                                          u'[`name == \"{}\"`]'.format(text))
        return self.find_element(first_file_title_loc)

    # 删除第一个文件
    def delete_first_file(self):
        self.swipe('left', self.first_file)
        self.tap_element(self.delete_button)
        self.click_alert_button('删除')

    # 切换到文件夹
    def switch_to_folder_page(self):
        self.tap_element(TabBar.folder_button_loc)
