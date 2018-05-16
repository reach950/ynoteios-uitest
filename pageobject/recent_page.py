#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""最新列表页面"""

__author__ = 'kejie'

from pageobject.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy
from pageobject.page_common_module import TabBar, CreateButtonsLayer


class RecentPage(BasePage):

    # 创建scan按钮
    create_scan_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeNavigationBar/XCUIElementTypeButton[1]')

    # 创建audio按钮
    create_audio_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeNavigationBar/XCUIElementTypeButton[3]')

    # 第一个文件
    first_file_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeCell')

    # 链接收藏输入框
    link_collect_textview_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeTextView" AND enabled == 1')

    # 获取第一个文件的标题
    def get_first_file_title(self, file_type):
        index = 0
        if file_type == 'note':
            index = 2
        elif file_type == 'audio':
            index = 3
        elif file_type == 'markdown':
            index = 2
        elif file_type == 'pic':
            index = 2
        elif file_type == 'hand_write':
            index = 1
        # 第一个文件标题
        first_file_title_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell/XCUIElementTypeStaticText[{}]'
                                .format(index))
        return self.find_element(first_file_title_loc).get_attribute('value')

    # 点击第一个文件的删除按钮
    def click_first_file_delete_button(self, is_sync=False):
        if is_sync:
            index = 3
        else:
            index = 4
        # 第一个文件的删除按钮
        first_file_delete_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell/XCUIElementTypeButton[{}]'
                                        .format(index))
        self.tap_element(first_file_delete_button_loc)

    # 打开创建笔记页面
    def open_create_note(self):
        self.tap_element(TabBar.create_button_loc)
        self.tap_element(CreateButtonsLayer.create_note_buuton_loc)

    # 删除第一个文件
    def delete_first_file(self, is_sync=False):
        self.swipe('left', self.first_file_loc)
        if is_sync:
            self.click_first_file_delete_button(is_sync)
        else:
            self.click_first_file_delete_button()
        self.click_alert_button('删除')

    # 切换到文件夹
    def switch_to_folder_page(self):
        self.tap_element(TabBar.folder_button_loc)

    # 打开创建scan页面
    def open_create_scan(self, is_from_tabbar=False):
        if is_from_tabbar:
            self.tap_element(TabBar.create_button_loc)
            self.tap_element(CreateButtonsLayer.create_scan_buuton_loc)
        else:
            self.tap_element(self.create_scan_button_loc)

    # 打开创建audio页面
    def open_create_audio(self, is_from_tabbar=False):
        if is_from_tabbar:
            self.tap_element(TabBar.create_button_loc)
            self.tap_element(CreateButtonsLayer.create_audio_buuton_loc)
        else:
            self.tap_element(self.create_audio_button_loc)

    # 打开创建markdown页面
    def open_create_markdown(self):
        self.tap_element(TabBar.create_button_loc)
        self.tap_element(CreateButtonsLayer.create_markdown_button_loc)

    # 打开创建链接收藏笔记
    def open_create_link_collect_note(self):
        self.tap_element(TabBar.create_button_loc)
        self.tap_element(CreateButtonsLayer.link_collect_button_loc)

    # 打开上传图片页面
    def open_upload_pic(self):
        self.tap_element(TabBar.create_button_loc)
        self.tap_element(CreateButtonsLayer.upload_pic_button_loc)

    # 打开创建手写笔记页面
    def open_create_handwrite(self):
        self.tap_element(TabBar.create_button_loc)
        self.tap_element(CreateButtonsLayer.create_handwrite_button_loc)

    # 输入收藏的链接
    def input_link(self, url):
        self.send_keys(self.link_collect_textview_loc, url)
