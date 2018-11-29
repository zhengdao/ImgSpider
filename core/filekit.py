#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
core.filekit
~~~~~~~~~~~~~~~~~~

This module define some file operation utilities.

"""

import os
import urllib
import sys
import conf

import threading.Thread as Thread


class FileDownloader(Thread):

    def __init__(self, finfo, id):
        Thread.__init__(self)

        self.__finfo = finfo
        self.__id = id
