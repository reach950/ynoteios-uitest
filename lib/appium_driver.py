#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""初始化appium driver"""

__author__ = 'kejie'

from appium import webdriver
from lib import utils


class AppiumDriver:

    def __init__(self):
        desired_caps = utils.get_device('iPhone6')
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def get_driver(self):
        return self.driver