#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" module """

__author__ = 'calject'

import os
import re


class EnvSrc(object):

    def __init__(self, home, source_path):
        self._home = home
        self._source_path = source_path
        self._source_text = "source " + source_path

    def bashrc_path(self):
        return os.path.join(self._home, '.bash_profile')

    def zshrc_path(self):
        return os.path.join(self._home, '.zshrc')

    def get_shrc_path(self):
        zshrc_path = self.zshrc_path()
        bashrc_path = self.bashrc_path()
        if os.path.isfile(zshrc_path):
            if self._math_line_text(zshrc_path, 'source ~/.bash_profile|source ' + bashrc_path):
                return bashrc_path
            return zshrc_path
        else:
            return bashrc_path

    def clear(self):
        src_path = self.get_shrc_path()
        file_content = []
        with open(src_path, 'r') as f:
            for content in f:
                if not re.match(r'' + self._source_text, content):
                    file_content.append(content)
        if file_content:
            with open(src_path, 'w') as f:
                f.write(''.join(file_content))

    def write(self, force=False):
        src_path = self.get_shrc_path()
        if force or not self._math_line_text(src_path, self._source_text):
            with open(src_path, 'a') as f:
                f.write(self._source_text)

    # 查找某行内容匹配(单行)
    def _math_line_text(self, path, text):
        if os.path.isfile(path):
            with open(path) as contents:
                for line in contents:
                    if re.match(r'' + text, line):
                        return True
        return False
