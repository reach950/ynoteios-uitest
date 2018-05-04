#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试创建删除笔记"""

__author__ = 'kejie'

import unittest
import pageobject as po
from lib import AppiumDriver
from lib import get_time


class TestCreateDeleteNote(unittest.TestCase):

    def setUp(self):
        # 打开Appium服务器，start server后，尝试启动被测App
        self.driver = AppiumDriver().get_driver()
        self.title = u'create_textnote_{}'.format(get_time())
        self.recent_page = po.RecentPage(self.driver)
        self.note_page = po.NotePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_create_delete_note(self):
        self.recent_page.open_create_note()
        self.note_page.input_note_title(self.title)
        self.note_page.tap_complete_button()
        self.note_page.tap_return_button()
        # 检查新创建的笔记是否在最新列表中显示
        self.assertEqual(self.recent_page.get_first_note_title(), self.title, '笔记创建失败')
        self.recent_page.delete_first_file()
        self.assertNotEqual(self.recent_page.get_first_note_title(), self.title, '笔记删除失败')


if __name__ == '__main__':
    unittest.main()
