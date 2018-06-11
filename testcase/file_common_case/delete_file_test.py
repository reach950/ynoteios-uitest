#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试删除文件"""

__author__ = 'kejie'

import unittest
from testcase import BaseCase


class TestDeleteFile(BaseCase):
    """测试删除文件"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_delete_first_file_from_list(self):
        """从最新列表删除第一个文件"""
        original_text = self.recent_page.get_first_file_first_static_text()
        self.recent_page.delete_first_file()
        self.assertEqual(original_text, self.recent_page.get_first_file_first_static_text(), '文件删除失败')


if __name__ == '__main__':
    unittest.main()
