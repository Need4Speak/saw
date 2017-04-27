# -*-coding:utf-8-*-
import shelve
import logging
import json
from logging_conf import init_log
shelf_loc = '/home/ubuntu/sawtooth/data/' # C:\Users\m\project\log\launcher-data\data
shelf_loc2 = '/project/log/launcher-data/data/'


def read_mc000_block_shelf(shelf_file):
    a_file = shelve.open(shelf_file)
    print shelf_file + ':'
    block_id = '1b77e5a45017882e'
    transaction_id = '2d6dfb735d69293d'
    print type(a_file[block_id])
    block_content = a_file[block_id].dump()
    print block_content
    block_content['TransactionIDs'] = [transaction_id]
    print block_content
    temp_block = a_file[block_id]
    temp_block.TransactionIDs = [transaction_id]
    a_file[block_id] = temp_block
    print temp_block.dump()
    print a_file[block_id].dump()
    a_file.close()


def read_mc000_txn_shelf(shelf_file):
    a_file = shelve.open(shelf_file)
    print a_file
    transaction_id_list = a_file.keys()
    logging.info('Transaction Id: ' + ', '.join(transaction_id_list))

    for each_key in transaction_id_list:
        logging.info('Transaction Id: %s, Transaction type: %s' % (each_key, type(a_file[each_key])))
        logging.info('Transaction dump: ')
        logging.info(json.dumps(a_file[each_key].dump()))

        # if 'a4145d66701da329' == each_key:
        #     temp = a_file[each_key]
        #     temp._patient_name = 'Tom'
        #     a_file['a4145d66701da329'] = temp
        # logging.info('Set transaction a4145d66701da329\'s _patient_name as Tom.')
    # print a_file.keys()
    # print type(a_file['12d806a88ce55c95'])
    # print a_file['12d806a88ce55c95']
    # print a_file['12d806a88ce55c95'].dump()
    a_file.close()

def read_shelf(shelf_file):
    logging.info('Read shelf: ' + shelf_file)
    a_file = shelve.open(shelf_file)
    print a_file

def read_txn_shelf(shelf_file):
    logging.info('Read shelf: ' + shelf_file)
    a_file = shelve.open(shelf_file)
    print a_file

    transaction_id_list = a_file.keys()
    logging.info('Transaction Id: ' + ', '.join(transaction_id_list))

    for each_key in transaction_id_list:
        logging.info('Transaction Id: %s, Transaction type: %s' % (each_key, type(a_file[each_key])))
        logging.info('Transaction dump: ')
        logging.info(json.dumps(a_file[each_key].dump()))


def read_block_shelf(shelf_file):
    logging.info('Read shelf: ' + shelf_file)
    a_file = shelve.open(shelf_file)
    print a_file

    block_id_list = a_file.keys()
    logging.info('Block_ Id: ' + ', '.join(block_id_list))

    for each_key in block_id_list:
        logging.info('Block Id: %s, Block type: %s' % (each_key, type(a_file[each_key])))
        logging.info('Block dump: ')
        logging.info(json.dumps(a_file[each_key].dump()))


def modify_txn_shelf(shelf_file, txn_id):
    logging.info('Read shelf: ' + shelf_file)
    a_file = shelve.open(shelf_file)
    print a_file

    transaction_id_list = a_file.keys()
    logging.info('Transaction Id: ' + ', '.join(transaction_id_list))

    for each_key in transaction_id_list:
        # logging.info('Transaction Id: %s, Transaction type: %s' % (each_key, type(a_file[each_key])))
        # logging.info('Transaction dump: ')
        # logging.info(json.dumps(a_file[each_key].dump()))

        if txn_id == each_key:
            temp = a_file[each_key]
            temp._patient_name = 'Tom'
            a_file[txn_id] = temp
            logging.info('Set transaction %s\'s _patient_name as Tom.' % txn_id)

    a_file.close()


def modify_shelf(shelf_file):
    a_file = shelve.open(shelf_file)
    a_file['MostRecentBlockID'] = 'dffdf26a4491f323'


if __name__ == '__main__':
    init_log()
    # shelf_files = ['mc000_block.shelf', 'mc000_chain.shelf', 'mc000_local.shelf', 'mc000_txn.shelf']

    ''' 1. Read mc000_block.shelf '''
    # read_mc000_block_shelf(shelf_loc + 'mc000_block.shelf')

    ''' 2. Read mc000_txn.shelf '''
    read_txn_shelf(shelf_loc2 + 'validator-001_txn.shelf')
    # modify_txn_shelf(shelf_loc2 + 'validator-000_txn.shelf', "fa6f8b7a09442c21")
    # modify_shelf(shelf_loc + 'mc000_chain.shelf')
    # read_shelf(shelf_loc + 'mc000_chain.shelf')
