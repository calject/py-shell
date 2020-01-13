#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" module """

__author__ = 'calject'


# color - 前景色: 30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋 红）、36（青色）、37（白色）
# bg    - 背景色: 40（黑色）、41（红色）、42（绿色）、 43（黄色）、44（蓝色）、45（洋 红）、46（青色）、47（白色）
# model - 显示方式: 0（默认值）、1（高亮）、22（非粗体）、4（下划线）、24（非下划线）、 5（闪烁）、25（非闪烁）、7（反显）、27（非反显）
def c_print(message, color=None, bgColor=None, model=None):
    maps = {'black': 30, 'red': 31, 'green': 32, 'yellow': 33, 'blue': 34, 'magenta': 35, 'cyan': 36, 'white': 37}
    if isinstance(color, str):
        color = maps[color] if color in maps else 0
    if isinstance(bgColor, str):
        bgColor = maps[bgColor] + 10 if bgColor in maps else 1
    strFormat = str(model) if model else ''
    if color:
        strFormat += ';' if strFormat else ''
        strFormat += str(color)
    if bgColor and 40 <= bgColor <= 47:
        strFormat += ';' if strFormat else ''
        strFormat += str(bgColor) + 'm'
    elif strFormat:
        strFormat += ';1m'
    print('\033[' + strFormat + message + '\033[0m' if strFormat else message)


def success(message):
    c_print(message, 'green')


def failure(message):
    c_print(message, 'red')


def error(message, err_code=1):
    c_print(message, 'red')
    exit(err_code)

