#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
core.bean.resource
~~~~~~~~~~~~~~~~~~

This module define several resource beans for maintaining
the entity attributes.

"""

import time
import numpy.random as random

from enum import Enum, unique
from core.util.tools import Tools
from core.util.tools import JSON


@unique
class QualifierMode(Enum):
    USE_COUNTER = 0
    USE_TIMESTAMP = 1
    USE_RANDOM = 2


class ResourceDef:
    """
    core.bean.resource.ResourceDef
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The definition object for maintaining the source information of the web crawler,
    such as url etc..
    """

    QUALIFIER_COUNTER = 0

    def __init__(self, url, selector, prefix='res', qmode=0):
        self.url = url
        self.selector = selector

        # prefix of resource filename to store
        self.prefix = prefix
        # qualifier mode for building filename to store
        self.qmode = QualifierMode(qmode)

    def __str__(self):
        # Enum can't be json serialized
        def decorator(pn, pv):
            if pn == 'qmode':
                pv = pv.value

            return pv

        return JSON.stringify(Tools.obj2dict(self, decorator))

    __repr__ = __str__

    @staticmethod
    def buildfilename(resdef):
        fname = [resdef.prefix]
        qmode = resdef.qmode
        if qmode == QualifierMode.USE_COUNTER:
            ResourceDef.QUALIFIER_COUNTER = ResourceDef.QUALIFIER_COUNTER + 1
            ext = str(ResourceDef.QUALIFIER_COUNTER)
        elif qmode == QualifierMode.USE_TIMESTAMP:
            ext = time.strftime("%Y%m%d%H%M%S", time.localtime()) + random.randint(0, 99)
        else:
            ext = str(time.time()).replace('.', '')

        fname.append(ext)
        return ''.join(fname)


class ImageResDef(ResourceDef):
    """
    core.bean.resource.ImageResDef
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The definition for maintaining the source information of the image crawler.
    """

    def __init__(self, url, selector='img', prefix='Image', qmode=0):
        ResourceDef.__init__(url, selector, prefix, qmode)


if __name__ == '__main__':
    rdef = ResourceDef('http://weibo.com', 'img')
    print(rdef)

    print(ResourceDef.buildfilename(rdef))
    print(ResourceDef.buildfilename(rdef))

    dictobj = ({'url': 'http://www.baidu.com', 'selector': 'img'})
    Tools.dict2obj(dictobj, rdef)
    print(rdef)

    print(ResourceDef.buildfilename(rdef))
    print(ResourceDef.buildfilename(rdef))

