from aiopg.sa import create_engine
from sqlalchemy import MetaData
from config import db


connection = 'postgres://{0}:{1}@{2}/{3}'.format(db["user"], db["password"], db["host"], db["db_name"])

metadata = MetaData()


async def create_tables():
    async with create_engine(connection) as engine:
        async with engine.acquire() as conn:
            await conn.execute('DROP TABLE IF EXISTS users')
            await conn.execute('DROP TABLE IF EXISTS projects')
            await conn.execute('DROP TABLE IF EXISTS invoices')
            await conn.execute('CREATE TABLE users (id SERIAL PRIMARY KEY, login, hash_password)')
            await conn.execute('CREATE TABLE projects (id SERIAL PRIMARY KEY, user reference users(id), date)')
            await conn.execute('CREATE TABLE invoices (id SERIAL PRIMARY KEY, project reference projects(id), '
                               'description)')


async def delete_entry(table_name, entry_id):
    async with create_engine(connection) as engine:
        async with engine.acquire() as conn:
            await conn.execute(table_name.delete().where(table_name.columns.id == int(entry_id)))


async def update_entry(table_name, entry_id, **kwargs):
    async with create_engine(connection) as engine:
        async with engine.acquire() as conn:
            await conn.execute(table_name.update().where(table_name.columns.id == int(entry_id)).values(**kwargs))


async def get_entry(table_name, entry_id):
    async with create_engine(connection) as engine:
        async with engine.acquire() as conn:
            return await conn.execute(table_name.select().where(table_name.columns.id == int(entry_id)))



