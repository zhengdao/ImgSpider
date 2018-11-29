#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import logging
import logging.handlers
import logging.config

import appenv as env
from core.util.config import Config


DEFAULT_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


def get_simple_logger():
    config = Config.getdefault()
    logconfig = config.get_log_config()

    if logconfig.get('loghandler') == 'file':
        logfile = os.path.normcase(logconfig['logfile'])
        handler = logging.handlers.RotatingFileHandler(logfile, maxBytes=20 * 1024 * 1024, backupCount=10)
    else:
        handler = logging.StreamHandler(sys.stdout)

    fmt = logging.Formatter(DEFAULT_FORMAT)
    handler.setFormatter(fmt)

    alogger = logging.getLogger(config.get_config_value('logname'))
    alogger.addHandler(handler)
    alogger.setLevel(logconfig['level'])

    return alogger


def get_advanced_logger():
    file = os.path.normcase(env.get_root() + '/conf/LogConfig.ini')
    logging.config.fileConfig(file)

    config = Config.getdefault()
    return logging.getLogger(config.get_config_value('logname'))


def getlogger():
    config = Config.getdefault()
    mode = config.get_config_value('logmode')
    if mode == 0:
        alogger = get_simple_logger()
    else:
        alogger = get_advanced_logger()

    return alogger


if __name__ == '__main__':
    logger = getlogger()
    logger.debug('Debug log.')
    logger.error('Error log.')

