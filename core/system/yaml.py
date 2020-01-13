#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" module """

__author__ = 'calject'

import yaml


class Yaml(object):

    def __init__(self, path):
        self._path = path
        self._read(path)

    def _read(self, config_path):
        with open(config_path, 'rb') as f:
            self._configs = list(yaml.safe_load_all(f.read()))[0]

    def all(self):
        return self._configs

    def get(self, key, default=None):
        return self._configs[key] if key in self._configs else default

    def has(self, key):
        return key in self._configs
