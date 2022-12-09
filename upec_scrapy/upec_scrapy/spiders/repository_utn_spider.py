import scrapy

class RepositorySpider(scrapy.Spider):
    name = 'repository_utn'
    start_urls = [
        'http://repositorio.utn.edu.ec/browse'
    ]
    custom_settings = {
        'FEED_URI': 'repository_utn.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        repository_page_links = response.css('td.evenRowEvenCol a')
        yield from response.follow_all(repository_page_links, self.parse_repository)
        
        pagination_link = response.css('a.pull-right')
        yield from response.follow_all(pagination_link, self.parse)
    def parse_repository(self, response):
        def extract_with_xpath(query):
            return response.xpath(query).get()

        yield {
            'title': extract_with_xpath('//table[@class="table itemDisplayTable"]/tr[1]/td[2]/text()'),
            'authors': extract_with_xpath('//table[@class="table itemDisplayTable"]/tr[2]/td[2]/text()'),
            'keywords': extract_with_xpath('//table[@class="table itemDisplayTable"]/tr[3]/td[2]/text()'),
            'date': extract_with_xpath('//table[@class="table itemDisplayTable"]/tr[4]/td[2]/text()'),
            'publisher': extract_with_xpath('//table[@class="table itemDisplayTable"]/tr[5]/td[2]/text()'),
            'citation': extract_with_xpath('//table[@class="table itemDisplayTable"]/tr[6]/td[2]/text()'),
            'abstract': extract_with_xpath('//table[@class="table itemDisplayTable"]/tr[7]/td[2]/text()'),
            'uri': extract_with_xpath('//table[@class="table itemDisplayTable"]/tr[1]/td[8]/text()'),
            'category': extract_with_xpath('//table[@class="table itemDisplayTable"]/tr[9]/td[2]/text()'),
            'file_name': extract_with_xpath('//table[@class="table panel-body"]/tr[2]/td/a/text()'),
            'file_url': extract_with_xpath('//table[@class="table panel-body"]/tr[2]/td/a/@href')
        }
