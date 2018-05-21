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

    # 创建audio按钮
    create_audio_buuton_loc = (MobileBy.ACCESSIBILITY_ID, 'newNote-asr')

    # 创建markdown按钮
    create_markdown_button_loc = (MobileBy.ACCESSIBILITY_ID, 'newNote-markdown')

    # 链接收藏按钮
    link_collect_button_loc = (MobileBy.ACCESSIBILITY_ID, 'newNote-link')

    # 上传图片按钮
    upload_pic_button_loc = (MobileBy.ACCESSIBILITY_ID, 'newNote-upload')

    # 创建手写笔记按钮
    create_handwrite_button_loc = (MobileBy.ACCESSIBILITY_ID, 'newNote-handwrite')


class TabBar:
    """
    底部的tabbar模块
    """

    # tabbar的创建按钮
    create_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTabBar/XCUIElementTypeOther'
                                                   '/**/XCUIElementTypeButton[3]')

    # 最新
    recent_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTabBar/XCUIElementTypeOther'
                                                   '/**/XCUIElementTypeButton[1]')

    # 文件夹
    folder_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTabBar/XCUIElementTypeOther'
                                                   '/**/XCUIElementTypeButton[2]')

    # 收藏
    collect_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTabBar/XCUIElementTypeOther'
                                                    '/**/XCUIElementTypeButton[4]')

    # 我的
    mine_button_loc = (MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTabBar/XCUIElementTypeOther'
                                                 '/**/XCUIElementTypeButton[5]')


class MultiOperationList:
    """
    文件的更多操作列表
    """

    # 操作列表中的删除按钮
    delete_button_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeStaticText" AND name == "删除"')

    # 点击删除后的提示中的删除按钮
    sheet_delete_button_loc = (MobileBy.IOS_PREDICATE, 'type == "XCUIElementTypeButton" AND name == "删除"')
