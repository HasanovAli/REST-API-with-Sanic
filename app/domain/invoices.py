from app.services.models import invoices
from aiopg.sa import create_engine
from app.services.database import connection_url


class Invoices:

    @staticmethod
    async def get_invoice(invoice_id=None):
        async with create_engine(connection_url) as engine:
            async with engine.acquire() as conn:
                if invoice_id:
                    query = invoices.select(invoices.c.id == invoice_id)
                else:
                    query = invoices.select()
                invoices_data = []
                async for row in conn.execute(query):
                    invoices_data.append(dict(row))
                return invoices_data

    @staticmethod
    async def insert_invoices(project_id, description=None):
        async with create_engine(connection_url) as engine:
            async with engine.acquire() as conn:
                query = invoices.insert().values(project_id=project_id, description=description)
                await conn.execute(query)

    @staticmethod
    async def delete_invoice(invoice_id=None):
        async with create_engine(connection_url) as engine:
            async with engine.acquire() as conn:
                if invoice_id:
                    query = invoices.delete().where(invoices.c.id == int(invoice_id))
                else:
                    query = invoices.delete()
                await conn.execute(query)

    @staticmethod
    async def update_invoice(invoice_id, project_id, description):
        async with create_engine(connection_url) as engine:
            async with engine.acquire() as conn:
                query = invoices.update().where(invoices.c.id == invoice_id).values(project_id=project_id,
                                                                                    description=description)
                await conn.execute(query)
