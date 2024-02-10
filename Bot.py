import time

import Bot_config
import Generator
import telebot
from telebot import types

bot = telebot.TeleBot(Bot_config.token_bot)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Nicknames", callback_data="button1"), )

    bot.send_message(message.chat.id, "Вітаю! Я бот, який створює Nicknames!", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "button1")
def button1(call):
    nick = Generator.get_nick()
    print(nick)
    for word in nick:
        bot.send_message(call.message.chat.id, text=word)

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Yeap", callback_data="button1"),
               types.InlineKeyboardButton("Nope", callback_data="button2"))
    time.sleep(2)
    bot.send_message(call.message.chat.id, text="Бажаєш ще?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "button2")
def button1(call):
    bot.send_message(call.message.chat.id, "Підтримайте автора: [card_number]")
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Nicknames", callback_data="button1"))
    bot.send_message(call.message.chat.id, text="Повертайтесь ще!!!", reply_markup=markup)


bot.polling()
