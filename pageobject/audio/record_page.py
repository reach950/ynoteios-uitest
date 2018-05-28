#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""语音速记录音页面"""

__author__ = 'kejie'

from pageobject.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class RecordPage(BasePage):

    # 开始录音按钮
    record_start_button_loc = (MobileBy.ACCESSIBILITY_ID, '开始录音')

    # 暂停录音按钮
    record_pause_button_loc = (MobileBy.ACCESSIBILITY_ID, '暂停')

    # 继续录音按钮
    record_continue_button_loc = (MobileBy.ACCESSIBILITY_ID, '继续录音')

    # 完成录音按钮
    record_complete_button_loc = (MobileBy.ACCESSIBILITY_ID, '完成')

    # 录音时间的秒数
    record_time_second_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`type == "XCUIElementTypeStaticText"'
                                                        ' AND name == "秒"`]/XCUIElementTypeStaticText[3]')

    # 开始录音
    def start_record(self):
        self.tap_element(self.record_start_button_loc)

    # 暂停录音
    def pause_record(self):
        self.tap_element(self.record_pause_button_loc)

    # 完成录音
    def complete_record(self):
        self.tap_element(self.record_complete_button_loc)

    # 获取录音时间
    def get_record_time(self):
        return int(self.find_element(self.record_time_second_loc).get_attribute('value'))
