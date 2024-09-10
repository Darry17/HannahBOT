import telebot
import json
import os

API_KEY = '7239889112:AAFTAkzrbs-a_u8o29c5FvGjHci5lsV_9IQ'
bot = telebot.TeleBot(API_KEY)

QA_FILE = "qa_data.json"

def load_qa_data():
    if os.path.exists(QA_FILE):
        with open(QA_FILE, 'r', encoding='utf-8') as f: 
            return json.load(f) 
    return {}

def save_qa_data():
    with open(QA_FILE, 'w', encoding='utf-8') as f: 
        json.dump(qa_dict, f, indent=4, ensure_ascii=False) 

qa_dict = load_qa_data()

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text.lower() 
    
    if user_input in qa_dict:
        bot.reply_to(message, qa_dict[user_input])
    else:
        msg = bot.reply_to(message, "di ko po alam sasabihin 🥺, ano po want niyong sabihin ko?")
        bot.register_next_step_handler(msg, learn_response, user_input)

def learn_response(message, question):
    answer = message.text  
    qa_dict[question] = answer  
    save_qa_data() 
    bot.reply_to(message, "Okay pooo 😊👌")

bot.polling(none_stop=True, timeout=123)
