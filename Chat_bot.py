import telebot
import random
from telebot import types

# Load the list of interesting facts
f = open('data/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
# Load the list of sayings
f = open('data/thinks.txt', 'r', encoding='UTF-8')
thinks = f.read().split('\n')
f.close()
# Create a bot
bot = telebot.TeleBot('YOUR_BOT_TOKEN_HERE')  # Replace with your actual token
# start command
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Add two buttons
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Facts")
        item2 = types.KeyboardButton("Sayings")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Click: \nFact for an interesting fact\nSaying for a wise quote', reply_markup=markup)
# Receiving messages from the user
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # If the user sent 'Facts', we give them a random fact
    if message.text.strip() == 'Facts':
            answer = random.choice(facts)
    # If the user sent 'Sayings', we give them a wise thought
    elif message.text.strip() == 'Sayings':
            answer = random.choice(thinks)
    # We send the user a message back to their chat
    bot.send_message(message.chat.id, answer)
# Run the bot
bot.polling(none_stop=True, interval=0)
