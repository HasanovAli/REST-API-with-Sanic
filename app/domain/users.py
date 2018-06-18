from app.services.models import users
from aiopg.sa import create_engine
from app.services.database import connection_url
import hashlib


class Users:

    @staticmethod
    async def get_user(login=None):
        async with create_engine(connection_url) as engine:
            async with engine.acquire() as conn:
                if login:
                    query = users.select(users.c.login == login)
                else:
                    query = users.select()
                users_data = []
                async for row in conn.execute(query):
                    users_data.append(dict(row))
                return users_data

    @staticmethod
    async def insert_user(login, password: str):
        password_hash = hashlib.md5(bytes(password, 'utf-8')).hexdigest()
        async with create_engine(connection_url) as engine:
            async with engine.acquire() as conn:
                query = users.insert().values(login=login, password_hash=password_hash)
                await conn.execute(query)

    @staticmethod
    async def delete_user(login=None):
        async with create_engine(connection_url) as engine:
            async with engine.acquire() as conn:
                if login:
                    query = users.delete().where(users.c.login == login)
                else:
                    query = users.delete()
                await conn.execute(query)

    @staticmethod
    async def update_user(user_id, login, password):
        password_hash = hashlib.md5(bytes(password, 'utf-8')).hexdigest()
        async with create_engine(connection_url) as engine:
            async with engine.acquire() as conn:
                query = users.update().where(users.c.id == user_id).values(login=login,
                                                                           password_hash=password_hash)
                await conn.execute(query)
