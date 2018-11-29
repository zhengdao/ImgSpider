#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def get_root():
    """get_root_path()

    Return the root path of current application without the ending separator.

    """
    return os.path.dirname(os.path.abspath(__file__))


def get_root_path():
    """get_root_path()

    Return the root path of current application with the ending separator.

    """
    return get_root() + os.sep


if __name__ == '__main__':
    print(get_root_path())

