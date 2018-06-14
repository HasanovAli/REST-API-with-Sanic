import os

db = {
    'user': os.environ.get('DB_USERNAME', 'postgres'),
    'password': os.environ.get('DB_PASSWORD', 'postgres'),
    'host': os.environ.get('DB_HOST', 'localhost'),
    'port': os.environ.get('DB_PORT', 5432),
    'name': os.environ.get('DB_NAME', 'ss_train')
}