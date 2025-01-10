import telebot
import __loging__

logger=log.Logger()
bot = telebot.TeleBot("")

if __name__ == '__main__':
    bot.infinity_polling()

