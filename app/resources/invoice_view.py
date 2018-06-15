from sanic.views import HTTPMethodView
from sanic.response import json as sanic_json
from app.domain.invoices import Invoices


class InvoicesView(HTTPMethodView):

    async def get(self, request):
        result = await Invoices.get_invoice()
        return sanic_json(result)

    async def post(self, request):
        await Invoices.insert_invoices(project_id=request.headers.get('project_id'),
                                       description=request.headers.get('description'))
        return sanic_json({'message': 'invoice has been added'})

    async def delete(self, request):
        await Invoices.delete_invoice(request)
        return sanic_json({'message': 'all invoices have been deleted'})


class InvoiceView(HTTPMethodView):

    async def get(self, request, invoice_id):
        result = await Invoices.get_invoice(invoice_id)
        return sanic_json(result)

    async def put(self, request, invoice_id):
        await Invoices.update_invoice(invoice_id, project_id=request.headers.get('project_id'),
                                      description=request.headers.get('description'))
        return sanic_json({'message': 'invoice has been updated'})

    async def delete(self, request, invoice_id):
        await Invoices.delete_invoice(invoice_id)
        return sanic_json({'message': 'invoice has been deleted'})
