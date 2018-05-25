#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""语音速记详情页面"""

__author__ = 'kejie'

from pageobject.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class AudioPage(BasePage):

    # 播放录音按钮
    play_audio_button_loc = (MobileBy.ACCESSIBILITY_ID, 'asr play')

    # 返回列表按钮
    return_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeNavigationBar/XCUIElementTypeButton[1]')

    # 语音速记标题
    audio_title_loc = (MobileBy.CLASS_NAME, 'XCUIElementTypeTextField')

    # 检查audio_page是否显示
    def is_audio_page_display(self):
        return self.find_element(self.play_audio_button_loc)

    # 点击返回按钮
    def tap_return_button(self):
        self.tap_element(self.return_button_loc)

    # 获取语音速记标题
    def get_audio_title(self):
        return self.find_element(self.audio_title_loc).get_attribute('value')

