from pathlib import Path
import scrapy
import os
import pandas as pd
from urllib.parse import urljoin, urlparse
import time
import random 

class QuotesSpider(scrapy.Spider):

    name = "quotes"
    count_urls = 0

    def start_requests(self):
        urls = [
            'https://www.classcentral.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        #print(response.url.split("/"))

        filename = response.url.split("/")[-2] + '.html'

        href_list = response.css('a::attr(href)').extract()

        #print(href_list)

        Path(os.path.join('source','html',filename)).write_bytes(response.body)

        self.log(f'Saved file {filename}')

        self.df = pd.DataFrame(columns = ['href_path', 'full_path', 'file_name'])

        for count, url in enumerate(href_list):

            full_url = urljoin('https://www.classcentral.com/', url)

            if urlparse(full_url).netloc == 'www.classcentral.com':
                
                self.df.loc[len(self.df)] = [url, full_url, str(count)+'.html']


                #yield scrapy.Request(url=url_dom, callback=self.parse_single)
            else:

                self.df.loc[len(self.df)] = [url,url,str(count)+'.html']

        self.df.to_csv('urls_dataframe.csv')

        print(self.df)
        
        for count in self.df.index:
            #print(df.loc[count]['full_path'])
            #self.count_urls = count
            yield scrapy.Request(
                url=self.df.loc[count]['full_path'],
                #method='GET',
                #formdata = {'count': str(count)},
                #html_name =df.loc[count]['file_name'],
                callback=self.parse_single,
                meta={'count': count},
            )
            time.sleep(random.uniform(2,4))
            

            #yield scrapy.Request(url=url, callback=self.parse_single)

    def parse_single(self, response):
        url = response.url#.split
        #print(response)
        #count = response.formdata['count']
        filename = self.df.loc[response.meta.get('count')]['file_name']#response.html_name
        Path(os.path.join('source','html',filename)).write_bytes(response.body)
        print(url, filename)
        #self.count_urls+=1