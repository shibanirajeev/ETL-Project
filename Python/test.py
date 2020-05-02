import psycopg2

conn_string = "host='localhost' dbname='ETL_Project_DB' user='postgres' password='postgres'"
conn = psycopg2.connect(conn_string)

cursor = conn.cursor()
cursor.execute("SELECT * FROM emissions_infrastructure LIMIT 10;")

print(cursor)

result = cursor.fetchall()

for row in result:
    print(row)

conn.close()