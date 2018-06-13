#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""我的页面"""

__author__ = 'kejie'

from pageobject.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy
import time
import json


class MinePage(BasePage):

    # 切换账户（iPhone X）
    switch_user_button_loc = {'x': 187.5, 'y': 605.5}

    # 退出登录按钮（iPhone X）
    # logout_button_loc = (MobileBy.ACCESSIBILITY_ID, '退出登录')
    logout_button_loc = {'x': 187.5, 'y': 670.5}

    # 免流量用笔记
    free_network_flow_loc = (MobileBy.ACCESSIBILITY_ID, '免流量用笔记')

    # 退出登录
    def logout(self):
        while not json.loads(self.find_element(self.free_network_flow_loc,
                                               check_display=False).get_attribute('rect'))['y'] == 514:
            self.swipe('up')
            time.sleep(3)
        self.tap_window(self.logout_button_loc['x'], self.logout_button_loc['y'])
        self.click_alert_button('确定')
