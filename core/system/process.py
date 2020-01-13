#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" module """

__author__ = 'calject'

import core.system.output as function


class Process(object):
    _isProcess = False
    maps = {'process': 'green', 'info': 'cyan', 'notice': 'yellow', 'put': 'blue', 'warning': 'red', 'error': 'red'}

    @property
    def process(self):
        return self._isProcess

    @process.setter
    def process(self, value):
        self._isProcess = value

    def print(self, message, model='info'):
        if self._isProcess:
            function.c_print(message, self.maps[model] if model in self.maps else None)
