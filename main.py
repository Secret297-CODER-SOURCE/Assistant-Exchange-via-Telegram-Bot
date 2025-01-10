import telebot

bot = telebot.TeleBot("")

if __name__ == '__main__':
    bot.infinity_polling()