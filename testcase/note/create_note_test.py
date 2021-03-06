#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试创建笔记"""

__author__ = 'kejie'

import unittest
from testcase import BaseCase
from lib import get_time


class TestCreateNote(BaseCase):
    """测试创建笔记"""
    def setUp(self):
        # 生成笔记标题
        self.title = u'create_textnote_{}'.format(get_time())
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_create_note_with_no_content(self):
        """创建没有内容的笔记"""
        self.recent_page.open_create_file_from_tabbar('note')
        self.note_page.input_note_title(self.title)
        self.note_page.tap_return_button()
        self.recent_page.wait_first_file_sync_success()
        # 检查新创建的笔记是否是最新列表中第一个文件
        self.assertTrue(self.recent_page.is_first_file_title_exist(self.title), '笔记创建失败')


if __name__ == '__main__':
    unittest.main()
