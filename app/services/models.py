from sqlalchemy import MetaData, Table, Column, Integer, String, Date, ForeignKey


metadata = MetaData()

invoices = Table('invoices', metadata,
                 Column('id', Integer, autoincrement=True, primary_key=True),
                 Column('project', Integer, ForeignKey('projects.id')),
                 Column('description', String))


users = Table('users', metadata,
              Column('id', Integer, autoincrement=True, primary_key=True),
              Column('login', String, unique=True),
              Column('password', String))


projects = Table('projects', metadata,
                 Column('id', autoincrement=True, primary_key=True),
                 Column('user', Integer, ForeignKey('users.id')),
                 Column('date', Date))



