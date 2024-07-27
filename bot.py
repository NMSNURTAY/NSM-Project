import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '7475079631:AAE0zKnCmTQnj5ZUNDqfWLdvN1wf8oUombU'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}')


@bot.message_handler(commands=['site'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Open Web App", url="http://127.0.0.1:5000/")
    markup.add(button)
    bot.send_message(message.chat.id, "Click the button to open the web app:", reply_markup=markup)


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>I can help you create and manage Telegram bots.</b> If you are new to the Bot API', parse_mode='html')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

bot.polling(non_stop=True) 


