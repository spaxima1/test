
def get_database():
    from pymongo import MongoClient
    CONNECTION_STRING = 'mongodb://127.0.0.1:27017/'
    client = MongoClient(CONNECTION_STRING)
    return client['EnglishProfile']


__db=get_database()
__idsTable=__db['Words']

def insert(rec):    
    __idsTable.insert_one(rec)