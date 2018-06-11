#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""工具类"""

__author__ = 'kejie'

import yaml
import os
from datetime import datetime


def parse_config(file_name, key):
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    yamlpath = os.path.join(os.path.pardir, 'config', '{}.yaml'.format(file_name))
    with open(yamlpath, 'r', encoding='utf-8') as f:
        config = yaml.load(f)
    return config[key]


def get_time():
    return datetime.now().strftime("%Y%m%d%H%M%S")


if __name__ == '__main__':
    print(parse_config('account', 'mail')['password'])
