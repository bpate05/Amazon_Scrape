# -*- coding: utf-8 -*-
import scrapy

class GoproSpider(scrapy.Spider):
    name = 'GoPro'
    allowed_domains = ['www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews']
    start_urls = ['https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews']

    def parse(self, response):
        ids =
        # working!!!
        titles = response.xpath("//a[@class='a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold']/span/text()").getall()
        # working!!!
        dates = response.xpath("//span[@data-hook='review-date']/text()").getall()
        # working!!!
        stars = response.xpath("//i[@data-hook='review-star-rating']/span[@class='a-icon-alt']/text()").getall()
        stars = float(stars[0:2])
        # working!!!
        text = response.xpath("//span[@data-hook='review-body']/span/text()").getall()
