#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试用例的基类"""

__author__ = 'kejie'

import unittest
import pageobject as po
from lib import AppiumDriver
from lib import utils
from lib import get_time


class BaseCase(unittest.TestCase):

    def setUp(self):
        # 打开Appium服务器，start server后，尝试启动被测App
        self.driver = AppiumDriver().get_driver()
        # 初始化App的页面对象
        self.init_page()
        self.handle_first_open_app()

    def tearDown(self):
        self.driver.quit()

    def init_page(self):
        self.recent_page = po.RecentPage(self.driver)
        self.folder_page = po.FolderPage(self.driver)
        self.note_page = po.NotePage(self.driver)
        self.hand_write_page = po.HandWritePage(self.driver)
        self.add_photos_page = po.AddPhotosPage(self.driver)
        self.preview_photos_page = po.PreviewPhotosPage(self.driver)
        self.scan_page = po.ScanPage(self.driver)
        self.album_page = po.AlbumPage(self.driver)
        self.record_page = po.RecordPage(self.driver)
        self.audio_page = po.AudioPage(self.driver)
        self.markdown_page = po.MarkdownPage(self.driver)
        self.login_page = po.LoginPage(self.driver)
        self.mine_page = po.MinePage(self.driver)
        self.intro_page = po.IntroPage(self.driver)

    # 处理第一次打开app的引导页和登录问题
    def handle_first_open_app(self):
        if not self.recent_page.is_recent_page_dispaly():
            if self.intro_page.is_intro_page_dispaly():
                # 接受app弹出的请求通知权限
                self.intro_page.accept_alert(timeout=15.0)
                self.intro_page.handle_intro_page()
                self.recent_page.switch_to_dest_page('mine')
                self.user_id = utils.get_account('163')['userId']
                self.password = utils.get_account('163')['password']
                self.login_page.login_by_netease_email(self.user_id, self.password)
                self.recent_page.wait_sync_success()

    def open_note_from_note_folder(self):
        self.recent_page.switch_to_dest_page('folder')
        # 如果没有note文件夹，则创建一个
        if self.folder_page.is_folder_exist_by_title('note'):
            self.folder_page.create_folder_by_title('note')
        self.folder_page.open_folder_by_title('note')
        # 如果note文件夹没有笔记，则创建一个
        if self.folder_page.is_folder_empty():
            title = u'create_textnote_{}'.format(get_time())
            self.recent_page.open_create_file_from_tabbar('note')
            self.note_page.input_note_title(title)
            self.note_page.tap_return_button()
            self.recent_page.wait_first_file_sync_success()
        self.folder_page.open_first_file()
