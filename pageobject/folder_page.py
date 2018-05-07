#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""文件夹页面"""

__author__ = 'kejie'

from pageobject.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class FolderPage(BasePage):

    # 当前目录下的第一个文件
    first_file = (MobileBy.CLASS_NAME, 'XCUIElementTypeCell')

    # 打开指定标题的文件夹
    def open_folder_by_title(self, text):
        return self.tap_element((MobileBy.ACCESSIBILITY_ID, text))

    # 打开当前目录下的第一个文件
    def open_first_file(self):
        self.tap_element(self.first_file)
