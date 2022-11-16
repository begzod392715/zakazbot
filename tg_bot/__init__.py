

from telegram.ext import Updater,CallbackContext,MessageHandler,CommandHandler,ConversationHandler
from telegram import Update,replykeyboardmarkup,InlineKeyboardButton,InlineKeyboardMarkup

class Bot(Updater):
    def __init__(self):
        super().__init__("5495346600:AAHamtgSD-IyqbGT5vbwPi6V3f_kpnu7yWQ")
        self.dispatcher.add_handler(ConversationHandler(
            [
                CommandHandler("start",self.start)
            ],
            {

            },
            [
                CommandHandler("start",self.start)
            ]
        ))



        self.start_polling()
        print(
            self.bot.getMe()
        )
        self.idle()



    def start(self, update:Update, context:CallbackContext):
        update.message.reply_text("salom")


        