from sanic.views import HTTPMethodView
from sanic.response import json as sanic_json
from app.domain.projects import Projects


class ProjectView(HTTPMethodView):

    async def get(self, request, project_id):
        result = await Projects.get_project()
        return sanic_json(result)

    async def post(self, request):
        await Projects.insert_project(user_id=request.headers.get('user_id'),
                                      date=request.headers.get('date'))
        return sanic_json({'message': 'project has been added'})

    async def delete(self, request):
        await Projects.delete_project(request)
        return sanic_json({'message': 'the db has been deleted'})
