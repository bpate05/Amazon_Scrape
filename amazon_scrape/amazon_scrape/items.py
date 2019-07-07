import scrapy


class AmazonScrapeItem(scrapy.Item):
    # items for GoProReviews spider
    review_id = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    stars = scrapy.Field()
    text = scrapy.Field()

    # items for Products spider
    product_name = scrapy.Field()
    brand_name = scrapy.Field()
    source = scrapy.Field()
    specs = scrapy.Field()
    stars_aggregate = scrapy.Field()
    number_reviews = scrapy.Field()
    url_link = scrapy.Field()
    asin = scrapy.Field()
