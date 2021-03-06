import asyncio_redis
from aiopg.sa import create_engine
from sqlalchemy import MetaData
from app.config import db, redis, default_postgres_db

connection_url_ss_train = 'user={user} host={host} dbname={name} password={password}'.format(**db)
connection_url_postgres = 'user={user} host={host} dbname={name} password={password}'.format(**default_postgres_db)

metadata = MetaData()


class RedisEngine:
    _engine = None

    @classmethod
    async def get_redis_engine(cls):
        if not cls._engine:
            cls._engine = await asyncio_redis.Connection.create(host=redis['host'],
                                                                port=redis['port'])
        return cls._engine


async def create_tables():
    async with create_engine(connection_url_ss_train) as engine:
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

    async with create_engine(connection_url_postgres) as engine:
        async with engine.acquire() as conn:
            await conn.execute('CREATE DATABASE {}'.format('ss_train'))
            await prepare_db()


async def prepare_db():
    await create_tables()


async def drop_db():
    async with create_engine(connection_url_postgres) as engine:
        async with engine.acquire() as conn:
            await conn.execute('DROP DATABASE {}'.format('ss_train'))