from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import os


TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
updater = Updater(TOKEN)

def echo(bot, update):
    requests.post("http://localhost:6800/schedule.json",
                  {"project": "echoscraper", "spider": "echo",
                   "chat_id": update.message.chat_id})

def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't get that.")

dispatcher = updater.dispatcher
echo_handler = CommandHandler('echo', echo)
unknown_handler = MessageHandler(Filters.command, unknown)
unknown_message = MessageHandler(Filters.text, unknown)

dispatcher.add_handler(echo_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(unknown_message)

updater.start_polling()
updater.idle()
