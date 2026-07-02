import psycopg2

def conectar():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="********",
        port=5432
    )
