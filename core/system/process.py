#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" module """

__author__ = 'calject'

import core.system.output as function


class Process(object):
    _is_process = False
    maps = {'process': 'green', 'info': 'cyan', 'notice': 'yellow', 'put': 'blue', 'warning': 'red', 'error': 'red'}

    def __init__(self, is_process=False):
        self._is_process = is_process

    @property
    def is_process(self):
        return self._is_process

    @is_process.setter
    def is_process(self, value):
        self._is_process = value

    def print(self, message, model='info', head=''):
        if self._is_process:
            if model and model in self.maps:
                message = '[' + model + ']: ' + message
            function.c_print(head + message, self.maps[model] if model in self.maps else None)

    def process(self, message, head=''):
        self.print(message, 'process', head)

    def info(self, message, head):
        self.print(message, 'info', head)

    def notice(self, message, head):
        self.print(message, 'notice', head)

    def put(self, message, head):
        self.print(message, 'put', head)

    def warning(self, message, head):
        self.print(message, 'warning', head)

    def error(self, message, head):
        self.print(message, 'error', head)
