from sawtooth_validator.database import shelf_database
import os

def read_shelf(param_shelf_file, log_dir="./log"):

    shelfdb = shelf_database.ShelfDatabase(param_shelf_file, 'c')
    keys = shelfdb.keys()
    with open('%s/%s.txt' % (log_dir, os.path.basename(param_shelf_file)), 'w') as f:
        if len(keys) > 0:
            f.write("value type: " + str(type(shelfdb.get(keys[0]))) + "\n\n\n")

        for key in keys:
            print "key: " + key
            print "value: " + str(shelfdb.get(key))
            f.write("key: " + key + "\n")
            f.write("value: " + str(shelfdb.get(key)) + "\n\n")

if __name__ == '__main__':
    data_dir = '/home/ubuntu/sawtooth/data/'
    shelf_files = [data_dir+'mc000_chain.shelf',
                   data_dir+'mc000_block.shelf',
                   data_dir+'mc000_local.shelf',
                   data_dir+'mc000_txn.shelf']

    for shelf_file in shelf_files:
        print "shelf file: " + shelf_file
        read_shelf(shelf_file)
