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


class FolderRead(object):

    def __init__(self, def_dir):
        if not os.path.isdir(def_dir):
            raise Exception(def_dir + ' 不是一个正确的目录.')
        self._def_dir = def_dir

    def file_list(self, paths=None, suffix=None):
        suffix = suffix.replace('*', '') if isinstance(suffix, bytearray) else []
        paths = paths if isinstance(paths, bytearray) else []
        return (x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py')

    def _read_file(self, paths, suffix):
        files = []
        for tmp in paths:
            if os.path.isdir(tmp):
                files.extend(self._read_file(os.listdir(tmp), suffix))
            elif os.path.isfile(tmp):
                files.append(tmp)
            elif os.path.isdir(os.path.join(self._def_dir, tmp)):
                files.extend(self._read_file(os.path.join(self._def_dir, tmp), suffix))
        return files