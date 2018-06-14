#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""最新列表页面"""

__author__ = 'kejie'

from pageobject.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy
from pageobject.page_common_module import TabBar, CreateButtonsLayer
import time


class RecentPage(BasePage):

    # 创建scan按钮
    create_scan_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeNavigationBar/XCUIElementTypeButton[1]')

    # 创建audio按钮
    create_audio_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeNavigationBar/XCUIElementTypeButton[3]')

    # 最新页面导航栏
    navigation_bar_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeNavigationBar" AND name == "最新"')

    # 第一个文件
    first_file_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeCell')

    # 第一个文件的删除按钮
    first_file_delete_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell/XCUIElementTypeButton[-1]')

    # 链接收藏输入框
    link_collect_textview_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeTextView" AND visible == 1')

    # 导航栏更多操作列表下的按钮（iPhoneX）
    sync_loc = {'x': 290.0, 'y': 121.5}
    display_summary_loc = {'x': 290.0, 'y': 182.5}
    dispaly_share_loc = {'x': 290.0, 'y': 217.5}

    # 第一个文件的标题的是否存在
    def is_first_file_title_exist(self, text):
        # 第一个文件标题
        first_file_title_loc = (MobileBy.IOS_CLASS_CHAIN,
                                '**/XCUIElementTypeCell/XCUIElementTypeStaticText[`name BEGINSWITH \"{}\"`]'
                                .format(text))
        # 获取isVisible属性时，如果最新列表刚好同步成功，则返回False，故设置check_display为False
        if self.find_element(first_file_title_loc, check_display=False):
            return True
        else:
            return False

    # 根据文件后缀名获取第一个文件的标题,App自带文件格式（note，scan，md，audio）没有后缀名无法获取
    def get_first_file_title_by_extension(self, extension):
        # 第一个文件标题
        first_file_title_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell/'
                                                          'XCUIElementTypeStaticText'
                                                          '[`name ENDSWITH \"{}\"`]'.format(extension))
        return self.find_element(first_file_title_loc, check_display=False).get_attribute('value')

    # 删除第一个文件
    def delete_first_file(self):
        self.swipe('left', self.first_file_loc)
        self.tap_element(self.first_file_delete_button_loc)
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

    # 第一次登录时，等待页面同步成功
    def wait_first_sync_success(self, timeout=30.0):
        start_time = time.time()
        while time.time() - start_time < timeout:
            first_sync_file_number = self.get_file_number()
            time.sleep(1)
            if first_sync_file_number > 1 and first_sync_file_number == self.get_file_number():
                return

    # 等待第一个文件同步成功
    def wait_first_file_sync_success(self, timeout=15.0):
        # 第一个文件的同步按钮
        first_file_sync_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell/XCUIElementTypeButton')
        first_file_sync_button = self.find_element(first_file_sync_button_loc, wait=10)
        if first_file_sync_button:
            start_time = time.time()
            while time.time() - start_time < timeout:
                if not self.find_element(first_file_sync_button_loc, wait=3):
                    return

    # 获取最新列表文件个数
    def get_file_number(self):
        return len(self.find_elements(self.first_file_loc))
