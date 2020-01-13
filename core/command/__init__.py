#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" module """

__author__ = 'calject'

import os


def run(command):
    with os.popen(command) as f:
        return f.read().strip()
