from sanic.views import HTTPMethodView
from app.services.authorization import verify_login_data


class LoginView(HTTPMethodView):
    async def post (self, request):
        response = await verify_login_data(login=request.headers.get('login'),
                                           password=request.headers.get('password'))
        return response
