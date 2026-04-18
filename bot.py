import telebot
from dotenv import load_dotenv
import os

load_dotenv()

# Replace with your token from @BotFather

bot = telebot.TeleBot(os.getenv('TOKEN'))

# Command: /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! I'm your bot :wave:")

# Command: /help
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "Available commands:\n/start\n/help")

# Echo all messages
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, f"You said: {message.text}")

# Run bot
print("Bot is running...")
bot.infinity_polling()