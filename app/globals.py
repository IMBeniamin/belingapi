import os
import psycopg2
from psycopg2 import pool

# create a connection pool
conn_pool = psycopg2.pool.ThreadedConnectionPool(
    minconn=1,
    maxconn=5,
    host=os.environ['DB_HOST'],
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'],
    database=os.environ['DB_NAME']
)


def transaction(query: str, params: list = None, fetchall: bool = False):
    with conn_pool.getconn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            if fetchall:
                return cursor.fetchall()
            return cursor.fetchone()
