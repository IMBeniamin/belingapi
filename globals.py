import psycopg2
import os

pgconn = psycopg2.connect(
    host="postgresql-imben.alwaysdata.net",
    database="imben_netflix",
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD']
)


def transaction(query: str, params: list = None, fetchall: bool = False):
    cursor = pgconn.cursor()
    cursor.execute(query, params)
    data = cursor.fetchall() if fetchall else cursor.fetchone()
    pgconn.commit()
    cursor.close()
    return data
