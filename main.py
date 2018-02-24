# -*- coding: utf-8 -*-

import logging
from time import sleep

import telebot

from config import ADMIN, TOKEN
from remotes import NailerPI

log = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot(TOKEN, num_threads=1, skip_pending=True)

pi = NailerPI()


'''
Change text values in second column to ypur desired
'''

buttons = \
    {
        'shutdown': 'Shutdown',
        'reboot': 'Reboot',
        'temp': 'CPU Temp',
        'eth': 'eth0',
        'wlan': 'wlan0',
        'wol': 'Wake up Z400'
    }


def fixed(text):
    return '```{}```'.format(text)


def welcome(m):
    markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True, row_width=1)
    markup.row(
        buttons['shutdown'],
        buttons['reboot'],
        buttons['temp']
    )
    markup.row(
        buttons['eth'],
        buttons['wlan']
    )
    markup.row(buttons['wol'])

    bot.send_message(m.chat.id, '_Welcome!_\nUse the buttons below\nYou can also execute `bash` commands by sending them directly',
                     parse_mode='markdown', reply_to_message_id=m.message_id, reply_markup=markup)


def button_handler(chat_id, msg_text):
    if msg_text == buttons['shutdown']:
        tmp = bot.send_message(
            chat_id, '_Shutting down. . ._', parse_mode='markdown')
        for x in range(5, 0, -1):
            bot.edit_message_text('_Shutting down in {} seconds. . ._'.format(
                x), parse_mode='markdown', chat_id=tmp.chat.id, message_id=tmp.message_id)
            sleep(1)
        bot.edit_message_text('_Shutting down. . ._', parse_mode='markdown',
                              chat_id=tmp.chat.id, message_id=tmp.message_id)
        bot.send_message(chat_id, fixed(pi.shutdown()))

    elif msg_text == buttons['reboot']:
        tmp = bot.send_message(
            chat_id, '_Rebooting. . ._', parse_mode='markdown')
        for x in range(5, 0, -1):
            bot.edit_message_text('_Rebooting in {} seconds. . ._'.format(
                x), parse_mode='markdown', chat_id=tmp.chat.id, message_id=tmp.message_id)
            sleep(1)
        bot.edit_message_text('_Rebooting. . ._', parse_mode='markdown',
                              chat_id=tmp.chat.id, message_id=tmp.message_id)
        bot.send_message(chat_id, fixed(pi.reboot()))

    elif msg_text == buttons['temp']:
        bot.send_message(
            chat_id, 'Current CPU temperature is {} °C'.format(pi.cpu_temp()))

    elif msg_text == buttons['eth']:
        bot.send_message(chat_id, pi.ethernet())

    elif msg_text == buttons['wlan']:
        bot.send_message(chat_id, pi.wireless())

    elif msg_text == buttons['wol']:
        bot.send_message(chat_id, pi.wol())


def command_handler(chat_id, command):
    bot.send_message(chat_id, fixed(pi.run(command)), parse_mode='markdown')


def message_handler(messages):
    for message in messages:
        if message.from_user.id == ADMIN:
            if message.text in buttons.values():
                button_handler(message.chat.id, message.text)

            elif message.text in ['/start', '/help']:
                welcome(message)

            else:
                command_handler(message.chat.id, message.text)


def main():
    bot.set_update_listener(message_handler)
    bot.send_message(ADMIN, pi.online(), parse_mode='markdown',
                     disable_notification=True)
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
