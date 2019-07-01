# -*- coding: utf-8 -*-
import scrapy

class GoproSpider(scrapy.Spider):
    name = 'GoPro'
    allowed_domains = ['www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews']
    start_urls = ['https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews']

    def parse(self, response):
        # all working!!!
        ids = response.xpath("//div[@data-hook='review']/@id").getall()
        titles = response.xpath("//a[@class='a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold']/span/text()").getall()
        dates = response.xpath("//span[@data-hook='review-date']/text()").getall()
        stars = response.xpath("//i[@data-hook='review-star-rating']/span[@class='a-icon-alt']/text()").getall()
        stars = float(stars[0:2])
        text = response.xpath("//span[@data-hook='review-body']/span/text()").getall()

        for item in zip(ids, titles, dates, stars, text):
            scrapped_data = {
                'id': item[0],
                'title': item[1],
                'date': item[2],
                'stars': item[3],
                'text': item[4]
            }

            yield scrapped_data
