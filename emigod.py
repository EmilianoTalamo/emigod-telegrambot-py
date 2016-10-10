import telebot
import logging
import random
import time
import os
from telebot import types
from telegram.ext import Updater

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot("TOKEN")
tb = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['bless','Bless'])
def bless(message):
    photo = open('res/emigod.webp', 'rb')
    rand = random.randint(0,7999)
    rand = int(rand/1000)
    name = message.text
    try:
        name = name.split(" ")[1]
        name = name.title()
    except IndexError:
        name = message.from_user.first_name
    if rand == 0:
        bot.send_message(message.chat.id, "Thy be blessed by Emigod, %s." %name)
    elif rand == 1:
        bot.send_message(message.chat.id, "Maymays and stickors shall be with thee, %s." %name)
    elif rand == 2:
        bot.send_message(message.chat.id, "The Lord bless you and keep you, the Lord make his stickors to shine upon you and be gracious to you, %s." %name)
    elif rand == 3:
        bot.send_message(message.chat.id, "The grace of the Lord Emigod be with your spirit, %s." %name)
    elif rand == 4:
        bot.send_message(message.chat.id, "Blessed are those who keep his stickors and seek him with all their heart, %s." %name)
    elif rand == 5:
        bot.send_message(message.chat.id, "%s, he who finds a nice meme finds what is good and receives favor from the Lord." %name)
    elif rand == 6:
        bot.send_message(message.chat.id, "Dear %s, let us not be salty with Rocket League or Dota, but with actions and in truth." %name)
    elif rand == 7:
        bot.send_message(message.chat.id, "%s, A person may think their own ways are right, but the Lord always will score on Rocket League." %name)
    else:
        bot.send_message(message.chat.id, "Beep bop boop, me rompí")
    bot.send_document(message.chat.id,photo)

@bot.message_handler(commands=['salt','Salt','SALT'])
def salt(message):
    markup = types.InlineKeyboardMarkup()
    itemuno = types.InlineKeyboardButton(text= 'Pero chupame la pija', callback_data = 'Uno')
    itemdos = types.InlineKeyboardButton(text='La concha de tu madre', callback_data = 'Dos')
    itemtres = types.InlineKeyboardButton(text='Que juego de mierda', callback_data = 'Tres')
    itemcuatro = types.InlineKeyboardButton(text='Boludo, cerrá el orto vos', callback_data = 'Cuatro')
    itemcinco = types.InlineKeyboardButton(text='Dale, fucker', callback_data = 'Cinco')
    itemseis = types.InlineKeyboardButton(text='Andá a la concha de tu madre', callback_data = 'Seis')
    markup.row(itemuno, itemdos)
    markup.row(itemtres, itemcuatro)
    markup.row(itemcinco, itemseis)
    bot.send_message(message.chat.id, "Elegí un sodio:", reply_markup=markup)
    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        if call.message:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*salando*")
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Te salás de nada man, eh.")
            if call.data == "Uno":
                audio = open('res/salt/salt1.ogg', 'rb')
                bot.send_audio(call.message.chat.id, audio)
            elif call.data == "Dos":
                audio = open('res/salt/salt2.ogg', 'rb')
                bot.send_audio(call.message.chat.id, audio)
            elif call.data == "Tres":
                audio = open('res/salt/salt3.ogg', 'rb')
                bot.send_audio(call.message.chat.id, audio)
            elif call.data == "Cuatro":
                audio = open('res/salt/salt4.ogg', 'rb')
                bot.send_audio(call.message.chat.id, audio)
            elif call.data == "Cinco":
                audio = open('res/salt/salt5.ogg', 'rb')
                bot.send_audio(call.message.chat.id, audio)
            elif call.data == "Seis":
                audio = open('res/salt/salt6.ogg', 'rb')
                bot.send_audio(call.message.chat.id, audio)

@bot.message_handler(commands=['ask','Ask'])
def ask(message):
    bot.send_message(message.chat.id, "\U0001F914")
    time.sleep(1)
    rand = random.randint(0,1)
    if rand == 0:
        bot.send_message(message.chat.id, "\U0001F914")
    rand = random.randint(0,4999)
    rand = int(rand/1000)
    if rand == 0:
        bot.send_message(message.chat.id, "Por supuesto que sí.")
    elif rand == 1:
        bot.send_message(message.chat.id, "Nah.")
    elif rand == 2:
        bot.send_message(message.chat.id, "No estoy seguro, pero es probable.")
    elif rand == 3:
        bot.send_message(message.chat.id, "Yo diría que sí.")
    elif rand == 4:
        bot.send_message(message.chat.id, "Ni ahí.")
    else:
        bot.send_message(message.chat.id, "Beep bop boop, me rompí")

@bot.message_handler(commands=['roll','Roll'])
def dice(message):
    bot.send_message(message.chat.id, "*rolling*")
    time.sleep(2)
    rand = random.randint(0,19999)
    rand = int(rand/1000)+1
    if rand == 1:
        photo = open('res/d20/1.webp', 'rb')
        bot.send_document(message.chat.id,photo)
    elif rand == 2:
        photo = open('res/d20/2.webp', 'rb')
        bot.send_document(message.chat.id,photo)
    elif rand == 3:
        photo = open('res/d20/3.webp', 'rb')
        bot.send_document(message.chat.id,photo)
    elif rand == 4:
        photo = open('res/d20/4.webp', 'rb')
        bot.send_document(message.chat.id,photo)
    elif rand == 5:
        photo = open('res/d20/5.webp', 'rb')
        bot.send_document(message.chat.id,photo)
    elif rand == 6:
        photo = open('res/d20/6.webp', 'rb')
        bot.send_document(message.chat.id,photo)
    elif rand == 7:
        photo = open('res/d20/7.webp', 'rb')
        bot.send_document(message.chat.id,photo)
    elif rand == 8:
        photo = open('res/d20/8.webp', 'rb')
        bot.send_document(message.chat.id,photo)
    elif rand == 9:
        photo = open('res/d20/9.webp', 'rb')
        bot.send_document(message.chat.id,photo)
    elif rand == 10:
        photo = open('res/d20/10.webp', 'rb')
        bot.send_document(message.chat.id,photo)
    elif rand == 11:
        photo = open('res/d20/11.webp', 'rb')
        bot.send_document(message.chat.id,photo)
    elif rand == 12:
        photo = open('res/d20/12.webp', 'rb')
        bot.send_document(message.chat.id,photo)
    elif rand == 13:
        photo = open('res/d20/13.webp', 'rb')
        bot.send_document(message.chat.id,photo)
    elif rand == 14:
        photo = open('res/d20/14.webp', 'rb')
        bot.send_document(message.chat.id,photo)
    elif rand == 15:
        photo = open('res/d20/15.webp', 'rb')
        bot.send_document(message.chat.id,photo)
    elif rand == 16:
        photo = open('res/d20/16.webp', 'rb')
        bot.send_document(message.chat.id,photo)
    elif rand == 17:
        photo = open('res/d20/17.webp', 'rb')
        bot.send_document(message.chat.id,photo)
    elif rand == 18:
        photo = open('res/d20/18.webp', 'rb')
        bot.send_document(message.chat.id,photo)
    elif rand == 19:
        photo = open('res/d20/19.webp', 'rb')
        bot.send_document(message.chat.id,photo)
    elif rand == 20:
        photo = open('res/d20/20.webp', 'rb')
        bot.send_document(message.chat.id,photo)
    else:
        bot.send_message(message.chat.id, "Beep bop boop, me rompí")

@bot.message_handler(commands=['lol', 'LOL'])
def lol(message):
    bot.send_voice(message.chat.id, "AwADAQADwwADknofAAE2uIZCD8HprAI")

@bot.message_handler(commands=['gas','Gas'])
def gas(message):
    audio = open('res/gas.ogg', 'rb')
    bot.send_audio(message.chat.id, audio)

@bot.message_handler(commands=['BLESS','ASK','ROLL'])
def caps(message):
    bot.send_message(message.chat.id, "No grites.")

@bot.message_handler(commands=['kick','Kick','KICK'])
def kick(message):
    bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=LNqMdEJNiNo")

@bot.message_handler(commands=['highfive','Highfive','HIGHFIVE'])
def highfive(message):
    bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=PIemAlwtksU&feature=youtu.be&t=10s")

@bot.message_handler(commands=['hug','Hug','HUG'])
def hug(message):
    bot.send_message(message.chat.id, "http://thenicestplaceontheinter.net/")

bot.polling(timeout=500)
