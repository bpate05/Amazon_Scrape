import scrapy


class AmazonScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    review_id = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    stars = scrapy.Field()
    text = scrapy.Field()

