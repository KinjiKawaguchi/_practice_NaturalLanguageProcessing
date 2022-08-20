import sqllitedatastore as datastore

if __name__ == '__main__':
    datastore.connect()
    datastore.create_table()
    datastore.close()
    