#!/usr/bin/env python
#  -*-coding:utf-8-*-

import os
import getpass
import ConfigParser
from mc_client import McClient
import logging
from colorlog import ColoredFormatter


def create_console_handler(verbose_level):
    clog = logging.StreamHandler()
    formatter = ColoredFormatter(
        "%(log_color)s[%(asctime)s %(levelname)-8s%(module)s]%(reset)s "
        "%(white)s%(message)s",
        datefmt="%H:%M:%S",
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red',
        })

    clog.setFormatter(formatter)

    if verbose_level == 0:
        clog.setLevel(logging.WARN)
    elif verbose_level == 1:
        clog.setLevel(logging.INFO)
    else:
        clog.setLevel(logging.DEBUG)

    return clog


def setup_loggers(verbose_level):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(create_console_handler(verbose_level))


def load_config():
    home = os.path.expanduser("~")
    real_user = getpass.getuser()

    config_file = os.path.join(home, ".sawtooth", "mc.cfg")
    key_dir = os.path.join(home, ".sawtooth", "keys")

    config = ConfigParser.SafeConfigParser()
    config.set('DEFAULT', 'url', 'http://localhost:8800')
    config.set('DEFAULT', 'key_dir', key_dir)
    config.set('DEFAULT', 'key_file', '%(key_dir)s/%(username)s.wif')
    config.set('DEFAULT', 'username', real_user)
    if os.path.exists(config_file):
        config.read(config_file)

    return config


def add_patient_info(param_config, patient_id, patient_name, patient_illness):

    url = param_config.get('DEFAULT', 'url')
    key_file = param_config.get('DEFAULT', 'key_file')

    client = McClient(base_url=url, keyfile=key_file)
    client.add_patient_info(patient_id=patient_id, patient_name=patient_name,
                            patient_illness=patient_illness)

    client.wait_for_commit()

if __name__ == '__main__':
    logging.info("Start commit, please wait ...")
    setup_loggers(verbose_level=0)
    arg_config = load_config()
    add_patient_info(arg_config, "001", "tom", "cancer")
    logging.info("Successfully commit ！")
