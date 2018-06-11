#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试创建文档扫描"""

__author__ = 'kejie'

import unittest
from testcase import BaseCase


class TestCreateScan(BaseCase):
    """测试创建文档扫描"""
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_create_scan_by_import_pic(self):
        """通过相册导入第一张图片"""
        self.recent_page.open_create_scan()
        # 获取摄像头权限，模拟器上没有
        self.add_photos_page.accept_alert()
        self.add_photos_page.tap_album_button()
        # 获取相册权限
        self.add_photos_page.accept_alert()
        # 完成按钮为disable状态
        self.assertFalse(self.album_page.is_complete_button_enabled())
        self.album_page.tap_first_photo()
        # 完成按钮为enable状态
        self.assertTrue(self.album_page.is_complete_button_enabled())
        self.album_page.tap_complete_button()
        self.add_photos_page.tap_complete_button()
        # 返回到文档扫描详情页面
        self.assertTrue(self.scan_page.is_scan_page_display())
        title = self.scan_page.get_scan_title()
        self.scan_page.tap_return_button()
        self.recent_page.wait_first_file_sync_success()
        # 检查新创建的文档扫描是否是最新列表中第一个文件
        self.assertTrue(self.recent_page.is_first_file_title_exist(title), 'scan创建失败')


if __name__ == '__main__':
    unittest.main()
