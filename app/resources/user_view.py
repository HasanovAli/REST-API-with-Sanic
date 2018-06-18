from sanic.views import HTTPMethodView
from sanic.response import json as sanic_json
from app.domain.users import Users


class UsersView(HTTPMethodView):

    async def get(self, request):
        result = await Users.get_user()
        return sanic_json(result)

    async def post(self, request):
        await Users.insert_user(login=request.headers.get('login'),
                                password=request.headers.get('password'))
        return sanic_json({'message': 'user has been added'})

    async def delete(self, request):
        await Users.delete_user(request)
        return sanic_json({'message': 'all users have been deleted'})


class UserView(HTTPMethodView):

    async def get(self, request, login):
        result = await Users.get_user(login)
        return sanic_json(result)

    async def put(self, request, user_id):
        await Users.update_user(user_id, login=request.headers.get('login'),
                                password=request.headers.get('password'))
        return sanic_json({'message': 'user has been updated'})

    async def delete(self, request, login):
        await Users.delete_user(login)
        return sanic_json({'message': 'user has been deleted'})
