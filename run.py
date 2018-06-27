#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""用例运行入口"""

__author__ = 'kejie'

import unittest
import os
import argparse
import logging
from lib import HTMLTestRunner
from lib import get_time
from lib import send_mail
from lib import install


# 用例路径
case_path = os.path.join(os.path.abspath(os.curdir), 'testcase')

# 测试报告信息
result_path = os.path.join(os.path.abspath(os.curdir), 'result', str(get_time()))
os.mkdir(result_path)
report_title = '有道云笔记iOS用例执行报告'
desc = '有道云笔记iOS用例执行报告'
report_file = os.path.join(result_path, 'YnoteiosTestReport.html')
client_log = os.path.join(result_path, 'client.log')


def parse_args():
    parser = argparse.ArgumentParser(description='iOS app install script')
    '''
    parser.add_argument('-t', '--installType', dest="install_type", default='cover', choices=['cover', 'reinstall'],
                        help="Specify install type, cover or reinstall.")
    parser.add_argument('-d', '--device', dest="device", required=True,
                        help="Specify devices, real device or simulator.")
    '''
    parser.add_argument('-p', '--appPath', dest="app_path", help="Specify install app path.")
    args = parser.parse_args()
    return args


def run_all_case():
    logging.info('开始执行用例')
    all_case = unittest.defaultTestLoader.discover(case_path, pattern='*_test.py')
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(all_case)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename=client_log, filemode='w',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 安装笔记客户端
    app_path = parse_args().app_path
    install(app_path)
    # 执行用例
    run_all_case()
    # 发送测试报告
    send_mail(report_file)
