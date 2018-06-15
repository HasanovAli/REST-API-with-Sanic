from sanic import Sanic
from app.resources.project_view import ProjectsView, ProjectView
from app.resources.invoice_view import InvoicesView, InvoiceView


app = Sanic(__name__)


# app.aad_route(LoginView.as_view()), '/login')
app.add_route(ProjectsView.as_view(), '/projects')
app.add_route(ProjectView.as_view(), '/projects/<project_id>')
app.add_route(InvoicesView.as_view(), '/projects/<project_id>/invoices')
app.add_route(InvoiceView.as_view(), '/projects/<project_id>/invoices/<invoice_id>')

