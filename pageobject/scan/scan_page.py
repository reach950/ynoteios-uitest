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

    # scan页滑动引导
    scan_doc_tip_loc = (MobileBy.ACCESSIBILITY_ID, 'scan_doc_tip')

    # scan页引导关闭按钮
    scan_guide_close_button_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND visible == 1')

    # 检查scan_page是否显示
    def is_scan_page_display(self):
        return self.find_element(self.add_photos_button_loc)

    # 删除scan文件
    def delete_scan(self):
        self.tap_element(self.multi_operation_button_loc)
        self.tap_element(MultiOperationList.delete_button_loc)
        self.tap_element(MultiOperationList.sheet_delete_button_loc)

    # 点击返回
    def tap_return_button(self):
        self.tap_element(self.return_button_loc)

    # 获取scan文件标题
    def get_scan_title(self):
        self.tap_element(self.multi_operation_button_loc)
        title = self.find_element(MultiOperationList.file_title_loc).get_attribute('value')
        # 收起更多操作列表
        self.tap_element(self.multi_operation_button_loc, check_display=False)
        return title.split('.')[0]

    # 关闭引导
    def close_scan_guide(self):
        if self.find_element(self.scan_doc_tip_loc, check_display=False):
            self.tap_element(self.scan_guide_close_button_loc, check_display=False)
