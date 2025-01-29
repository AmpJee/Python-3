import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="demodb",
    user="postgres",
    password="postgres"
)

