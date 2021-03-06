#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试创建手写笔记"""

__author__ = 'kejie'

import unittest
from testcase import BaseCase
from lib import get_time
import json


class TestCreateHandWrite(BaseCase):
    """测试创建手写笔记"""
    def setUp(self):
        # 生成手写笔记标题
        self.title = u'create_hand_write_{}'.format(get_time())
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_create_hand_write(self):
        """创建一张图片的手写笔记"""
        self.recent_page.open_create_file_from_tabbar('hand_write')
        rect = json.loads(self.hand_write_page.get_hand_write_zone_rect())
        from_x = float(rect['x'])
        from_y = float(rect['y'])
        to_x = float(rect['x'] + rect['width'])
        to_y = float(rect['y'] + rect['height'])
        self.hand_write_page.drag_from_to_for_duration(from_x, from_y, to_x, to_y)
        self.hand_write_page.input_note_title(self.title)
        self.assertTrue(self.hand_write_page.is_hand_write_image_exist(), '手写笔记生成图片失败')
        self.hand_write_page.tap_complete_button()
        self.hand_write_page.tap_return_button()
        self.recent_page.wait_first_file_sync_success()
        # 检查新创建的手写笔记是否是最新列表中第一个文件
        self.assertTrue(self.recent_page.is_first_file_title_exist(self.title), '笔记创建失败')


if __name__ == '__main__':
    unittest.main()
