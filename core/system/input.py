#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" module """

__author__ = 'calject'


class Input(object):

    @staticmethod
    def input_check(prompt, default=None):
        result = input(prompt)
        if result == 'y':
            return True
        elif result == 'n':
            return False
        else:
            return default


