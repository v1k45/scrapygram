import requests
import scrapy


class EchoSpider(scrapy.Spider):
    name = "echo"
    start_urls = [
        "http://localhost:5000/echo"
    ]
    chat_id = None

    def __init__(self, chat_id=None, *args, **kwargs):
        super(EchoSpider, self).__init__(*args, **kwargs)
        self.chat_id = chat_id

    def parse(self, response):
        return {"text": response.text}
