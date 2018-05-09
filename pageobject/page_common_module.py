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

    # 创建scan按钮
    create_scan_buuton_loc = (MobileBy.ACCESSIBILITY_ID, 'newNote-document')


class TabBar:
    """
    底部的tabbar模块
    """

    # tabbar的创建按钮
    create_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTabBar/**/XCUIElementTypeButton[3]')

    # 文件夹
    folder_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTabBar/**/XCUIElementTypeButton[2]')


class MultiOperationList:
    """
    文件的更多操作列表
    """

    # 操作列表中的删除按钮
    delete_button_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND name == "删除"')

    # 点击删除后的提示中的删除按钮
    sheet_delete_button_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND name == "删除"')
