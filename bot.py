import telebot
import settings
import timetable

bot = telebot.TeleBot(settings.token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
            message,
            u"Din don, sono un bot e ti avviserò  quando passa l'autobus alla fermata {0}".format(settings.nome_fermata)
            )

@bot.message_handler(commands=['time'])
def send_timetable(message):
    for reply in timetable.timetable():
        bot.reply_to(
            message,
            reply
            )

bot.polling()
