# -*-coding:utf-8-*-
# 导入socket库:
import socket
import urllib2
import json


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


def get_block_id_list():

    block_id_list = json.loads(urllib2_conn(url_block + "?" + encode))  # block_id_list's type is list.
    return block_id_list


def get_block_chain(block_id_list, log_file='./block_chain.txt'):
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

encode = "p=1"
url_store = "store"
url_block = "block"
url_transaction = "transaction"

if __name__ == '__main__':
    """
        If the response is encoded using JSON,
        the response can be “pretty printed” by adding a “p” parameter to the URL.
    """

    get_block_chain(get_block_id_list())



