import pymongo

client = pymongo.MongoClient()
client = pymongo.MongoClient('92.222.68.207', 27017)
json = {"key_words": "SADSA", "title": "Algorytm Gale´a-Shapleya i jego uogólnienie", "year": "2005"}


class mongoConnection:
    def __init__(self, database='test', collection='scrap1'):
        self.db = client[database]
        self.collection = self.db[collection]
        self.connection_test()

    def connection_test(self):
        try:
            client.server_info()  # force connection on a request as the
            # connect=True parameter of MongoClient seems
            # to be useless here
            print(client.database_names())
            # db = client['test']
            # test_collection = db['test1']
            # posts = db.posts
            # post_id = test_collection.insert_one(json).inserted_id

            # print (test_collection)
        except pymongo.errors.ServerSelectionTimeoutError:
            # do whatever you need
            print(err)

    def insert_one_object(self, objectJSON):
        post_id = self.collection.insert_one(objectJSON).inserted_id
        return post_id

    def insert_one_if_doesnt_exist(self, objectJSON):
        query = self.collection.find_one(objectJSON)

        if query is None:
            post_id = self.collection.insert_one(objectJSON).inserted_id
            return post_id
        else:
            print("record already exist")
            return "record already exist"

    def find_in_colection(self, find={}):
        for i in self.collection.find(find):
            print(i)
