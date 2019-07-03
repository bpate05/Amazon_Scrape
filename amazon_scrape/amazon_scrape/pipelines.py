import pymongo

class AmazonScrapePipeline(object):

    collection_name = 'GoPro'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('mongodb://localhost:27017/mydb'),
            mongo_db=crawler.settings.get('Amazon_DB', 'Amazon')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    # def process_item(self, item, spider):
    #     self.db[self.collection_name].insert_one(dict(item))
    #     return item

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(item)
        return item