#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""初始化appium driver"""

__author__ = 'kejie'

from appium import webdriver
from lib import utils


class AppiumDriver:

    def __init__(self):
        device = utils.parse_config('run_info', 'device')
        desired_caps = utils.parse_config('devices', device)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def get_driver(self):
        return self.driver
