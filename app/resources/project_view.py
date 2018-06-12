from sanic.views import HTTPMethodView
from app.resources.service_resource import project


class ProjectView(HTTPMethodView):

    @staticmethod
    async def get(request):
        return await project(request)

    @staticmethod
    async def post(request):
        return await project(request)

    @staticmethod
    async def put(request):
        return await project(request)

    @staticmethod
    async def delete(request):
        return await project(request)
