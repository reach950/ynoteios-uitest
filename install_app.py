#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""在iOS上安装应用"""

__author__ = 'kejie'

import subprocess
import argparse


def run_shell(cmd_shell):
    process = subprocess.Popen(cmd_shell, shell=True)
    process.wait()
    # return_code = process.returncode
    # assert return_code == 0


def parse_args():
    parser = argparse.ArgumentParser(description='iOS app install script')
    parser.add_argument('-t', '--installType', dest="install_type", default='cover', choices=['cover', 'reinstall'],
                        help="Specify install type, cover or reinstall.")
    parser.add_argument('-d', '--device', dest="device", required=True,
                        help="Specify devices, real device or simulator.")
    parser.add_argument('-p', '--appPath', dest="app_path",  required=True, help="Specify install app path.")
    args = parser.parse_args()
    print("args: {}".format(args))
    return args


def open_device(device):
    cmd_shell = 'xcrun instruments -w \"{}\"'.format(device)
    run_shell(cmd_shell)


def install_app(install_type, app_path, bundle_id):
    install_shell = 'xcrun simctl install booted \"{}\"'.format(app_path)
    uninstall_shell = 'xcrun simctl uninstall booted \"{}\"'.format(bundle_id)
    if install_type == 'reinstall':
        run_shell(uninstall_shell)
    run_shell(install_shell)


def main():
    args = parse_args()
    bundle_id = 'com.youdao.note.iphone'
    open_device(args.device)
    install_app(args.install_type, args.app_path, bundle_id)


if __name__ == '__main__':
    main()
