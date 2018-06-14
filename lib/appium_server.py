#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""启动appium服务"""

__author__ = 'kejie'

from urllib import request
from urllib.error import URLError
from lib import utils
import time
import logging


class AppiumServer:

    @classmethod
    def _start_server(cls):
        cmd_shell = 'appium &'
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
                logging.info('appium server已正常启动')
                return
        else:
            logging.info('appium server启动超时！')
            raise RuntimeError

    @classmethod
    def run(cls):
        # logging.info('开始启动appium server')
        if cls._is_server_started():
            # logging.info('appium server正在运行中！')
            return
        else:
            cls._start_server()


if __name__ == '__main__':
    AppiumServer.run()
