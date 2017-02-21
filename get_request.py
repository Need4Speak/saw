# -*-coding:utf-8-*-

import socket
import urllib2
import json
import logging
from logging_conf import init_log

def socket_conn():
    # 创建一个socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('127.0.0.1', 8800))
    # 发送数据:
    #s.send('GET /block HTTP/1.1\r\nHost: 127.0.0.1:8800\r\nConnection: close\r\n\r\n')
    s.send('GET /block/31695f872ececa39 HTTP/1.1\r\nHost: 127.0.0.1:8800\r\nUser-Agent: curl/7.43.0\r\nAccept: */*\r\nConnection: close\r\n\r\n')
    # 接收数据:
    buffer = []
    while True:
        # 每次最多接收1k字节:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = ''.join(buffer)
    # 关闭连接:
    s.close()

    #print data
    header, html = data.split('\r\n\r\n', 1)
    print html


def urllib2_conn(url):
    url = "http://127.0.0.1:8800/%s" % url

    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    return res


def get_store():
    """Returns a list of all of the store names of transaction families."""

    store_list = json.loads(urllib2_conn(url_store + "?" + encode))
    logging.info("The type of store_list is %s" % (type(store_list)))
    return store_list


def get_store_keys(tfname):
    """
    Get store keys by tf_name,
    returns a list of keys within tf_name.
    The “tf” is short for Transaction Family.
    """
    store_keys = json.loads(urllib2_conn(url_store + tfname + "?" + encode))
    logging.info("The type of store_keys is %s" % (type(store_keys)))
    return store_keys


def get_store_all_contents(tfname):
    """
    Returns a dump of all the keys and values within tf_name.
    """
    tf_content = urllib2_conn(url_store + tfname + r"/*" + "?" + encode)
    logging.info("The type of tf_content is %s" % (type(tf_content)))
    return tf_content


def log_tf_info(log_file='./log/transaction_families.txt'):
    """Write the transaction families info into log_file. """
    tf_list = []
    all_stores = get_store()

    for tf_name in all_stores:
        tf_list.append(get_store_all_contents(tf_name))

    with open(log_file, 'w') as f:
        f.write('\n\n'.join(tf_list))


def get_block_id_list():

    block_id_list = json.loads(urllib2_conn(url_block + "?" + encode))  # block_id_list's type is list.
    return block_id_list


def get_block_chain(block_id_list, log_file='./log/block_chain.txt'):
    """
    Return block chain as a list,
    and write the block chain content into log_file.
    """
    block_chain = []

    for each_block in block_id_list:
        block_content = urllib2_conn(url_block + "/" + each_block + "?" + encode)  # block_content's type is str.
        block_chain.append(block_content)
        # print block_content

    with open(log_file, 'w') as f:
        f.write('\n\n'.join(block_chain))

    for index in range(len(block_chain)):
        block_chain[index] = json.loads(block_chain[index])

    return block_chain


def get_transaction_id_list():
    """Returns a list of the committed transaction IDs."""
    # transaction_id_list's type is list.
    transaction_id_list = json.loads(urllib2_conn(url_transaction + "?" + encode))
    return transaction_id_list


def get_transaction_by_id(transaction_id):
    """Returns the contents of transaction transaction_id."""
    return urllib2_conn(url_transaction + r"/" + transaction_id + "?" + encode)


def log_transaction_info(log_file='./log/transactions.txt'):
    """Write the transactions' info into log_file. """
    transaction_list = []
    transaction_id_list = get_transaction_id_list()

    for transaction_id in transaction_id_list:
        transaction_list.append(get_transaction_by_id(transaction_id))

    with open(log_file, 'w') as f:
        f.write('\n\n'.join(transaction_list))



"""
    If the response is encoded using JSON,
    the response can be “pretty printed” by adding a “p” parameter to the URL.
"""
encode = "p=1"
url_store = "store"
url_block = "block"
url_transaction = "transaction"

if __name__ == '__main__':
    init_log()
    get_block_chain(get_block_id_list())

    # Test /store ...
    # all_stores = get_store()
    # print all_stores
    #
    # for tf_name in all_stores:
    #     print get_store_keys(tf_name)
    #     print get_store_all_contents(tf_name)
    log_tf_info()

    # Test /transaction
    # print get_transaction_id_list()
    # print get_transaction_by_id(u'5b901ae9572f25a4')
    log_transaction_info()


