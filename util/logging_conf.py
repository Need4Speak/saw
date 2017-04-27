# -*-coding:utf-8-*-
import logging
import sys
import os
import time


def init_log():

    if not os.path.exists('./log'):
        os.makedirs('./log')
    #cur_time = time.strftime("%Y-%m-%d--%H-%M", time.localtime())
    #logging_file = './log/' + sys.argv[0].split(r'/')[-1] + cur_time +'.log'
    logging_file = './log/' + sys.argv[0].split(r'/')[-1] + '.log'

    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=logging_file,
                    filemode='a')

    #################################################################################################
    #定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('[ %(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s ]: %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    #################################################################################################
