import scrapy


class AmazonScrapeItem(scrapy.Item):
    review_id = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    stars = scrapy.Field()
    text = scrapy.Field()

