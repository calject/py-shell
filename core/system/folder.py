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

    def file_path(self, *path):
        return os.path.join(self._dir, *path)

    def core_path(self, *path):
        return self.file_path('core', *path)

    def tmp_path(self, *path):
        return self.core_path('template', *path)


class FolderRead(object):

    def __init__(self, def_dir):
        if not os.path.isdir(def_dir):
            raise Exception(def_dir + ' 不是一个正确的目录.')
        self._def_dir = def_dir

    def file_list(self, paths=None, suffix=None):
        paths = paths if isinstance(paths, list) else []
        suffix = list(suf.replace('*', '') for suf in (suffix if isinstance(suffix, list) else []))
        return self._read_file(paths, suffix)

    def _read_file(self, paths, suffix):
        files = []
        for tmp in (paths if isinstance(paths, list) else [paths]):
            if os.path.isdir(tmp):
                files.extend(self._read_file(list(os.path.abspath(os.path.join(tmp, d)) for d in os.listdir(tmp)), suffix))
            elif os.path.isfile(tmp):
                if os.path.splitext(tmp)[1] in suffix:
                    files.append(tmp)
            elif os.path.isdir(os.path.join(self._def_dir, tmp)):
                files.extend(self._read_file(os.path.join(self._def_dir, tmp), suffix))
        return files
