#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" module """
import os

__author__ = 'calject'


class Folder(object):

    def __init__(self, file_path):
        self._dir = os.path.split(os.path.realpath(file_path))[0]

    @property
    def dir(self):
        return self._dir

    def file_path(self, path):
        return os.path.join(self._dir, path)
