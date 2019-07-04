"""Define spiders for GoPro"""
import scrapy
from amazon_scrape.items import AmazonScrapeItem
from datetime import datetime

class GoproSpider(scrapy.Spider):
    """GoPro Spider class"""
    name = 'GoProReviews'
    # indicates the next page number to be scraped
    page_number = 2
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews&pageNumber=1']

    def parse(self, response):
        """Obtains identified objects from start_url"""
        items = AmazonScrapeItem()

        # paths to each of the elements to be scraped
        ids = response.xpath("//div[@data-hook='review']/@id").getall()
        titles = response.xpath("//a[@class='a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold']/span/text()").getall()
        dates = response.xpath("//span[@data-hook='review-date']/text()").getall()
        stars = response.xpath("//i[@data-hook='review-star-rating']/span[@class='a-icon-alt']/text()").getall()
        text = response.xpath("//span[@data-hook='review-body']/span/text()").getall()

        # from items.py
        items['review_id'] = ids
        items['title'] = titles
        items['date'] = dates
        items['stars'] = stars
        items['text'] = text            
        
        # zips content together and yields a dictionary
        for ids, title, date, star, text in zip(items['review_id'], items['title'], 
            items['date'], items['stars'], items['text']):
            star = float(star[0:2])
            formats = "%B %d, %Y"
            date = date.lower()
            date = datetime.strptime(date, formats).strftime("%m/%d/%Y")
            yield {
                'review_id': ids.strip(),
                'title': title.strip(),
                'review_date': date.strip(),
                'stars': star,
                'text': text.strip()
            }
        
        # next page to be scraped
        next_page = 'https://www.amazon.com/GoPro-Fusion-Waterproof-Digital-Spherical/product-reviews/B0792MJLNM/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=' + str(GoproSpider.page_number)
        
        # loop through all pages of reviews
        if GoproSpider.page_number <= 8:
            # increase page number
            GoproSpider.page_number += 1
            # call back to parse, store elements on new page
            yield response.follow(next_page, callback = self.parse)

        # # from all reviews page 1

        # # annoying spaces
        # product_name = response.xpath("//a[@data-hook='product-link']/text()").get()
        # brand_name = response.xpath("//a[@class='a-size-base a-link-normal']/text()").get()
        # source = "Amazon"
        # # range
        # price_range = response.xpath("//span[@class='a-color-price arp-price']/text()").getall()
        # price_msrp = 
        # price_sale = 
        # # not available on all reviews page!
        # specs = 
        # stars_aggregate = response.xpath("//span[@data-hook='rating-out-of-text']/text()").get()
        # number_reviews = response.xpath("//span[@data-hook='total-review-count']/text()").get()

        # # from product home page

        # # lots of line breaks
        # product_name = response.xpath("//span[@id='productTitle']/text()").get()
        # brand_name = response.xpath("//a[@id='bylineInfo']/text()").get()
        # source = "Amazon"
        # price_range = ""
        # price_msrp = 
        # price_sale = 
        # # extra stuff at start and end
        # specs = response.xpath("//div[@id='productDescription']/p/text()").get()
        # # see above, fixed
        # stars_aggregate = response.xpath("//span[@class='a-icon-alt']/text()").get()
        # # in format '79 customer reviews'
        # number_reviews = response.xpath("//span[@id='acrCustomerReviewText']/text()").get()
