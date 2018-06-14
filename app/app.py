from sanic import Sanic
from app.resources.project_view import ProjectsView, ProjectView


app = Sanic(__name__)


app.add_route(ProjectsView.as_view(), '/projects')
app.add_route(ProjectView.as_view(), '/projects/<project_id>')
