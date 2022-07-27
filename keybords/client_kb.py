from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположениие')
b3 = KeyboardButton('/Меню')
# b4 = KeyboardButton('/Поделиться номером', request_contact=True)
# b5 = KeyboardButton('/Отправить Где я', request_location=True)

kb_clients = ReplyKeyboardMarkup(resize_keyboard=True)

kb_clients.add(b1).add(b2).insert(b3)#.row(b4, b5)
