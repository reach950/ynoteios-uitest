#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""登录测试"""

__author__ = 'kejie'

import unittest
from testcase import BaseCase
from lib import utils


class TestLogin(BaseCase):

    def setUp(self):
        super().setUp()
        self.user_id = utils.get_account('163')['userId']
        self.password = utils.get_account('163')['password']

    def tearDown(self):
        super().tearDown()

    def test_163_login(self):
        self.recent_page.switch_to_mine_page()
        self.mine_page.swipe('up')
        self.mine_page.tap_logout_button()
        self.login_page.login_by_netease_email(self.user_id, self.password)


if __name__ == '__main__':
    unittest.main()
