import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
MSSQL = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'inventario',
        'USER': 'sa',
        'PASSWORD': 'Password123.',
        'HOST': 'DESKTOP-RTR90I9',
        'PORT': '1433',
        'OPTIONS': {'driver': 'ODBC Driver 17 for SQL Server',
                    },
    }
}

