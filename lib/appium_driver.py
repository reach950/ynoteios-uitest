#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""初始化appium driver"""

__author__ = 'kejie'

from appium import webdriver
from lib import utils
import logging


class AppiumDriver:

    def __init__(self):
        logging.info('初始化appium driver')
        appium_server_url = utils.parse_config('run_info', 'appium_server_url')
        device = utils.parse_config('run_info', 'device')
        desired_caps = utils.parse_config('devices', device)
        self.driver = webdriver.Remote(appium_server_url, desired_caps)

    def get_driver(self):
        return self.driver
