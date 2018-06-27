#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""启动appium服务"""

__author__ = 'kejie'


import time
import logging
import argparse
import os
from urllib import request
from urllib.error import URLError
from lib import utils


def parse_args():
    parser = argparse.ArgumentParser(description='iOS app install script')
    parser.add_argument('-a', '--action', dest="action", default='start', choices=['start', 'stop'],
                        help="start or stop appium.")
    args = parser.parse_args()
    return args


class AppiumServer:

    @classmethod
    def _start_server(cls):
        appium_log_path = os.path.join(os.path.abspath(os.curdir), 'result', 'appium.log')
        cmd_shell = 'nohup appium --log-timestamp --local-timezone > {} 2>&1 &'.format(appium_log_path)
        utils.run_shell(cmd_shell)

    @classmethod
    def _stop_server(cls):
        cmd_shell = "ps -ef | grep appium | grep -v grep | awk '{print $2}' | xargs kill -9"
        utils.run_shell(cmd_shell)

    @classmethod
    def _is_server_started(cls):
        appium_server_url = utils.parse_config('run_info', 'appium_server_url')
        url = '{}/status'.format(appium_server_url)
        response = None
        try:
            response = request.urlopen(url, timeout=5)
            if str(response.getcode()).startswith("2"):
                print(response.getcode())
                return True
            else:
                return False
        except URLError:
            return False
        finally:
            if response:
                response.close()

    @classmethod
    def wait_started(cls, timeout=30.0):
        start_time = time.time()
        while time.time() - start_time < timeout:
            if cls._is_server_started():
                print('appium server已正常启动')
                return
        else:
            print('appium server启动超时！')
            raise RuntimeError

    @classmethod
    def run(cls):
        action = parse_args().action
        if action == 'start':
            print('开始启动appium server')
            cls._start_server()
        else:
            print('开始关闭appium server')
            cls._stop_server()


if __name__ == '__main__':
    AppiumServer.run()
