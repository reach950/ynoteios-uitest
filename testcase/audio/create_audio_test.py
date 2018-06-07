#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试创建语音速记"""

__author__ = 'kejie'

import unittest
from testcase import BaseCase
from time import sleep


class TestCreateAudio(BaseCase):
    """测试创建语音速记"""
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_create_audio_from_navigator(self):
        """从导航栏语音图标创建语音笔记"""
        self.recent_page.open_create_audio()
        self.record_page.start_record()
        # 获取麦克风权限
        self.record_page.accept_alert()
        # 录音3s
        sleep(3)
        self.record_page.pause_record()
        # 录音时间大于等于3s
        self.assertTrue(self.record_page.get_record_time() >= 3, '语音录制失败')
        self.record_page.complete_record()
        # 录音完成后，返回到语音速记详情页面
        self.assertTrue(self.audio_page.is_audio_page_display())
        audio_title = self.audio_page.get_audio_title()
        self.audio_page.tap_return_button()
        self.recent_page.wait_first_file_sync_success()
        self.assertTrue(self.recent_page.is_first_file_title_exist(audio_title), '语音速记创建失败')


if __name__ == '__main__':
    unittest.main()
