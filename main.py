import config as cfg
import extensions
import telebot

bot = telebot.TeleBot(cfg.token)

@bot.message_handler(commands=['start'])
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, text=cfg.welcome_mes)


@bot.message_handler(commands=['help'])
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, cfg.help)


@bot.message_handler(commands=['values'])
def echo_test(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in cfg.keys.keys:
        text = '\n'.join((text, key, ))
    bot.send_message(message.chat.id, text)


@bot.message_handler()
def main_def(message: telebot.types.Message):
    request = message.text.split()

    quote, base, answer = request
    answer = extensions.CurrencyConverter.convert(quote, base, answer)

    bot.send_message(message.chat.id, f'Цена за {base} составляет {round(answer, 2)}')


bot.polling()