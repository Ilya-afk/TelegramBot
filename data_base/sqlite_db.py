import sqlite3 as sq
from aiogram import types

from create_bot import dp, bot


def sql_start():
    global base, cur
    base = sq.connect('memes_egor.db')
    cur = base.cursor()
    if base:
        print('Data base is connected OK')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message: types.Message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n Описание: {ret[2]}\n Цена: {ret[3]}')
