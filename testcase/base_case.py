#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试用例的基类"""

__author__ = 'kejie'

import unittest
import pageobject as po
from lib import AppiumDriver


class BaseCase(unittest.TestCase):

    def setUp(self):
        self.driver = AppiumDriver().get_driver()
        self.recent_page = po.RecentPage(self.driver)
        self.add_photos_page = po.AddPhotosPage(self.driver)
        self.preview_photos_page = po.PreviewPhotosPage(self.driver)
        self.scan_page = po.ScanPage(self.driver)
        self.album_page = po.AlbumPage(self.driver)

    def tearDown(self):
        self.driver.quit()
