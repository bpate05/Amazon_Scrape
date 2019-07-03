import scrapy
from amazon_scrape.items import AmazonScrapeItem

class GoproSpider(scrapy.Spider):
    name = 'GoProReviews'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews']

    def parse(self, response):
        item = AmazonScrapeItem()

        ids = response.xpath("//div[@data-hook='review']/@id").getall()
        titles = response.xpath("//a[@class='a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold']/span/text()").getall()
        dates = response.xpath("//span[@data-hook='review-date']/text()").getall()
        stars = response.xpath("//i[@data-hook='review-star-rating']/span[@class='a-icon-alt']/text()").getall()
        # stars = stars[0:1]
        text = response.xpath("//span[@data-hook='review-body']/span/text()").getall()
        # item['review_id'] = ''.join(ids).strip()
        # item['title'] = ''.join(titles).strip()
        # item['date'] = ''.join(dates).strip()
        # item['stars'] = ''.join(stars).strip()
        # item['text'] = ''.join(text).strip()

        item['review_id'] = ids
        item['title'] = titles
        item['date'] = dates
        item['stars'] = stars
        item['text'] = text

        for review_id, title, date, stars, text in item:
            
            yield item

        # next_relative_url = 'response.xpath("//li[@class='a-last']//@href").get()'
        # next_abs_url = response.urljoin(next_relative_url)

