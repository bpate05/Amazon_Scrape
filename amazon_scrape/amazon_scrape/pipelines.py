"""Builds pipeline to MongoDB"""
import pymongo

class AmazonScrapePipeline(object):
    """Pipeline for GoProReviews Spider"""
    collection_name = 'GoProReviews'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        """Store variables to paths for local MongoDB and name DB"""
        return cls(
            mongo_uri=crawler.settings.get('mongodb://localhost:27017/mydb'),
            mongo_db=crawler.settings.get('Amazon_DB', 'Amazon')
        )

    def open_spider(self, spider):
        """Opens spider and establishes connections to DB"""
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        # changes collection name based on name of spider
        if hasattr(spider, 'collection_name'):
            self.collection_name = spider.collection_name

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        """Insert items into collection"""
        self.db[self.collection_name].insert_one(item)
        return item
