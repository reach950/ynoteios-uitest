#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试创建删除文档扫描"""

__author__ = 'kejie'

import unittest
from lib import get_time
from testcase import BaseCase


class TestCreateDeleteScan(BaseCase):

    def setUp(self):
        # 生成scan标题
        self.title = u'create_scan_{}'.format(get_time())
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_create_delete_scan(self):
        self.recent_page.open_create_scan()
        # 获取摄像头权限
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
        # 删除文档扫描
        self.scan_page.delete_scan()


if __name__ == '__main__':
    unittest.main()
