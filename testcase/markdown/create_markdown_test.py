#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试创建markdown"""

__author__ = 'kejie'

import unittest
from testcase import BaseCase
from lib import get_time


class TestCreateMarkdown(BaseCase):

    def setUp(self):
        # 生成markdown标题
        self.title = u'create_markdown_{}'.format(get_time())
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_create_markdown(self):
        self.recent_page.open_create_file_from_tabbar('markdown')
        # md显示为编辑状态
        self.assertTrue(self.markdown_page.is_md_edit())
        self.markdown_page.input_md_title(self.title)
        self.markdown_page.tap_preview_button()
        # md显示为预览状态
        self.assertTrue(self.markdown_page.is_md_preview())
        self.markdown_page.tap_return_button()
        self.recent_page.wait_first_file_sync_success()
        # 检查新创建的markdown是否是最新列表中第一个文件
        self.assertTrue(self.recent_page.is_first_file_title_exist(self.title), 'markdown创建失败')


if __name__ == '__main__':
    unittest.main()
