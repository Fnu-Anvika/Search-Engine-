from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider

class TranscriptsSpider(CrawlSpider):
    name = 'transcripts'
    allowed_domains = ['subslikescript.com']
    start_urls = ['https://subslikescript.com/movies']
    max_pages = 100  # Maximum number of pages to crawl
    max_depth = 2  # Maximum depth to crawl
    count = 0  # Counter to keep track of the number of pages crawled

    # Setting rules for the crawler
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//ul[@class='scripts-list']/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        article = response.xpath("//article[@class='main-article']")
        self.count += 1
        if self.count > self.max_pages:
            raise CloseSpider('Reached maximum number of pages')
        if response.meta['depth'] > self.max_depth:
            raise CloseSpider('Reached maximum depth')

        # Append the HTML content of the page to a single file
        with open('all_pages.html', 'ab') as f:
            f.write(response.body)
        self.log(f'Appended content to file all_pages.html')

        # Extract the data we want and then yield it
        yield {
            'title': article.xpath("./h1/text()").get(),
            'plot': article.xpath("./p/text()").get(),
            'transcript': article.xpath("./div[@class='full-script']/text()").getall(),
            'url': response.url,
        }