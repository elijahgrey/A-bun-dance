import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chatid, photo=url)
    

chat_id = update.message.chat_id

def start(bot, update):
    update.effective_message.reply_text("Sup bruh")


def hello(bot, update):
    chatid = update.message.chat.id
    string = update.effective_message.text
    if string.upper() == "HI":
        bot.sendMessage(chat_id=update.message.chat_id, text='Sup '+update.message.from_user.first_name)
    if string.upper()[:3] == "HI ":
        bot.sendMessage(chat_id=update.message.chat_id, text='Sup '+update.message.from_user.first_name)
        
        
def main():
    updater = Updater('452290636:AAEAGjoxOjtyZqg8vlNeVn74yxfzi_unhUQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    # Set these variable to the appropriate values
    TOKEN = "452290636:AAEAGjoxOjtyZqg8vlNeVn74yxfzi_unhUQ"
    NAME = "testingbotsenabled"

    # Port is given by Heroku
    PORT = os.environ.get('PORT')

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Set up the Updater
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    # Add handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, hello))
    dp.add_handler(MessageHandler(Filters.text, who))
    

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()
