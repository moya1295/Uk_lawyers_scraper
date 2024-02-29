import scrapy
from uk_lawyers.items import LawyerItem
from scrapy.loader import ItemLoader

class LawyersSpider(scrapy.Spider):
    name = 'lawyers'
    allowed_domains = ['solicitors.lawsociety.org.uk']
    #start_urls = ['https://solicitors.lawsociety.org.uk/person/2/']

    def start_requests(self):
        base_url = 'https://solicitors.lawsociety.org.uk/person/'
        for i in range(1, 1001):  # Adjust range as needed
            url = f'{base_url}{i}/'
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):

        if response.status == 200:
            # Handle 200 response
            self.logger.info('Successfully fetched: %s', response.url)
            #parsing logic for a successful response goes here

            # Initiate Itemloader
            
            l = ItemLoader(LawyerItem(), response=response)

            l.add_css('Name', 'h1::text')
            l.add_css('Sra_id', 'dl.single-lines dd::text')
            l.add_css('Phone', 'dl.single-lines:nth-of-type(2) dd::text')
            l.add_css('Email', 'dd.slidingDiv a::text')
            l.add_css('Org_name', 'dd.address a::text')
            l.add_css('Org_addr', 'dd.address ::text')
            l.add_css('Position', 'dl.multi-line dd ul li::text')
            l.add_css('Date', 'span.related ::text')
            l.add_css('Area_Of_Practice', 'ul.two-cols ::text')
            l.add_value('Url', response.url)

            yield l.load_item()



        elif response.status == 403:
            # Handle 403 response (Forbidden)
            self.logger.warning('Forbidden: %s', response.url)
            # Your handling logic for a forbidden response goes here
        else:
            # Handle other response statuses
            self.logger.error('Unexpected status code: %s for URL: %s', response.status, response.url)
            # Your handling logic for other response statuses goes here

