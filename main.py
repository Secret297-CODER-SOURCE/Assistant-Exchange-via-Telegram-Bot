import telebot
import logging

bot = telebot.TeleBot("")

if __name__ == '__main__':
    bot.infinity_polling()

