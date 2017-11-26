import requests
import os

API_KEY_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]


class EchoscraperPipeline(object):
    def process_item(self, item, spider):
        res = requests.post("https://api.telegram.org/bot" + API_KEY_TOKEN + "/sendMessage",
                            {"text": item["text"], "chat_id": spider.chat_id, "parse_mode": "html"})
        return item
