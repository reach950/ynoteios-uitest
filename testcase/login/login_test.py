#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""登录测试"""

__author__ = 'kejie'

import unittest
from testcase import BaseCase


class TestLogin(BaseCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_163_login(self):
        self.recent_page.switch_to_mine_page()
        self.mine_page.swipe('up')
        self.mine_page.tap_logout_button()
        self.login_page.login_by_netease_email('ygroup009@163.com', 'youdao123')


if __name__ == '__main__':
    unittest.main()
