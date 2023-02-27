from translitirate import to_cyrillic, to_latin
import telebot
TOKEN = '1433487454:AAGg7v6ZhLYp-AQLlx0JbzFl6eZtVN9Tuec'
bot = telebot.TeleBot(TOKEN , parse_mode = None)



@bot.message_handler(commands = ['start'])
def send_welcome(message):
    answer = "Assalomu aleykum,Xush kelibsiz! Men Nazarov Shavkat dasturchiman"
    answer += "\nBu bot kiritgan matningizni kirilldan lotinga lotindan kirilga aylantiradi\n Matn kiriting "
    bot.reply_to(message,answer)

@bot.message_handler(func = lambda message: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        answer = to_cyrillic(msg)
    else:
        answer = to_latin(msg)        
    bot.reply_to(message,answer)
bot.polling()

matn = input('Matn kiriting : ')
if matn.isascii():
    print(to_cyrillic(matn))
else:
    print(to_latin(matn))



        