#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""工具类"""

__author__ = 'kejie'

import yaml
import os
from datetime import datetime


def get_device(device_name):
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    yamlpath = os.path.join(os.path.pardir, 'config', 'devices.yaml')
    with open(yamlpath, 'r', encoding='utf-8') as f:
        devices = yaml.load(f)
    return devices[device_name]


def get_account(account_name):
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    yamlpath = os.path.join(os.path.pardir, 'config', 'account.yaml')
    with open(yamlpath, 'r', encoding='utf-8') as f:
        devices = yaml.load(f)
    return devices[account_name]


def get_time():
    return datetime.now().strftime("%Y%m%d%H%M%S")


if __name__ == '__main__':
    print(get_account('163'))
