# Need to downoload telebot module every time when you use this programm.
import telebot
from telebot import (types)
# In the beggining need to downoload library telebot or pyTelegramBotAPI. Its depends of consol, which you use.
# Firstly, need to import libraries and modules """
# Secondly, need to input Token from Botfather
bot = telebot.TeleBot('7975155989:AAFVWkVFBKaJi0rDDd7FoPh7MEt9v0-kOjk')
NEMO = {}
# Thirdly, need to open file(dataset) in the format txt
with open(r'C:\Users\Пользователь\Practice5/data/menu6.txt', encoding="utf8") as f:
    onstring = f.readlines()
# Then, need to create res {}, split dataset to keys and value. After that, keys and value write to res{}
res = {}
for i in onstring:
    k,v = i.split(':')
    v = v.strip()
    v = int(v) if v.isdigit() else v
    res[k] = v
# After set a function . Firstly, need to create objects for users(markup = types.ReplyKeyboardMarkup)# and set automatical size of keybords(resize_keyboard=True)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*res.keys())
    bot.send_message(message.chat.id, "Привет! Что вы хотите заказать?", reply_markup=markup)
# On the second step need to create buttons for users. Name of button = res.key (markup.add(*res.keys()))    markup.add(*res.keys())
# On the third step, bot send message and add buttons to user screen    bot.send_message(message.chat.id, "Привет! Что вы хотите заказать?", reply_markup=markup)
"""This paragraph of code detect keys in message of users and response user value for key. For example, person click
button "Шашлык" , function detect key "шашлык" and reply "стоит 350 рублей....". "стоит 350 рублей" is value, "шашлык"is key."""
@bot.message_handler(func=lambda message: message.text in res)
def handle_order(message):
    response = res.get(message.text)
    bot.send_message(message.chat.id, response)
# This string restart and restart bot, that bot continues to process requests
bot.polling()