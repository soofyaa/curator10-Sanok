import telebot

bot = telebot.TeleBot("6693372310:AAFaCFNlzCLc-QMEPiR8wIw7FI9VRPthmOs")


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Приветствую")


@bot.message_handler(commands=['end'])
def main(message):
    bot.send_message(message.chat.id, 'Покатствую!')


@bot.message_handler(commands=['contact'])
def main(message):
    bot.send_message(message.chat.id, 'Мой Телеграм: @sivachev')


bot.infinity_polling()