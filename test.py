import telebot

API_KEY = '7239889112:AAFTAkzrbs-a_u8o29c5FvGjHci5lsV_9IQ'

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['hi'])
def hi(message):
    bot.reply_to(message, "Hi Mommy, Hi Daddy 😊") 

bot.polling()