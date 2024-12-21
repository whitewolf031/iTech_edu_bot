from telebot import types
from Localisation.keyboard_lang import *


def generate_language():
    keyboard = types.InlineKeyboardMarkup()
    btn_uz = types.InlineKeyboardButton(text="🇺🇿Uz", callback_data="uz")
    btn_en = types.InlineKeyboardButton(text="🇺🇸En", callback_data="en")
    btn_ru = types.InlineKeyboardButton(text="🇷🇺Ru", callback_data="ru")
    keyboard.row(btn_uz, btn_en, btn_ru)
    return keyboard

def main_menu(lang):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton(aboutcourse[lang])
    btn2 = types.KeyboardButton(connect[lang])
    btn3 = types.KeyboardButton(register[lang])
    about_us = types.KeyboardButton(aboutus[lang])
    menu_back = types.KeyboardButton(change_languange[lang])
    markup.row(btn1, btn2)
    markup.row(btn3, about_us)
    markup.row(menu_back)
    return markup


def registration_menu(lang):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_back = types.KeyboardButton(back[lang])
    btn1 = types.KeyboardButton(courses[lang])
    btn2 = types.KeyboardButton(office_management[lang])
    btn3 = types.KeyboardButton(foundation[lang])
    btn4 = types.KeyboardButton(Specialty[lang])
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    markup.row(btn_back)
    return markup


def back_button_menu(lang):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_back = types.KeyboardButton(back[lang])
    markup.row(btn_back)
    return markup


def phone_number_button(lang):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    btn_phone = types.KeyboardButton(share_phone_number[lang], request_contact=True)
    btn_back = types.KeyboardButton(back[lang])
    markup.row(btn_phone, btn_back)
    return markup

def signup(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_signup = types.KeyboardButton(register[lang])
    btn_back = types.KeyboardButton(back[lang])
    keyboard.row(btn_signup)
    keyboard.row(btn_back)
    return keyboard

def contact(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn = types.KeyboardButton(text=phone_number[lang], request_contact=True)
    keyboard.row(btn)
    return keyboard

def commit(lang):
    keyboard = types.InlineKeyboardMarkup()
    btn_yes = types.InlineKeyboardButton(text=yes_lang[lang], callback_data="yes")
    btn_no = types.InlineKeyboardButton(text=no_lang[lang], callback_data="no")
    keyboard.row(btn_yes, btn_no)
    return keyboard
