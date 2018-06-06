#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""文件夹页面"""

__author__ = 'kejie'

from pageobject.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class FolderPage(BasePage):

    # 导航栏更多按钮
    multi_operation_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeNavigationBar/XCUIElementTypeButton[2]')

    # 当前目录下的第一个文件
    first_file_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeCell')

    # 导航栏更多操作列表下的按钮（iPhoneX）
    batch_edit_loc = {'x': 290.0, 'y': 121.5}
    create_folder_loc = {'x': 290.0, 'y': 156.5}
    sync_loc = {'x': 290.0, 'y': 191.5}
    display_summary_loc = {'x': 290.0, 'y': 252.5}
    sort_by_modify_time_loc = {'x': 290.0, 'y': 313.5}
    sort_by_title_loc = {'x': 290.0, 'y': 348.5}
    sort_by_create_time_loc = {'x': 290.0, 'y': 383.5}

    # 新建文件夹输入框
    create_folder_textfield_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeTextField" AND visible == 1')

    # 没有文档的背景图片
    no_file_image_loc = (MobileBy.ACCESSIBILITY_ID, 'noNotePlaceholder')

    # 打开指定标题的文件夹
    def open_folder_by_title(self, text):
        folder_title_loc = (MobileBy.ACCESSIBILITY_ID, text)
        self.tap_element(folder_title_loc)

    # 打开当前目录下的第一个文件
    def open_first_file(self):
        self.tap_element(self.first_file_loc)

    # 指定标题的文件夹是否存在
    def is_folder_exist_by_title(self, text):
        folder_title_loc = (MobileBy.ACCESSIBILITY_ID, text)
        if self.find_element(folder_title_loc):
            return True
        else:
            return False

    # 创建指定标题的文件夹
    def create_folder_by_title(self, text):
        self.tap_element(self.multi_operation_button_loc)
        self.tap_window(self.create_folder_loc['x'], self.create_folder_loc['y'])
        self.send_keys(self.create_folder_textfield_loc, text)
        self.click_alert_button('确认')

    # 当前目录是否为空
    def is_folder_empty(self):
        if self.find_element(self.no_file_image_loc, check_display=False):
            return True
        else:
            return False
