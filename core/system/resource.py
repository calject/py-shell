#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" module """
import os
import shutil
import core.system.output as output
from core.system.input import Input


__author__ = 'calject'


class Resource(object):

    def __init__(self, home, source_name):
        self._home = home
        self._source_name = source_name

    def clear(self):
        if os.path.isdir(self._home):
            if os.path.isfile(self.get_path(self._source_name)) or Input.input_check("检查" + self._home + "目录失败，是否继续删除(y/n):", False):
                shutil.rmtree(self._home)
            else:
                output.error('cancel')
        os.mkdir(self._home)

    def get_home_path(self):
        return self._home

    def get_source_path(self):
        return self.get_path(self._source_name)

    def get_dir(self, *path):
        dir_path = self.get_path(*path)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
        return dir_path

    def get_path(self, *path):
        return os.path.join(self._home, *path)
