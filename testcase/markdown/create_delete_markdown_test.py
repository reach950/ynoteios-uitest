#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试创建删除markdown"""

__author__ = 'kejie'

import unittest
from testcase import BaseCase
from lib import get_time


class TestCreateDeleteMarkdown(BaseCase):

    def setUp(self):
        # 生成markdown标题
        self.title = u'create_markdown_{}'.format(get_time())
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_create_delete_markdown(self):
        self.recent_page.open_create_markdown()
        # md显示为编译状态
        self.assertTrue(self.markdown_page.is_md_edit())
        self.markdown_page.input_md_title(self.title)
        self.markdown_page.tap_preview_button()
        # md显示为预览状态
        self.assertTrue(self.markdown_page.is_md_preview())
        self.markdown_page.tap_return_button()
        # 检查新创建的markdown是否是最新列表中第一个文件
        self.assertEqual(self.recent_page.get_first_file_title('markdown'), self.title, 'markdown创建失败')
        self.recent_page.delete_first_file()


if __name__ == '__main__':
    unittest.main()
