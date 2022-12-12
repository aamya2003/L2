from replit import db
import os
import telebot

token = os.getenv("token")
bot = telebot.telebot(token)

db["users"] = {}

@bot.message_handler(commands=["start"])
def start(message):
    fullname = message.from_user.first_name + message.from_user.last_name
    username = message.from_user.username
    id = message.from_user.id
    Num = len(db["users"]) + 1
    db["users"].update(
      {
        f"user{Num}" : [fullname, username, id]
      }
    )