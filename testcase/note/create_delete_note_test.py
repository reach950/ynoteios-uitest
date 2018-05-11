#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试创建删除笔记"""

__author__ = 'kejie'

import unittest
from testcase import BaseCase
from lib import get_time


class TestCreateDeleteNote(BaseCase):

    def setUp(self):
        # 生成笔记标题
        self.title = u'create_textnote_{}'.format(get_time())
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_create_delete_note(self):
        self.recent_page.open_create_note()
        self.note_page.input_note_title(self.title)
        self.note_page.tap_complete_button()
        self.note_page.tap_return_button()
        # 检查新创建的笔记是否是最新列表中第一个文件
        self.assertEqual(self.recent_page.get_first_file_title('note'), self.title, '笔记创建失败')
        self.recent_page.delete_first_file()
        # 检查笔记是否删除
        self.assertNotEqual(self.recent_page.get_first_file_title('note'), self.title, '笔记删除失败')


if __name__ == '__main__':
    unittest.main()
