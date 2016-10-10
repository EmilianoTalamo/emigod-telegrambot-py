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

bot.polling(timeout=500)