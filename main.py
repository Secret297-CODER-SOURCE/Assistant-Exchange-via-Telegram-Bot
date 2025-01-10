import telebot
import __logging__ as log

logger=log.Logger()
bot = telebot.TeleBot("7852439023:AAHhHkQ-vli6qJhytR-zJl9FOIgWVogfk0c")
# Bot user name @name_itfriends_bot
@bot.message_handler(content_types=['text'])
def Assistant_Exchange(message):
    if message.text=="/start":
        markup=telebot.types.ReplyKeyboardMarkup(True)
        markup.add(
            telebot.types.KeyboardButton("Assistant GPT"),
            telebot.types.KeyboardButton("Working Search"),
            telebot.types.KeyboardButton("Tasks"),
            telebot.types.KeyboardButton("Planers"),
            telebot.types.KeyboardButton("Setting"),
            telebot.types.KeyboardButton("Info")
        )
        bot.send_message(message.chat.id,"Hi, I Assistant Exchange Bot\nPlace select function",reply_markup=markup)
if __name__ == '__main__':
    logger.info('Started Assistant Exchange')
    bot.infinity_polling()
