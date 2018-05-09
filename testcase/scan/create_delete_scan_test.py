#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试创建删除文档扫描"""

__author__ = 'kejie'

import unittest
import pageobject as po
from lib import AppiumDriver
from lib import get_time


class TestCreateDeleteScan(unittest.TestCase):

    def setUp(self):
        # 打开Appium服务器，start server后，尝试启动被测App
        self.driver = AppiumDriver().get_driver()
        self.recent_page = po.RecentPage(self.driver)
        self.add_photos_page = po.AddPhotosPage(self.driver)
        self.preview_photos_page = po.PreviewPhotosPage(self.driver)
        self.scan_page = po.ScanPage(self.driver)
        self.album_page = po.AlbumPage(self.driver)
        self.title = u'create_scan_{}'.format(get_time())

    def tearDown(self):
        self.driver.quit()

    def test_create_delete_scan(self):
        self.recent_page.open_create_scan()
        # 获取摄像头权限
        self.add_photos_page.get_camera_album_right()
        self.add_photos_page.tap_album_button()
        # 获取相册权限
        self.add_photos_page.get_camera_album_right()
        # 完成按钮为disable状态
        self.assertFalse(self.album_page.is_complete_button_enabled())
        self.album_page.tap_first_photo()
        # 完成按钮为enable状态
        self.assertTrue(self.album_page.is_complete_button_enabled())
        self.album_page.tap_complete_button()
        self.add_photos_page.tap_complete_button()
        # 返回到文档扫描详情页面
        self.assertTrue(self.scan_page.is_scan_page_display())
        # 删除文档扫描
        self.scan_page.delete_scan()


if __name__ == '__main__':
    unittest.main()
