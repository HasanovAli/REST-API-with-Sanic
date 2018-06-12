from sanic import Sanic
from app.resources.smoke_view import SmokeView
from app.resources.project_view import ProjectView
from app.services.database import create_tables


app = Sanic(__name__)


async def prepare_db():
    app.db = await create_tables()

app.add_route(SmokeView.as_view(), '/smoke')
app.add_route(ProjectView.as_view(), 'projects')


