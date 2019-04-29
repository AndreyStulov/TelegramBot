#!/usr/bin/env python
import telebot
from telebot.types import Message

TOKEN = '859168646:AAFnwba2odDo_9oNcIqpHbLb0MZN0peSn44'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def echo_digits(message: Message):
    bot.reply_to(message, 'I am workung')

bot.polling(timeout=60)