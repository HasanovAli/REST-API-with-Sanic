import hashlib
import secrets
from sanic.response import json as sanic_json
from sanic.exceptions import Unauthorized
from app.domain.users import Users
from app.services.database import RedisEngine


available_endpoints = ['/login']


async def get_token():
    token = secrets.token_hex(16)
    return token


async def verify_login_data(login, password):
    entered_password = hashlib.md5(bytes(password, 'utf-8')).hexdigest()
    user_info = await Users.get_user(login)
    user_password = user_info[0]['password_hash']
    if entered_password == user_password:
        token = await get_token()
        user_id = user_info[0]['id']
        await insert_redis(token, user_id)
        return await token_response(token)
    else:
        raise Unauthorized("Wrong login or password")


async def verify_token(request):
    token = request.headers.get('Authorization')
    if request.path in available_endpoints:
        return True
    stored_token = await verify_token_in_redis(token)
    if stored_token and stored_token == token:
        return True
    else:
        raise Unauthorized('Unauthorized user')


async def token_response(token):
    response = sanic_json({'message': 'authorized'},
                          headers={'Authorization': token})
    return response


async def insert_redis(token, user_id):
    connection = await RedisEngine.get_redis_engine()
    await connection.set(token, str(user_id))


async def verify_token_in_redis(token):
    connection = await RedisEngine.get_redis_engine()
    try:
        await connection.get(token)
        return token
    except TypeError:
        raise Unauthorized('Unauthorized user')


