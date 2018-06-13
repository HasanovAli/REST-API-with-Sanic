from sqlalchemy import MetaData, Table, Column, Integer, String, Date, ForeignKey


metadata = MetaData()

invoices = Table('invoices', metadata,
                 Column('id', Integer, autoincrement=True, primary_key=True),
                 Column('project_id', Integer, ForeignKey('projects.id')),
                 Column('description', String))


users = Table('users', metadata,
              Column('id', Integer, autoincrement=True, primary_key=True),
              Column('login', String, unique=True),
              Column('password_hash', String))


projects = Table('projects', metadata,
                 Column('id', autoincrement=True, primary_key=True),
                 Column('user_id', Integer, ForeignKey('users.id')),
                 Column('date', Date))



