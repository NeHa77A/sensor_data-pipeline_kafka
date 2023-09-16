import pymongo
import os


import certifi
ca = certifi.where()
db_link ="mongodb+srv://Neha:<password>@cluster0.jsogkox.mongodb.net/"

class MongodbOperation:

    def __init__(self) -> None:

        #self.client = pymongo.MongoClient(os.getenv('MONGO_DB_URL'),tlsCAFile=ca)
        self.client = pymongo.MongoClient(db_link,tlsCAFile=ca)
        self.db_name="NehaDB"

    def insert_many(self,collection_name,records:list):
        self.client[self.db_name][collection_name].insert_many(records)
        

    def insert(self,collection_name,record):
        self.client[self.db_name][collection_name].insert_one(record)
        
