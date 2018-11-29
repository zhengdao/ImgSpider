#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
core.util.tools
~~~~~~~~~~~~~~~~~~

This module define several utilities.

"""

import json


class Tools:

    @staticmethod
    def obj2dict(obj: object, decorator=None):
        """Tools.obj2dict(obj)

        Convert the given obj to the dict, ignore the callable property
        and the property starting with "_".

        :param: object
        :rtype: dict
        """
        rst = {}
        isfn = callable(decorator)
        for name in dir(obj):
            value = getattr(obj, name)
            if (not name.startswith('__') and not callable(value)
                    and not name.startswith('_')):
                if isfn:
                    rst[name] = decorator(name, value)
                else:
                    rst[name] = value
        return rst

    @staticmethod
    def dict2obj(thedict: dict, obj):
        """Tools.dict2obj(thedict, obj)

        Convert the given dict as the object.
        """
        rst = {}
        if isinstance(obj, object):
            rst = obj

        rst.__dict__.update(thedict)
        return rst


class JSON:

    @staticmethod
    def stringify(obj):
        if not isinstance(obj, dict):
            obj = Tools.obj2dict(obj)

        return json.dumps(obj)

    @staticmethod
    def parse(s):
        return json.loads(s)
        

if __name__ == '__main__':
    pass

