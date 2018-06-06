#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""用例运行入口"""

__author__ = 'kejie'

import unittest
import os


# 用例路径
case_path = os.path.join(os.path.abspath(os.curdir), 'testcase')


def run_all_case():
    all_case = unittest.defaultTestLoader.discover(case_path, pattern='*_test.py')
    runner = unittest.TextTestRunner()
    runner.run(all_case)


if __name__ == '__main__':
    run_all_case()
