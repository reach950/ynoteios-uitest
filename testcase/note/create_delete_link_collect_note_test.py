#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试创建删除链接收藏笔记"""

__author__ = 'kejie'

import unittest
from testcase import BaseCase


class TestCreateDeleteLinkCollectNote(BaseCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_create_delete_link_collect_note(self):
        self.recent_page.open_create_link_collect_note()
        self.recent_page.input_link('www.youdao.com')
        self.recent_page.click_alert_button('确认')
        # 检查新创建的链接收藏笔记是否是最新列表中第一个文件
        self.assertEqual(self.recent_page.get_first_file_title('note'), '有道首页', '笔记创建失败')
        self.recent_page.delete_first_file()
        # 检查链接收藏笔记是否删除
        self.assertNotEqual(self.recent_page.get_first_file_title('note'), '有道首页', '笔记删除失败')


if __name__ == '__main__':
    unittest.main()
