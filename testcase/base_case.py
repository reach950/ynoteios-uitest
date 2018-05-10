#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试用例的基类"""

__author__ = 'kejie'

import unittest
import pageobject as po
from lib import AppiumDriver


class BaseCase(unittest.TestCase):

    def setUp(self):
        # 打开Appium服务器，start server后，尝试启动被测App
        self.driver = AppiumDriver().get_driver()
        # 初始化App的页面对象
        self.recent_page = po.RecentPage(self.driver)
        self.folder_page = po.FolderPage(self.driver)
        self.note_page = po.NotePage(self.driver)
        self.add_photos_page = po.AddPhotosPage(self.driver)
        self.preview_photos_page = po.PreviewPhotosPage(self.driver)
        self.scan_page = po.ScanPage(self.driver)
        self.album_page = po.AlbumPage(self.driver)

    def tearDown(self):
        self.driver.quit()
