## Setup instructions for using telegram bot along with scrapy

Install dependencies:
```
pip install -r requirements.txt
```

Run flask server:
```
export FLASK_APP=server.py
flask run
```

Run scrapyd

```
export TELEGRAM_BOT_TOKEN=abc
cd echoscraper
scrapyd
```

Deploy scraper to scrapyd
```
export TELEGRAM_BOT_TOKEN=abc
cd echoscraper
scrapyd-deploy
```

Run telegram bot
```
export TELEGRAM_BOT_TOKEN=abc
python bot.py
```

Send `/echo` command to telegram bot.
