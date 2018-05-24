#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""首次打开app的介绍页面"""

__author__ = 'kejie'

from pageobject.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy
from time import sleep


class IntroPage(BasePage):

    # 第一页引导图
    first_intro_img_loc = (MobileBy.ACCESSIBILITY_ID, 'introduction_0-ip5')

    # 第二页引导图
    second_intro_img_loc = (MobileBy.ACCESSIBILITY_ID, 'introduction_1-ip5')

    # 第三页引导图
    third_intro_img_loc = (MobileBy.ACCESSIBILITY_ID, 'introduction_2-ip5')

    # 试用主题
    tryout_theme_button_loc = (MobileBy.ACCESSIBILITY_ID, '试用主题')

    # 体验新版
    use_new_edition_button_loc = (MobileBy.ACCESSIBILITY_ID, '体验新版')

    # 检查引导页是否存在
    def is_intro_page_dispaly(self):
        if self.find_element(self.first_intro_img_loc):
            return True
        else:
            return False

    # 处理引导页
    def handle_intro_page(self):
        while self.find_element(self.use_new_edition_button_loc).is_displayed():
            self.swipe('left')
            sleep(0.5)
        self.tap_element(self.use_new_edition_button_loc)
