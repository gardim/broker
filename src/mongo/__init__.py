from pymongo import MongoClient


class MongoDBHandler:
    def __init__(self, connection_string):
        self.client = MongoClient("localhost", 27017)
        self.db = self.client.mydatabase
        self.collection = self.db.mycollection

    def insert_document(self, document):
        result = self.collection.insert_one(document)
        return result.inserted_id

    def find_all_documents(self):
        documents = self.collection.find()
        return list(documents)


mongo_client = MongoDBHandler("mongodb://mongo:27017/")
