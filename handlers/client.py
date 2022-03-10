from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove

from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db


# @dp.message_handler(commands=['start', 'help'])
async def comand_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятно познакомиться!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через лс, напишите ему: \n t.me/just_Egor_bot')


# @dp.message_handler(commands=['schedule'])
async def comand_schedule(message: types.Message):
    await bot.send_message(message.from_user.id, 'Свежие мем каждый день в 10 утра', reply_markup=ReplyKeyboardRemove())


# @dp.message_handler(commands=['address'])
async def comand_address(message: types.Message):
    await bot.send_message(message.from_user.id, 'Всемирная паутина сети интернет')


# @dp.message_handler(commands=['data_base'])
async def comand_db(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(comand_start, commands=['start', 'help'])
    dp.register_message_handler(comand_schedule, commands=['schedule'])
    dp.register_message_handler(comand_address, commands=['address'])
    dp.register_message_handler(comand_db, commands=['data_base'])
