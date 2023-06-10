import os

import telebot

# BOT_TOKEN = os.environ.get('BOT_TOKEN')

# log_snort = "/home/linux/bot-tele.txt"

bot = telebot.TeleBot('6056937180:AAER28G6M_ZYXL_QQarxuDONKzl875oExOo')

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message) :
    bot.reply_to(message, message.text)
    
# @bot.message_handler(commands=['block'])
# def block(ip_address) :
    
    
bot.polling()