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
        price = response.xpath("//span[@class='a-size-mini olpWrapper']/text()").get()
        # extra stuff at start and end
        specs = response.xpath("//div[@id='productDescription']/p/text()").get()
        stars_aggregate = response.xpath("//span[@class='a-icon-alt']/text()").get()
        number_reviews = response.xpath("//span[@id='acrCustomerReviewText']/text()").get()
        url_link = response.xpath("//link[@rel='canonical']/@href").get()

        # from items.py
        items['product_name'] = product_name
        items['brand_name'] = brand_name
        items['source'] = source
        items['price'] = price
        items['specs'] = specs
        items['stars_aggregate'] = stars_aggregate
        items['number_reviews'] = number_reviews
        items['url_link'] = url_link

        # extract product id using RegEx
        asin = re.findall(r"(?<=dp/)[A-Z0-9]{10}", url_link)
        asin = ''.join(asin)

        # convert string to float--stars
        stars = float(stars_aggregate[:3])

        # convert string to float--reviews
        number_reviews = float(number_reviews[:2])

        # convert string to float--price
        price = re.findall(r"[$](\d+(?:\.\d{1,2})?)", price)
        price = ''.join(price)
        price = float(price)

        yield {
            'product_name': items['product_name'].strip(),
            'brand_name': items['brand_name'].strip(),
            'source': items['source'].strip(),
            'price': price,
            'specs': items['specs'].strip(),
            'star_aggregate': stars,
            'number_reviews': number_reviews,
            'product_id': asin
        }