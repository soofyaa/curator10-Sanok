import telebot

bot = telebot.TeleBot("6821352269:AAFu2HOY9i2_LFs0ON7tgyyv3Y-4ElScnps")


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