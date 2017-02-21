# -*-coding:utf-8-*-
import logging
from logging_conf import init_log

import os

init_log()

keys_dir = '/home/ubuntu/sawtooth/keys'
data_dir = '/home/ubuntu/sawtooth/data'
logs_dir = '/home/ubuntu/sawtooth/logs'


def list_files():
    """List files in keys_dir, data_dir, logs_dir"""

    if os.path.exists(keys_dir):
        logging.info('Find dir %s.' % keys_dir)
        for filename in os.listdir(keys_dir):
            print filename
    else:
        logging.warning('Dir %s does not exist.' % keys_dir)

    if os.path.exists(data_dir):
        logging.info('Find dir %s.' % data_dir)
        for filename in os.listdir(data_dir):
            print filename
    else:
        logging.warning('Dir %s does not exist.' % data_dir)

    if os.path.exists(logs_dir):
        logging.info('Find dir %s.' % logs_dir)
        for filename in os.listdir(logs_dir):
            print filename
    else:
        logging.warning('Dir %s does not exist.' % logs_dir)


def delete_files():
    """Delete files in keys_dir, data_dir, logs_dir"""
    pass


if __name__ == '__main__':
    list_files()
