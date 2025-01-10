import telebot
import __logging__ as log

logger=log.Logger()
bot = telebot.TeleBot("")

if __name__ == '__main__':
    bot.infinity_polling()
