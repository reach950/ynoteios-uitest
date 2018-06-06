#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试创建链接收藏笔记"""

__author__ = 'kejie'

import unittest
from testcase import BaseCase


class TestCreateLinkCollectNote(BaseCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_create_link_collect_note(self):
        self.recent_page.open_create_file_from_tabbar('link_collect')
        self.recent_page.input_link('www.youdao.com')
        self.recent_page.click_alert_button('确认')
        self.recent_page.wait_first_file_sync_success()
        # 检查新创建的链接收藏笔记是否是最新列表中第一个文件
        self.assertTrue(self.recent_page.is_first_file_title_exist('有道首页'), '笔记创建失败')


if __name__ == '__main__':
    unittest.main()
