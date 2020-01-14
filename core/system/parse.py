#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" module """
import os
from types import *

__author__ = 'calject'


class Parse(object):
    _lists = {}

    @property
    def lists(self):
        return self._lists

    def handle(self):
        pass

    def append(self, model, paths):
        if hasattr(self, '_' + model):
            for path in (paths if isinstance(paths, list) else [paths]):
                content = getattr(self, '_' + model)(path)
                self._lists[model] = ((self._lists[model] + [content]) if model in self._lists else [content])

    def _alias(self, path):
        return 'source ' + path

    def _shell(self, path):
        if os.path.isfile(path):
            with open(path, 'r') as f:
                print(f.readlines(1))
                return path

    def _python(self, path):
        return 'python ' + path

