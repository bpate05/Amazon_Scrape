# -*- coding: utf-8 -*-
import scrapy
from amazon_scrape.items import AmazonScrapeItem

class GoproSpider(scrapy.Spider):
    name = 'GoProReviews'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/dp/B0792MJLNM/ref=sr_1_3?crid=D3C7EDM435E7&keywords=gopro+fusion&qid=1550442454&s=electronics&sprefix=GoPro+Fu%2Celectronics%2C1332&sr=1-3']

    def parse(self, response):
        items = AmazonScrapeItem()

        ids = response.xpath("//div[@data-hook='review']/@id").getall()
        titles = response.xpath("//a[@class='a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold']/span/text()").getall()
        dates = response.xpath("//span[@data-hook='review-date']/text()").getall()
        stars = response.xpath("//i[@data-hook='review-star-rating']/span[@class='a-icon-alt']/text()").getall()
        # stars = float(stars[0:2])
        text = response.xpath("//div[@class='a-expander-content reviewText review-text-content a-expander-partial-collapse-content']/span/text()").getall()
        items['review_id'] = ''.join(ids).strip()
        items['title'] = ''.join(titles).strip()
        items['date'] = ''.join(dates).strip()
        items['stars'] = ''.join(stars).strip()
        items['text'] = ''.join(text).strip()

        yield items

        # next_relative_url = 'response.xpath("//li[@class='a-last']//@href").get()'
        # next_abs_url = response.urljoin(next_relative_url)

