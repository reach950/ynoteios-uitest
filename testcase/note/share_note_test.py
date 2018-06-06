#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试分享笔记"""

__author__ = 'kejie'

import unittest
from testcase import BaseCase


class TestShareNote(BaseCase):

    def setUp(self):
        super().setUp()
        self.open_note_from_note_folder()

    def tearDown(self):
        super().tearDown()

    def test_copy_share_link(self):
        # 测试复制分享链接
        self.note_page.tap_share_button()
        self.note_page.copy_share_link()
        self.assertTrue(self.note_page.is_copy_share_link_success())
        self.note_page.click_alert_button('确定')


if __name__ == '__main__':
    unittest.main()
