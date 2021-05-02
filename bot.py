import logging
import settings
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def start_bot(update: Updater, context: CallbackContext):
    mytext = """Hello {}
    
    I'm investment bot""".format(update.message.chat.first_name)
    update.message.reply_text(mytext)

def chat(update: Updater, context: CallbackContext):
    text = update.message.text
    logging.info(text)

    update.message.reply_text(text)

def main():
    updrt = Updater(settings.TOKEN_TELEGRAM)


    updrt.dispatcher.add_handler(CommandHandler("start", start_bot))
    updrt.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updrt.start_polling()
    updrt.idle()

if __name__ == "__main__":
    logging.info('Bot started!')
    main()