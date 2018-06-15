from sanic import Sanic
from app.resources.project_view import ProjectsView, ProjectView
from app.resources.invoice_view import InvoicesView, InvoiceView
from app.resources.user_view import UsersView, UserView


app = Sanic(__name__)


app.add_route(UsersView.as_view(), '/users')
app.add_route(UserView.as_view(), '/users/<login>')
app.add_route(ProjectsView.as_view(), '/projects')
app.add_route(ProjectView.as_view(), '/projects/<project_id>')
app.add_route(InvoicesView.as_view(), '/projects/<project_id>/invoices')
app.add_route(InvoiceView.as_view(), '/projects/<project_id>/invoices/<invoice_id>')
