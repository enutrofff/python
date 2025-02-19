from psqlhelper.main import PostgresDB

db = PostgresDB(dbname='mydb', user='myuser', password='mypassword', log_level='INFO')
result = db.execute_query("SELECT * FROM cars3")
print(result)
db.close()