#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""文档注释"""

__author__ = 'kejie'

from .appium_driver import AppiumDriver
from .HTMLTestRunner import HTMLTestRunner
from .utils import get_time, parse_config, run_shell
from .send_report import send_mail
from .install_app import install
from .appium_server import AppiumServer
