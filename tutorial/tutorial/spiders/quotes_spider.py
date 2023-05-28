
import scrapy
import os
from datetime import datetime
import json
from tutorial.property_data import PropertyData
from pathlib import Path


class AppraiserSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        starting_url = "https://apps.putnam-fl.com/pa/property/?type=api&parcel=42-10-27-6850-1570-0020"
        yield scrapy.Request(
            url=starting_url,
            method='GET', 
            callback=self.parse_property
        )


    def parse_property(self, response):

        html_content = response.body

        self.log_page('property_page',str(html_content) )

        property_data = PropertyData(html_content)
        property_data.log_csv()

    def log_page(self, page_name:str, stringified_page:str):
        curr_t = datetime.now()
        curr_t = curr_t.strftime("%Y-%m-%d-%H-%M-%S")
        filename = f'{curr_t} - {page_name}.html'
        path = "tutorial/logged_pages"
        fullpath = os.path.join(path, filename)

        with open(fullpath, 'w') as file:
            file.write(stringified_page)