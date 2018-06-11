#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""用例运行入口"""

__author__ = 'kejie'

import unittest
import os
import argparse
from lib import HTMLTestRunner
from lib import get_time
from lib import parse_config
from lib import send_mail
from lib import open_device, install_app, uninstall_app


# 用例路径
case_path = os.path.join(os.path.abspath(os.curdir), 'testcase')

# 测试报告信息
result_path = os.path.join(os.path.abspath(os.curdir), 'result', str(get_time()))
report_title = 'Example用例执行报告'
desc = '用于展示修改样式后的HTMLTestRunner'
report_file = os.path.join(result_path, 'ExampleReport.html')

# app安装信息
install_type = parse_config('run_info', 'installType')
device = parse_config('run_info', 'device')
device_name = parse_config('devices', device)['deviceName']
platform_version = parse_config('devices', device)['platformVersion']
bundle_id = parse_config('devices', device)['bundleId']


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
    all_case = unittest.defaultTestLoader.discover(case_path, pattern='*_test.py')
    os.mkdir(result_path)
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(all_case)


if __name__ == '__main__':
    open_device(device_name, platform_version)
    app_path = parse_args().app_path
    if app_path:
        if install_type == 'reinstall':
            uninstall_app(bundle_id)
        install_app(app_path)
    run_all_case()
    send_mail(report_file)
