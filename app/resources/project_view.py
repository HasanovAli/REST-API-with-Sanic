from sanic.views import HTTPMethodView
from sanic.response import json as sanic_json
from app.domain.projects import Projects


class ProjectsView(HTTPMethodView):

    async def get(self, request):
        result = await Projects.get_project()
        return sanic_json(result)

    async def post(self, request):
        await Projects.insert_project(user_id=request.headers.get('user_id'),
                                      date=request.headers.get('date'))
        return sanic_json({'message': 'project has been added'})

    async def delete(self, request):
        await Projects.delete_project(request)
        return sanic_json({'message': 'all projects have been deleted'})


class ProjectView(HTTPMethodView):

    async def get(self, request, project_id):
        result = await Projects.get_project(project_id)
        return sanic_json(result)

    async def put(self, request, project_id):
        await Projects.update_project(project_id, user_id=request.headers.get('user_id'),
                                      date=request.headers.get('date'))
        return sanic_json({'message': 'project has been updated'})

    async def delete(self, request, project_id):
        await Projects.delete_project(project_id)
        return sanic_json({'message': 'project has been deleted'})
