import psycopg2
import os

pgconn = psycopg2.connect(
    host=os.environ['DB_HOST'],
    database=os.environ['DB_NAME'],
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD']
)


def transaction(query: str, params: list = None, fetchall: bool = False):
    cursor = pgconn.cursor()
    cursor.execute(query, params)
    data = cursor.fetchall()
    pgconn.commit()
    cursor.close()
    return data
