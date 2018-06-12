from sanic.views import HTTPMethodView
from app.resources.service_resource import smoke


class SmokeView(HTTPMethodView):
    @staticmethod
    async def get(request):
        return await smoke(request)
