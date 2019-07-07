"""Define spiders for products"""
import scrapy
import re
from amazon_scrape.items import AmazonScrapeItem

class ProdcutsSpider(scrapy.Spider):
    """Product Spider class"""
    name = "Products"
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/dp/B0792MJLNM/ref=cm_cr_arp_d_product_top?ie=UTF8']
    pipelines = ['second']
    collection_name = 'Products'

    def parse(self, response):
        """Obtains identified objects from start_url"""
        items = AmazonScrapeItem()

        # paths to elements
       # lots of line breaks
        product_name = response.xpath("//span[@id='productTitle']/text()").get()
        brand_name = response.xpath("//a[@id='bylineInfo']/text()").get()
        source = "Amazon"
        # price_range = ""
        # extra stuff at start and end
        specs = response.xpath("//div[@id='productDescription']/p/text()").get()
        # see above, fixed
        stars_aggregate = response.xpath("//span[@class='a-icon-alt']/text()").get()
        # in format '79 customer reviews'
        number_reviews = response.xpath("//span[@id='acrCustomerReviewText']/text()").get()
        url_link = response.xpath("//link[@rel='canonical']/@href").get()

        # from items.py
        items['product_name'] = product_name
        items['brand_name'] = brand_name
        items['source'] = source
        items['specs'] = specs
        items['stars_aggregate'] = stars_aggregate
        items['number_reviews'] = number_reviews
        items['url_link'] = url_link

        asin = re.findall(r"(?<=dp/)[A-Z0-9]{10}", url_link)
        asin = ''.join(asin)

        stars = float(stars_aggregate[:3])

        number_reviews = float(number_reviews[:2])

        yield {
            'product_name': items['product_name'].strip(),
            'brand_name': items['brand_name'].strip(),
            'source': items['source'].strip(),
            'specs': items['specs'].strip(),
            'star_aggregate': stars,
            'number_reviews': number_reviews,
            'prodcut_id': asin
        }