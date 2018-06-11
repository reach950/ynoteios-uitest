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
        self.user_id = utils.parse_config('account', '163')['userId']
        self.password = utils.parse_config('account', '163')['password']

    def tearDown(self):
        super().tearDown()

    def test_163_login(self):
        self.recent_page.switch_to_dest_page('mine')
        self.mine_page.logout()
        self.login_page.login_by_netease_email(self.user_id, self.password)
        self.assertTrue(self.recent_page.is_recent_page_dispaly(), '登录失败')


if __name__ == '__main__':
    unittest.main()
