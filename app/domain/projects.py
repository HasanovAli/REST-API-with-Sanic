from app.services.models import projects
from aiopg.sa import create_engine
from app.services.database import connection_url


class Projects:
    @staticmethod
    async def get_project(project_id=None):
        async with create_engine(connection_url) as engine:
            async with engine.acquire() as conn:
                if project_id:
                    query = projects.select(projects.c.id == project_id)
                else:
                    query = projects.select()
                projects_data = []
                async for row in conn.execute(query):
                    projects_data.append(dict(row))
                return projects_data

    @staticmethod
    async def insert_project(user_id, date):
        async with create_engine(connection_url) as engine:
            async with engine.acquire() as conn:
                query = projects.insert().values(user_id=user_id, date=date)
                await conn.execute(query)

    @staticmethod
    async def delete_project(project_id=None):
        async with create_engine(connection_url) as engine:
            async with engine.acquire() as conn:
                if project_id:
                    query = projects.delete().where(projects.c.id == int(project_id))
                else:
                    query = projects.delete()
                await conn.execute(query)

    @staticmethod
    async def update_project(project_id, user_id, date):
        async with create_engine(connection_url) as engine:
            async with engine.acquire() as conn:
                query = projects.update().where(projects.c.id == project_id).values(user_id=user_id, date=date)
                await conn.execute(query)
