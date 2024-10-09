conda activate my_env
pip install pytelegrambotapi
conda deactivate
import telebot
from telebot import types

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота из BotFather
bot = telebot.TeleBot('7975155989:AAFVWkVFBKaJi0rDDd7FoPh7MEt9v0-kOjk')

# Словарь с возможными заказами
with open ("Practice5/data/menu.txt", encoding='utf8') as f:
    orders = f.readlines()



@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*orders.keys())
    bot.send_message(message.chat.id, "Привет! Что вы хотите заказать?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in orders)
def handle_order(message):
    response = orders.get(message.text)
    bot.send_message(message.chat.id, response)

bot.polling()
