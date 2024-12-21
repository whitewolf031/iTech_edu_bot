import telebot
import os
from dotenv import load_dotenv
from Localisation.lang import *
from keyboard import *
import time
from Localisation.keyboard_lang import *

load_dotenv()

TOKEN = os.getenv('TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')
canal_id = os.getenv('CANAL_ID')
IMAGE_URL = os.getenv('IMAGE_URL')
IMAGE_CAPTION = os.getenv('IMAGE_CAPTION')
bot = telebot.TeleBot(TOKEN)

personal_details = {}
user_langs = {}

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")
    bot.send_message(message.chat.id, "Assalomu aleykum tilni tanlang!", reply_markup=generate_language())

@bot.callback_query_handler(func=lambda call: call.data in ["uz","en","ru"])
def Language(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")
    if call.data == "uz":
        lang = "uz"

    elif call.data == "en":
        lang = "en"

    elif call.data == "ru":
        lang = "ru"

    bot.send_message(chat_id, choose_section[lang], reply_markup=main_menu(lang))
    bot.register_next_step_handler(call.message, bot_menu)
    user_langs[chat_id] = lang

def bot_menu(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")

    if message.text == aboutcourse[lang]:
        bot.send_message(chat_id, course_choose[lang], reply_markup=registration_menu(lang))
        bot.register_next_step_handler(message, choosecourse)

    elif message.text == connect[lang]:
        bot.send_message(chat_id, contact_with_us[lang], reply_markup=back_button_menu(lang))
        bot.register_next_step_handler(message, general_back)

    elif message.text == register[lang]:
        bot.send_message(chat_id, your_name[lang])
        bot.register_next_step_handler(message, registration)

    elif message.text == aboutus[lang]:
        bot.send_message(chat_id, info[lang], reply_markup=back_button_menu(lang))
        bot.register_next_step_handler(message, general_back)

    elif message.text == change_languange[lang]:
        return start(message)


def choosecourse(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")

    if message.text == courses[lang]:
        bot.send_message(chat_id, about_course[lang], reply_markup=signup(lang))
        bot.register_next_step_handler(message, check)

    elif message.text == office_management[lang]:
        bot.send_message(chat_id, office_menegerlik[lang], reply_markup=signup(lang))
        bot.register_next_step_handler(message, check)

    elif message.text == foundation[lang]:
        bot.send_message(chat_id, info_foundation[lang], reply_markup=signup(lang))
        bot.register_next_step_handler(message, check)

    elif message.text == Specialty[lang]:
        bot.send_message(chat_id, profesion[lang], reply_markup=signup(lang))
        bot.register_next_step_handler(message, check)

    elif message.text == back[lang]:
        bot.send_message(chat_id, choose_section[lang], reply_markup=main_menu(lang))
        bot.register_next_step_handler(message, bot_menu)

def check(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")

    if message.text == register[lang]:
        bot.send_message(chat_id, your_name[lang])
        bot.register_next_step_handler(message, registration)

    elif message.text == back[lang]:
        bot.send_message(chat_id, choose_section[lang], reply_markup=main_menu(lang))
        bot.register_next_step_handler(message, bot_menu)


def registration(message):
    fio = message.text
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")

    bot.send_message(chat_id, your_age[lang])
    bot.register_next_step_handler(message, user_name, fio)

def user_name(message, fio):
    age = message.text
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")

    bot.send_message(chat_id, your_number[lang], reply_markup=contact(lang))
    bot.register_next_step_handler(message, send_group_message, fio, age)

def send_group_message(message, fio, age):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")

    if message.text:
        phone = message.text
        personal_details['fio'] = fio
        personal_details['age'] = age
        personal_details['phone'] = phone
        bot.send_message(chat_id, f"{name[lang]} {fio}\n"
                                  f"{agge[lang]} {age}\n"
                                  f"{number[lang]} {phone}", reply_markup=commit(lang))


    elif message.contact:
        phone = message.contact.phone_number
        personal_details['fio'] = fio
        personal_details['age'] = age
        personal_details['phone'] = phone
        bot.send_message(chat_id, f"{name[lang]} {fio}\n"
                                  f"{agge[lang]} {age}\n"
                                  f"{number[lang]} {phone}", reply_markup=commit(lang))

@bot.callback_query_handler(func=lambda call: call.data in ["yes", "no"])
def callback_handler(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")

    fio = personal_details['fio']
    age = personal_details['age']
    phone = personal_details['phone']

    if call.data == yes_lang[lang]:
        bot.send_message(canal_id, f"{new_student[lang]}"
                                       f"{ismi[lang]} {fio}\n"
                                       f"{yoshi[lang]} {age}\n"
                                        f"{tel[lang]} {phone}")
        bot.send_message(chat_id, sent_to_admin[lang])

        time.sleep(1)
        bot.send_message(chat_id, choose_section[lang], reply_markup=main_menu(lang))
        bot.register_next_step_handler(call.message, bot_menu)


    elif call.data == no_lang[lang]:
        bot.send_message(chat_id, course_choose[lang], reply_markup=registration_menu(lang))
        bot.register_next_step_handler(call.message, choosecourse)


def general_back(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")

    bot.send_message(chat_id, choose_section[lang], reply_markup=main_menu(lang))
    bot.register_next_step_handler(message, bot_menu)

bot.polling(non_stop=True)
