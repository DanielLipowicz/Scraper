
import pymongo
client = pymongo.MongoClient()
client = pymongo.MongoClient('92.222.68.207', 27017)
# db = client.test_database
# db = client['test-database']
# collection = db.test_collection
json ={"key_words": "SADSA","title": "Algorytm Gale´a-Shapleya i jego uogólnienie","year": "2005"}
try:
    client.server_info()  # force connection on a request as the
                          # connect=True parameter of MongoClient seems
                          # to be useless here
    print(client.database_names())
    db = client['test']
    test_collection = db['test1']
    posts = db.posts
    post_id = test_collection.insert_one(json).inserted_id
    post_id
    # client.test.test1.ReturnDocument #insert_one("{'key_words': 'SADS'}")#json)
    # pymongo.collection.Collection(db, test_collection)
    print (test_collection)
except pymongo.errors.ServerSelectionTimeoutError:
    # do whatever you need
    print(err)
