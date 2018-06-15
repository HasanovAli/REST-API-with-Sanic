from aiopg.sa import create_engine
from sqlalchemy import MetaData
from app.config import db

connection_url = 'user={user} host={host} dbname={name} password={password}'.format(**db)

metadata = MetaData()


async def create_tables():
    async with create_engine(connection_url) as engine:
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


async def create_db():
    async with create_engine(connection_url) as engine:
        async with engine.acquire() as conn:
            await conn.execute('CREATE DATABASE {}'.format('ss_train'))
            await prepare_db()


async def prepare_db():
    await create_tables()
