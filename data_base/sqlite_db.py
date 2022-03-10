import sqlite3 as sq
from aiogram.dispatcher.filters.state import State, StatesGroup


def sql_start():
    global base, cur
    base = sq.connect('memes_egor.db')
    cur = base.cursor()
    if base:
        print('Data base is connected OK')
    base.execute('''CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT''')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('''INSERT INTO menu VALUES (?, ?, ?, ?)''', tuple(data.values()))
        base.commit()
