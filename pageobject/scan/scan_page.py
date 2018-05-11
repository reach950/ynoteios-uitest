#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""文档扫描页面"""

__author__ = 'kejie'

from pageobject.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy
from pageobject.page_common_module import MultiOperationList


class ScanPage(BasePage):

    # 添加照片按钮
    add_photos_button_loc = (MobileBy.ACCESSIBILITY_ID, 'scanview addscan')

    # 返回按钮
    return_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeNavigationBar/XCUIElementTypeButton[1]')

    # 更多操作列表按钮
    multi_operation_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeNavigationBar/XCUIElementTypeButton[3]')

    # 检查scan_page是否显示
    def is_scan_page_display(self):
        return self.find_element(self.add_photos_button_loc).is_displayed()

    # 删除scan文件
    def delete_scan(self):
        self.tap_element(self.multi_operation_button_loc)
        self.tap_element(MultiOperationList.delete_button_loc)
        self.tap_element(MultiOperationList.sheet_delete_button_loc)

    # 点击返回
    def tap_return_button(self):
        self.tap_element(self.return_button_loc)