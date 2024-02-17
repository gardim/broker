from pymongo import MongoClient

from src import config


class MongoManager:
    def __init__(self, config):
        self.client = MongoClient(config["URL"])
        self.db = self.client.mydatabase
        self.collection = self.db.mycollection

    def insert_document(self, document):
        result = self.collection.insert_one(document)
        return result.inserted_id

    def find_all_documents(self):
        documents = self.collection.find()
        return list(documents)


mongo_manager = MongoManager(config["MONGO_DB"])
