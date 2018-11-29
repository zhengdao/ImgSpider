#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
core.util.config
~~~~~~~~~~~~~~~~~~

This module define corresponding configuration utilities for reading
the config properties from a ".ini" file.

"""

import os
import configparser
import re
import appenv as app


class Config:

    instances = dict()

    def __init__(self, file=None):
        if isinstance(file, str):
            self.configfile = file
        else:
            self.configfile = os.path.normcase(app.get_root() + '/conf/Config.ini')

        self.config = configparser.ConfigParser()
        self.config.read(self.configfile)

    def __getconfig(self, section):
        rst = dict()

        def todict(atuple):
            pn = atuple[0]
            pv = atuple[1]
            if pn.find('path') >= 0 and isinstance(pv, str):
                pv = os.path.normcase(pv.replace('${root}', app.get_root()))
            rst[pn] = pv

        map(todict, self.config.items(section))

        return rst

    def getconfig(self, section):
        """get_config(section)

        Read config items of the specified section as a dictionary.

        :param section: str
        :return: dict
        """
        try:
            tmp = self.__getattribute__(section)
        except AttributeError:
            tmp = None

        if not isinstance(tmp, dict):
            tmp = self.__getconfig(section)
            self.__setattr__(section, tmp)

        return tmp

    def get_app_cofig(self):
        """get_app_config()

        Read and return the log configs.

        :return: dict
        """
        return self.getconfig('app')

    def get_log_config(self):
        """get_log_config()

        Read and return the log configs.

        :return: dict
        """
        return self.getconfig('log')

    def get_config_value(self, key, section='app'):
        """get_config_item(key, section)

        Read and return the config value for the given key
        under the specified section.

        :return: str
        """
        m = self.getconfig(section)
        return m.get(key)

    @staticmethod
    def getinstance(file):
        """Config.getinstance(file)

        According to the specified full path fo a config file,
        build and return a Config instance.

        :param file: str the full path of the config file
        :return: Config
        """
        inst = Config.instances.get(file)
        if not isinstance(inst, Config):
            inst = Config.instances[file] = Config(file)

        return inst

    @staticmethod
    def getdefault():
        """Config.getdefault(file)

        Return the default Config for conf/Config.ini.

        :return: Config
        """
        inst = Config.instances.get('default_config')
        if not isinstance(inst, Config):
            inst = Config.instances['default_config'] = Config()

        return inst

    @staticmethod
    def getconfigvalue(pn, section='app', file=None):
        if isinstance(file, str):
            inst = Config.getinstance(file)
        else:
            inst = Config.getdefault()

        return inst.get_config_value(pn, section)


if __name__ == '__main__':
    config = Config.getdefault()
    print(config.get_log_config())

