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


if __name__ == '__main__':
    unittest.main()
