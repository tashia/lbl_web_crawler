from scrapy.spider import Spider
from scrapy.selector import Selector

from dbg_spider.items import DbgSpiderItem


class windebug(Spider):
    """description of class"""

    name = 'windebug'
    #allowed_domains = ['blogs.msdn.com']
    start_urls = ['http://blogs.msdn.com/b/ntdebugging/']

    def parse(self, response):
        '''
        '''
        sel = Selector(response)
        posts = sel.xpath('//div[@class="full-post"]/')
        items = []
        for post in posts:
            item = DbgSpiderItem()
            contents = post.xpath('div[@class="post-content"]/p')
            for content in contents:# if content.xpath('text()').extract():
                item['name'] = post.xpath('h3/text()').extract()
                item['description'] = content.xpath('text()').extract()
                item['url'] = response.url
                items.append(item)
        return items