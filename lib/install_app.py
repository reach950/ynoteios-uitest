#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""在iOS上安装应用"""

__author__ = 'kejie'

import subprocess


def run_shell(cmd_shell):
    process = subprocess.Popen(cmd_shell, shell=True)
    process.wait()
    # return_code = process.returncode
    # assert return_code == 0


def open_device(device_name, platform_version):
    device = '{} ({})'.format(device_name, platform_version)
    cmd_shell = 'xcrun instruments -w \"{}\"'.format(device)
    run_shell(cmd_shell)


def install_app(app_path):
    install_shell = 'xcrun simctl install booted \"{}\"'.format(app_path)
    run_shell(install_shell)


def uninstall_app(bundle_id):
    uninstall_shell = 'xcrun simctl uninstall booted \"{}\"'.format(bundle_id)
    run_shell(uninstall_shell)


if __name__ == '__main__':
    pass
