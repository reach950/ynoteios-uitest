#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""在iOS上安装应用"""

__author__ = 'kejie'

from lib import run_shell
from lib import parse_config
import logging


def _open_device(device_name, platform_version):
    device = '{} ({})'.format(device_name, platform_version)
    cmd_shell = 'xcrun instruments -w \"{}\"'.format(device)
    run_shell(cmd_shell)


def _install_app(app_path):
    install_shell = 'xcrun simctl install booted \"{}\"'.format(app_path)
    run_shell(install_shell)


def _uninstall_app(bundle_id):
    uninstall_shell = 'xcrun simctl uninstall booted \"{}\"'.format(bundle_id)
    run_shell(uninstall_shell)


def install(app_path):
    # app安装信息
    logging.info('开始安装app')
    install_type = parse_config('run_info', 'installType')
    device = parse_config('run_info', 'device')
    device_name = parse_config('devices', device)['deviceName']
    platform_version = parse_config('devices', device)['platformVersion']
    bundle_id = parse_config('devices', device)['bundleId']
    _open_device(device_name, platform_version)
    if app_path:
        if install_type == 'reinstall':
            _uninstall_app(bundle_id)
        _install_app(app_path)


if __name__ == '__main__':
    pass
