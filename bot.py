import telebot

TOKEN = "7872911668:AAE-PKfQPHwMRmFpdya7h7k5zMOLXJ76m5s"
ADMIN_USERNAME = "@raakhimovvay"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Отправьте мне имя, номер и адрес для заказа.")

@bot.message_handler(func=lambda message: True)
def forward_order(message):
    bot.send_message(message.chat.id, "Ваш заказ отправлен администратору!")
    bot.send_message(ADMIN_USERNAME, f"Новый заказ:\n\n{message.text}")

bot.polling(none_stop=True)
