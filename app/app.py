from sanic import Sanic

# from app.config import runtime_config
from app.resources.project_view import ProjectView


app = Sanic(__name__)
# app.config.from_object(runtime_config())


app.add_route(ProjectView.as_view(), '/projects')
app.add_route(ProjectView.as_view(), '/projects/<project_id>')
