import telebot
import json
import os

API_KEY = '7239889112:AAFTAkzrbs-a_u8o29c5FvGjHci5lsV_9IQ'
bot = telebot.TeleBot(API_KEY)

# Path to the file that will store the questions and answers
QA_FILE = "qa_data.json"

# Function to load the question-answer pairs from the file
def load_qa_data():
    if os.path.exists(QA_FILE):
        with open(QA_FILE, 'r', encoding='utf-8') as f:  # Specify UTF-8 encoding
            return json.load(f)  # Load existing data from the file
    return {}

# Function to save the question-answer pairs to the file
def save_qa_data():
    with open(QA_FILE, 'w', encoding='utf-8') as f:  # Specify UTF-8 encoding
        json.dump(qa_dict, f, indent=4, ensure_ascii=False)  # Save the updated dictionary with proper encoding

# Load the dictionary at startup
qa_dict = load_qa_data()

# Step 1: The bot handles known commands like /hi
@bot.message_handler(commands=['hi'])
def hi(message):
    bot.reply_to(message, "Hi Mommy, Hi Daddy 😊")

# Step 2: General message handler for user questions
@bot.message_handler(func=lambda message: True)  # This will handle any message
def handle_message(message):
    user_input = message.text.lower()  # Get the message text, lowercased for easier matching
    
    # Step 3: Check if the question is already known
    if user_input in qa_dict:
        bot.reply_to(message, qa_dict[user_input])  # Respond with the known answer
    else:
        # Step 4: If the bot doesn't know the answer, ask the user for the correct response
        msg = bot.reply_to(message, "di ko po alam sasabihin 🥺, ano po want niyong sabihin ko?")
        # Step 5: Wait for the user's next message, which will be the answer
        bot.register_next_step_handler(msg, learn_response, user_input)

# Step 6: Function to store the new question-answer pair
def learn_response(message, question):
    answer = message.text  # Get the user's answer
    qa_dict[question] = answer  # Store it in the dictionary
    save_qa_data()  # Save the updated data to the file
    bot.reply_to(message, "Okay pooo 😊👌")

# Step 7: Start the bot
bot.polling(none_stop=True, timeout=123)
