from aiopg.sa import create_engine
from sqlalchemy import MetaData
from config import db


connection = 'postgres://{0}:{1}@{2}/{3}'.format(db["user"], db["password"], db["host"], db["db_name"])

metadata = MetaData()


async def create_tables():
    async with create_engine(connection) as engine:
        async with engine.acquire() as conn:
            await conn.execute('''CREATE TABLE IF NOT EXISTS users (
                id serial PRIMARY KEY,
                login varchar(255),
                password_hash varchar(255))''')
            await conn.execute('''CREATE TABLE IF NOT EXISTS projects (
                id serial PRIMARY KEY,
                user_id int references users(id),
                date date)''')
            await conn.execute('''CREATE TABLE IF NOT EXISTS invoices (
                id serial PRIMARY KEY,
                project_id int references projects(id),
                description varchar(255))''')


async def delete_entry(table_name, entry_id):
    async with create_engine(connection) as engine:
        async with engine.acquire() as conn:
            await conn.execute(table_name.delete().where(table_name.columns.id == entry_id))


async def insert_entry(table_name, **kwargs):
    async with create_engine(connection) as engine:
        async with engine.acquire() as conn:
            await conn.execute(table_name.insert().values(**kwargs))


async def update_entry(table_name, entry_id, **kwargs):
    async with create_engine(connection) as engine:
        async with engine.acquire() as conn:
            await conn.execute(table_name.update().where(table_name.columns.id == entry_id).values(**kwargs))


async def get_entry(table_name, entry_id):
    async with create_engine(connection) as engine:
        async with engine.acquire() as conn:
            return await conn.execute(table_name.select().where(table_name.columns.id == entry_id))



