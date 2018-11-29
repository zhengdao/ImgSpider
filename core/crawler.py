#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
core.crawler
~~~~~~~~~~~~~~~~~~

This module define the web crawler to crawl and captch the specified
resources from the given page sources and then store results to the
specified path.

"""
from io import StringIO
from PIL import Image

from BeautifulSoup import BeautifulSoup as BS4
from core.bean.resource import ResourceDef


class Downloader:

    def __init__(self, src):
        pass


class Parser:

    def __init__(self):
        pass


class Crawler:

    def __init__(self, resdef):
        self.resdef = resdef


class ImageCrawler(Crawler):

    def __init__(self, resdef):
        Crawler.__init__(resdef)

    def get_size(self, ):
        pass
