#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.bean.Constraint import Constraint


class ResourceDef:

    def __init__(self, name='', url='', constraint=None):
        self.name = name
        self.url = url

        self.constraint = None
        self.set_constraint(constraint)

    def set_constraint(self, constraint):
        if type(constraint) == Constraint:
            self.constraint = constraint
        elif isinstance(constraint, dict):
            self.constraint = Constraint(constraint)
        else:
            pass

    def __str__(self):
        return ''

    __repr__ = __str__

