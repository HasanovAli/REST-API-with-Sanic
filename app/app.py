from sanic import Sanic
from app.resources.project_view import ProjectsView, ProjectView
from app.resources.invoice_view import InvoicesView, InvoiceView
from app.resources.user_view import UsersView, UserView
from app.resources.login_view import LoginView
from app.services.authorization import verify_token


app = Sanic(__name__)


@app.middleware('request')
async def verify_user_access(request):
    await verify_token(request)


app.add_route(UsersView.as_view(), '/users')
app.add_route(UserView.as_view(), '/users/<login>')
app.add_route(ProjectsView.as_view(), '/projects')
app.add_route(ProjectView.as_view(), '/projects/<project_id>')
app.add_route(InvoicesView.as_view(), '/projects/<project_id>/invoices')
app.add_route(InvoiceView.as_view(), '/projects/<project_id>/invoices/<invoice_id>')
app.add_route(LoginView.as_view(), '/login')
