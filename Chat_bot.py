import telebot
import random
from telebot import types

# Загружаем список интересных фактов
f = open('data/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
# Загружаем список поговорок
f = open('data/thinks.txt', 'r', encoding='UTF-8')
thinks  = f.read().split('\n')
f.close()
# Создаем бота
bot = telebot.TeleBot('6285552342:AAFAdDtjz7O3QMWuFWWLhw5Ck8s8b-KZDAc')
# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Facts")
        item2=types.KeyboardButton("Sayings")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Click: \nFact for an interesting fact\nSaying for a wise quote',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт
    if message.text.strip() == 'Facts':
            answer = random.choice(facts)
    # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == 'Sayings':
            answer = random.choice(thinks)
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)
# Запускаем бота
bot.polling(none_stop=True, interval=0)