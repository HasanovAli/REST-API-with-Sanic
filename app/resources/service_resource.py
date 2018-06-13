from sanic.response import text
from app.services import database
from app.services.models import projects


async def smoke(request):
    return text("smoke")


async def project(request):
    if request.method == 'GET':
        await database.get_entry(projects, entry_id=request.args.get('entry_id'))

    if request.method == 'POST':
        await database.insert_entry(projects, user_id=request.args.get('user_id'), date=request.args.get('date'))

    if request.method == 'PUT':
        await database.update_entry(projects, user_id=request.args.get('user_id'), date=request.args.get('date'))

    if request.method == 'DELETE':
        await database.delete_entry(projects, entry_id=request.args.get('entry_id'))

