import scrapy
from amazon_scrape.items import AmazonScrapeItem

class GoproSpider(scrapy.Spider):
    name = 'GoProReviews'
    page_number = 2
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews&pageNumber=1']

    def parse(self, response):
        items = AmazonScrapeItem()

        ids = response.xpath("//div[@data-hook='review']/@id").getall()
        titles = response.xpath("//a[@class='a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold']/span/text()").getall()
        dates = response.xpath("//span[@data-hook='review-date']/text()").getall()
        stars = response.xpath("//i[@data-hook='review-star-rating']/span[@class='a-icon-alt']/text()").getall()
        text = response.xpath("//span[@data-hook='review-body']/span/text()").getall()

        items['review_id'] = ids
        items['title'] = titles
        items['date'] = dates
        items['stars'] = stars
        items['text'] = text            
        
        for ids, title, date, star, text in zip(items['review_id'], items['title'], items['date'], items['stars'], items['text']):
            yield {
                'review_id': ids.strip(),
                'title': title.strip(),
                'review_date': date.strip(),
                'stars': star.strip(),
                'text': text.strip()
            }
        
        next_page = 'https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=' + str(GoproSpider.page_number)
        if GoproSpider.page_number <= 8:
            GoproSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse) 

        # next_relative_url = 'response.xpath("//li[@class='a-last']//@href").get()'
        # next_abs_url = response.urljoin(next_relative_url)

