#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试上传图片"""

__author__ = 'kejie'

import unittest
from testcase import BaseCase
from lib import get_time


class TestUploadPic(BaseCase):

    def setUp(self):
        self.time = int(get_time())
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_upload_pic(self):
        self.recent_page.open_create_file_from_tabbar('pic')
        # 获取相册权限
        self.recent_page.accept_alert()
        self.album_page.tap_first_photo()
        self.album_page.tap_complete_button()
        self.recent_page.wait_first_file_sync_success()
        title = self.recent_page.get_first_file_title_by_extension('jpg')
        # 获取图片标题，去除最后一位的数字编号，得到创建时间
        create_time = int(title.split('.')[0][:-1])
        # 检查新创建的图片是否是最新列表中第一个文件
        self.assertTrue(create_time > self.time, '上传图片失败')


if __name__ == '__main__':
    unittest.main()
