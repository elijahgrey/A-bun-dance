import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(bot, update):
    update.effective_message.reply_text("Sup bruh")


def hello(bot, update):
    chatid = update.message.chat.id
    string = update.effective_message.text
    if string.upper() == "HI":
        bot.sendMessage(chat_id=update.message.chat_id, text='Sup '+update.message.from_user.first_name)
    if string.upper()[:3] == "HI ":
        bot.sendMessage(chat_id=update.message.chat_id, text='Sup '+update.message.from_user.first_name)
        
def who(bot, update):
    if update.effective_message.text.lower() == "who":
        bot.sendMessage("VoilÃ ! In view, a humble vaudevillian veteran, cast vicariously as both victim and villain by the vicissitudes of Fate. This visage, no mere veneer of vanity, is a vestige of the vox populi, now vacant, vanished. However, this valorous visitation of a by-gone vexation, stands vivified, and has vowed to vanquish these venal and virulent vermin van-guarding vice and vouchsafing the violently vicious and voracious violation of volition. The only verdict is vengeance; a vendetta, held as a votive, not in vain, for the value and veracity of such shall one day vindicate the vigilant and the virtuous. Verily, this vichyssoise of verbiage veers most verbose, so let me simply add that it is my very good honor to meet you and you may call me V. And you would be?")
        


if __name__ == "__main__":
    # Set these variable to the appropriate values
    TOKEN = "452290636:AAHsCubD4p0sGDBfkquoqIKnY7gaPXz_9BQ"
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
