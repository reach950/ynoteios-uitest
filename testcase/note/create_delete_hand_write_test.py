#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试创建删除手写笔记"""

__author__ = 'kejie'

import unittest
from testcase import BaseCase
from lib import get_time


class TestCreateDeleteHandWrite(BaseCase):

    def setUp(self):
        # 生成手写笔记标题
        self.title = u'create_hand_write_{}'.format(get_time())
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_create_delete_hand_write(self):
        self.recent_page.open_create_handwrite()
        rect = self.hand_write_page.get_hand_write_zone_rect()
        self.hand_write_page.drag_from_to_for_duration(rect['x'], rect['y'], rect['x']+rect['width'],
                                                       rect['y']+rect['height'])
        self.assertEqual(self.hand_write_page.get_hand_write_images_count(), 1, '手写笔记生成图片失败')
        self.hand_write_page.input_note_title(self.title)
        self.hand_write_page.tap_complete_button()
        self.hand_write_page.tap_return_button()
        # 检查新创建的手写笔记是否是最新列表中第一个文件
        self.assertEqual(self.recent_page.get_first_file_title('hand_write'), self.title, '手写笔记创建失败')
        self.recent_page.delete_first_file(is_sync=True)


if __name__ == '__main__':
    unittest.main()
