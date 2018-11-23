#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Constraint:

    def __init__(self, attrs=None):
        if isinstance(attrs, dict):
            self.attributes = dict()
        else:
            self.attributes = dict(attrs)

    def set_attr(self, key=None, value=None):
        if isinstance(key, str) and isinstance(value, str):
            self.attributes[key] = value

    def get_attr(self, key):
        val = None
        if isinstance(key, str):
            val = self.attributes[key]

        return val

    def rm_attr(self, key):
        del self.attributes[key]

    def __str__(self):
        return self.attributes.__str__()

    __repr__ = __str__


