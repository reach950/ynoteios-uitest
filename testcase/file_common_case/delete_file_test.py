#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试删除文件"""

__author__ = 'kejie'

import unittest
from testcase import BaseCase
import time


class TestDeleteFile(BaseCase):
    """测试删除文件"""

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_delete_first_file_from_list(self):
        """从最新列表删除第一个文件"""
        file_number = self.recent_page.get_file_number()
        self.recent_page.delete_first_file()
        time.sleep(3)
        self.assertEqual(file_number - 1, self.recent_page.get_file_number(), '文件删除失败')


if __name__ == '__main__':
    unittest.main()
