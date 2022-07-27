from aiogram import types, Dispatcher
from create_bot import dp, bot
from keybords.client_kb import kb_clients
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_dp


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита!', reply_markup=kb_clients)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС. Напишите ему: \nhttps://t.me/Kross_ShefBot')


#@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вт-Чт с 9.00 до 22.00')


#@dp.message_handler(commands=['Расположениие'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул.Киевская 23а', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['Меню'])
async def pizza_menu_commands(message: types.Message):
    await sqlite_dp.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположениие'])
    dp.register_message_handler(pizza_menu_commands, commands=['Меню'])
