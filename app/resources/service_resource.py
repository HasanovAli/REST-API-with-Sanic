from sanic.response import text
from app.services import database
from app.services.models import projects


async def smoke(request):
    return text("smoke")


async def project(request):
    if request.method == 'GET':
        await database.get_entry(projects)
        return text('this is project with GET')
    if request.method == 'POST':
        await database.update_entry(projects)
        return text('this is project with POST')
    if request.method == 'PUT':
        await database.update_entry(projects)
        return text('this is project with PUT')
    if request.method == 'DELETE':
        await database.delete_entry(projects)
        return text('this is project with DELETE')
