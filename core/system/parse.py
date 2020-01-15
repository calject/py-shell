#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" module """
import os

__author__ = 'calject'


class Parse(object):

    def __init__(self, process, *path):
        self._process = process
        self._home = os.path.join(*path)
        self._lists = {}

    @property
    def lists(self):
        return self._lists

    def handle(self, source_path):
        source_content = []
        for model, data in self._lists.items():
            model_source_path = os.path.join(self._home, model + '.source')
            with open(model_source_path, 'w') as f:
                f.write("\n".join(data))
            source_content.append("source " + model_source_path)
        with open(source_path, 'w') as f:
            f.write("\n".join(source_content))

    def append(self, model, paths):
        if hasattr(self, '_' + model):
            for path in (paths if isinstance(paths, list) else [paths]):
                content = getattr(self, '_' + model)(path)
                self._lists[model] = ((self._lists[model] + [content]) if model in self._lists else [content])

    def _shell(self, path):
        if os.path.isfile(path):
            command = os.path.basename(os.path.splitext(path)[0])
            with open(path, 'r') as f:
                text = f.readline()
                if text != "\n":
                    command_run = text.replace('#!', '').replace('\n', '') + ' ' + path
                else:
                    command_run = "/bin/bash " + path
            return 'alias ' + command + "='" + command_run + "'"

    def _python(self, path):
        if os.path.isfile(path):
            command = os.path.basename(os.path.splitext(path)[0])
            return 'alias ' + command + "='" + 'python ' + path + "'"

    def _alias(self, path):
        return 'source ' + path

    def _export(self, path):
        return 'source ' + path

    def _func(self, path):
        return 'source ' + path

    def _fpath(self, path):
        pass
