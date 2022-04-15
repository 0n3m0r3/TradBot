import telebot
import time


API_KEY = "5351435972:AAH7AuikFUO2mdKRAS1lvdbgj06LqzUaEbE"

bot = telebot.TeleBot(API_KEY)


def extract_link(msg):
	for text in msg:
		if 'twitter.com' in text:
			return text



@bot.message.handler(func=lambda msg: msg.text is not None and 'twitter.com' in msg.txt)
def answer(message):
	split_message = message.text.split()
	link = extract_link(split_message)

while True:
	try:
		bot.polling()
	except Exception:
		time.sleep(15)