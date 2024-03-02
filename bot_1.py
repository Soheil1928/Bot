import telebot, requests, os

TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)


def send_data_to_server(data):
    url = 'https://doneshkar-bot.darkube.app/information/'
    res = requests.post(url, data=data)
    print(res.status_code)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    data = {'first_name': message.from_user.first_name,
            'last_name': message.from_user.last_name,
            'telegram_username': message.from_user.username,
            'telegram_id': message.chat.id}
    bot.reply_to(message, text='Welcome')
    send_data_to_server(data)


if __name__ == '__main__':
    bot.infinity_polling()