#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试分享笔记"""

__author__ = 'kejie'

import unittest
import pageobject as po
from lib import AppiumDriver


class TestShareNote(unittest.TestCase):

    def setUp(self):
        # 打开Appium服务器，start server后，尝试启动被测App
        self.driver = AppiumDriver().get_driver()
        self.recent_page = po.RecentPage(self.driver)
        self.note_page = po.NotePage(self.driver)
        self.folder_page = po.FolderPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_copy_share_link(self):
        # 测试复制分享链接
        self.recent_page.switch_to_folder_page()
        self.folder_page.open_folder_by_title('note')
        self.folder_page.open_first_file()
        self.note_page.tap_share_button()
        self.note_page.copy_share_link()
        self.assertTrue(self.note_page.is_copy_share_link_success())
        self.note_page.click_alert_button('确定')


if __name__ == '__main__':
    unittest.main()
