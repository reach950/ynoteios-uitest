#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试创建笔记"""

__author__ = 'kejie'

import unittest
import pageobject as po
from lib import AppiumDriver
from lib import get_time


class TestCreateNote(unittest.TestCase):

    def setUp(self):
        # 打开Appium服务器，start server后，尝试启动被测App
        self.driver = AppiumDriver().get_driver()
        self.title = u'create_textnote_{}'.format(get_time())

    def tearDown(self):
        self.driver.quit()

    def test_create_note(self):

        recent_page = po.RecentPage(self.driver)
        note_page = po.NotePage(self.driver)
        recent_page.tap_create_button()
        # 检查浮层是否显示
        self.assertTrue(recent_page.supernatant_is_display(), '未弹出创建浮层')
        recent_page.tap_create_note_button()
        note_page.input_note_title(self.title)
        note_page.tap_complete_button_loc()
        note_page.tap_return_button_loc()
        # 检查新创建的笔记是否在最新列表中显示
        self.assertEqual(recent_page.get_first_note_title(), self.title, '笔记创建失败')


if __name__ == '__main__':
    unittest.main()
