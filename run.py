#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""用例运行入口"""

__author__ = 'kejie'

import unittest
import os
from lib import HTMLTestRunner
from lib import get_time


# 用例路径
case_path = os.path.join(os.path.abspath(os.curdir), 'testcase')
result_path = os.path.join(os.path.abspath(os.curdir), 'result', str(get_time()))
report_title = 'Example用例执行报告'
desc = '用于展示修改样式后的HTMLTestRunner'
report_file = os.path.join(result_path, 'ExampleReport.html')


def run_all_case():
    all_case = unittest.defaultTestLoader.discover(case_path, pattern='*_test.py')
    os.mkdir(result_path)
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(all_case)


if __name__ == '__main__':
    run_all_case()
