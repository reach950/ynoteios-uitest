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

    # 最新页面导航栏
    navigation_bar_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeNavigationBar" AND name == "最新"')

    # 第一个文件
    first_file_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeCell')

    # 链接收藏输入框
    link_collect_textview_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeTextView" AND enabled == 1')

    # 同步成功的提示
    sync_success_tips_loc = (MobileBy.ACCESSIBILITY_ID, '同步成功')

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

    # 删除第一个文件
    def delete_first_file(self, is_sync=False):
        self.swipe('left', self.first_file_loc)
        if is_sync:
            self.click_first_file_delete_button(is_sync)
        else:
            self.click_first_file_delete_button()
        self.click_alert_button('删除')

    # 打开创建指定文件的页面
    def open_create_file_from_tabbar(self, file_type):
        self.tap_element(TabBar.create_button_loc)
        if file_type == 'note':
            self.tap_element(CreateButtonsLayer.create_note_buuton_loc, check_display=False)
        elif file_type == 'scan':
            self.tap_element(CreateButtonsLayer.create_scan_buuton_loc, check_display=False)
        elif file_type == 'audio':
            self.tap_element(CreateButtonsLayer.create_audio_buuton_loc, check_display=False)
        elif file_type == 'markdown':
            self.tap_element(CreateButtonsLayer.create_markdown_button_loc, check_display=False)
        elif file_type == 'link_collect':
            self.tap_element(CreateButtonsLayer.link_collect_button_loc, check_display=False)
        elif file_type == 'pic':
            self.tap_element(CreateButtonsLayer.upload_pic_button_loc, check_display=False)
        elif file_type == 'hand_write':
            self.tap_element(CreateButtonsLayer.create_handwrite_button_loc, check_display=False)

    # 打开创建scan页面
    def open_create_scan(self, is_from_tabbar=False):
        if is_from_tabbar:
            self.open_create_file_from_tabbar('scan')
        else:
            self.tap_element(self.create_scan_button_loc)

    # 打开创建audio页面
    def open_create_audio(self, is_from_tabbar=False):
        if is_from_tabbar:
            self.open_create_file_from_tabbar('audio')
        else:
            self.tap_element(self.create_audio_button_loc)

    # 切换到指定tab
    def switch_to_dest_page(self, dest):
        if dest == 'recent':
            self.tap_element(TabBar.recent_button_loc)
        elif dest == 'folder':
            self.tap_element(TabBar.folder_button_loc)
        elif dest == 'collect':
            self.tap_element(TabBar.collect_button_loc)
        elif dest == 'mine':
            self.tap_element(TabBar.mine_button_loc)

    # 输入收藏的链接
    def input_link(self, url):
        self.send_keys(self.link_collect_textview_loc, url)

    # 最新页面是否显示
    def is_recent_page_dispaly(self):
        if self.find_element(self.navigation_bar_loc, check_display=False).is_displayed():
            return True
        else:
            return False

    # 是否同步成功
    def is_sync_success(self):
        if self.find_element(self.sync_success_tips_loc, wait=20.0):
            return True
        else:
            return False