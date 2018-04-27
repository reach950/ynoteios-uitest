#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""页面公共模块"""

__author__ = 'kejie'

from appium.webdriver.common.mobileby import MobileBy


class CreateButtonsLayer:
    """
    创建按钮的浮层
    """

    # 关闭创建列表按钮
    create_close_button_loc = (MobileBy.ACCESSIBILITY_ID, 'create note close')

    # 创建笔记按钮
    create_note_buuton_loc = (MobileBy.ACCESSIBILITY_ID, 'newNote-note')


class TabBar:
    """
    底部的tabbar模块
    """

    # tabbar的创建按钮
    create_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTabBar/**/XCUIElementTypeButton[3]')
