from scrapy.spider import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
# LinkExtractor is as same as LxmlLinkExtractor 
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector

from dbg_spider.items import DbgSpiderItem


class windebug(CrawlSpider):
    """description of class"""

    name = 'windebug'
    allowed_domains = ['blogs.msdn.com']
    start_urls = ['http://blogs.msdn.com/b/ntdebugging/']

    rules = [ 
        Rule(LinkExtractor('/b/ntdebugging/archive/[^/][0-9/]+\.aspx$'), follow=True ),
        Rule(LinkExtractor('/b/ntdebugging/archive/[^/][0-9/]+[^/][A-Za-z0-9-]+\.aspx$'), callback='parse_article'),
        ]

    def parse_article(self, response):
        '''
        '''
        sel = Selector(response)
        item = DbgSpiderItem()
        item['name'] = response.xpath('//title/text()').extract()
        item['url'] = response.url
        contents = response.xpath('//p')
        description = ''
        # to filter out content
        for content in contents:# if content.xpath('text()').extract():
            description += str(content.xpath('text()').extract())
        item['description'] = description
        return item