import telebot
from telebot import types

bot = telebot.TeleBot("1851300578:AAGx6uAwVQjTqDDPy9GttzTbfZCKGlLcueQ")

# Vars
start = " welcome to our bot ! \U0001F311"
fill = "Choose a paper to start filling : "

@bot.message_handler(commands=["start"])
def send_but(message) :
	global start
	
	global markup
	markup = types.ReplyKeyboardMarkup(row_width=2)
	item1 = types.KeyboardButton("Contact us \U0001F574")
	item2 = types.KeyboardButton("See more \U0001F441")
	item3 = types.KeyboardButton("Fill \U0001F4DD")
	item4 = types.KeyboardButton(" \U0001F519 back")
	markup.row(item3)
	markup.row(item4,item2,item1)
	
	bot.send_message(message.chat.id,start,reply_markup=markup)

	
			
	
@bot.message_handler(func=lambda m : m.text == "Fill \U0001F4DD")
def send_back(message) :

                
                markup = types.ReplyKeyboardMarkup()
                item1 = types.KeyboardButton("Fill 1 paper")
                item2 = types.KeyboardButton("Fill 2 paper")
                item3 = types.KeyboardButton("Fill 3 paper")
                back = types.KeyboardButton(" \U0001F519 back")
                markup.row(item1,item2)
                markup.row(item3)
                markup.row(back)
	
	
	
                bot.send_message(message.chat.id,fill,reply_markup=markup)

	

@bot.message_handler(func=lambda m : m.text == "Fill 3 paper")
def send_back(message) :
	
	bot.send_message(message.chat.id," AL BAGARI")


@bot.message_handler(func=lambda m : m.text == "Fill 2 paper")
def send_back(message) :
	
	bot.send_message(message.chat.id," FANGARI ")


@bot.message_handler(func=lambda m : m.text == "Fill 1 paper")
def send_back(message) :
	
	bot.send_message(message.chat.id," AL BIT ")








	







	
bot.polling()



