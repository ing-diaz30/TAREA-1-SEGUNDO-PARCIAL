import telebot

bot = telebot.TeleBot('1812246097:AAGLAo4L48rSMC8GkTv9QoQsZQil9WCdO_Q')

@bot.message_handler(commands=['hola' ])
def hola1 (mensaje):
    bot.reply_to(mensaje, "Hola, un gusto saludarte, ¿cómo estás?")

@bot.message_handler(commands=['Nombre' ])
def Nombre (mensaje):
    bot.reply_to(mensaje, "Mi nombre es Claudia?")


@bot.message_handler(commands=['Edad' ])
def Edad (mensaje):
    bot.reply_to(mensaje, "Mi edad es 31?")


@bot.message_handler(commands=['Direccion' ])
def Direccion (mensaje):
    bot.reply_to(mensaje, "Mi direccion es Colonia Villa Ernestina, 27 calle?")




bot.polling()