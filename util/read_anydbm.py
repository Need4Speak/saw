# -*-coding:utf-8-*-
import anydbm
import os
import logging
import sys

logging_file = sys.argv[0] + '.log'

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=logging_file,
                filemode='a')

#################################################################################################
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################

dbm_loc = '/home/ubuntu/sawtooth/data/mc000_state.dbm'


def load_data(log_file='../log/%s_content.txt' % os.path.basename(dbm_loc)):
    if os.path.exists(dbm_loc):
        logging.info('Find file %s.' % dbm_loc)
        db = anydbm.open(dbm_loc, 'r')

        with open(log_file, 'w') as f:
            for item in db.items():
                print type(item)
                print item
                f.write(str(item) + '\n')
            db.close()

    else:
        logging.warning('File %s does not exist.' % dbm_loc)

if __name__ == '__main__':
    #CreateData()
    load_data()
