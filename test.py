import telebot
import os

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['hi'])
def hi(message):
    bot.reply_to(message, "Hi Mommy, Hi Daddy 😊") 

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot is running!")


bot.polling(none_stop=True, timeout=123)
