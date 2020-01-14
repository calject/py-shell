#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" module """

__author__ = 'calject'


class Handle(object):

    def handle(self, model, paths):
        eval('self.' + model)(paths)

