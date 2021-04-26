from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove


def start(update, context):
    reply_keyboard = [['/coffee', '/close'],
                      ['/site']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text('Привет! Я бот по продаже кофу ')
    update.message.reply_text("/coffee: посмотерь товар", reply_markup=markup)


def site(update, context):
    update.message.reply_text(
        "Сайт: http://127.0.0.1:5000/")


def coffee(update, context):
    update.message.reply_text('http://127.0.0.1:5000/product/12')
    update.message.reply_text("Gold Barista")

    update.message.reply_text('http://127.0.0.1:5000/product/11')
    update.message.reply_text("MacCoffee Zero")

    update.message.reply_text('http://127.0.0.1:5000/product/10')
    update.message.reply_text("Taster’s Choice")

    update.message.reply_text('http://127.0.0.1:5000/product/09')
    update.message.reply_text("Tchibo Exclusive Zero")

    update.message.reply_text('http://127.0.0.1:5000/product/08')
    update.message.reply_text("Jardin")


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def main():
    TOKEN = '1672196058:AAFpLFxhe68-6Ip9T1QOzOUFWAhuNMXeyAk'
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("coffee", coffee))
    dp.add_handler(CommandHandler("site", site))
    dp.add_handler(CommandHandler("close", close_keyboard))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
