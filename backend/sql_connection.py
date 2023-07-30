import datetime
# import mysql.connector
import psycopg2

__cnx = None

def get_sql_connection():
  print("Opening postgres connection")
  global __cnx

  host = '127.0.0.1'
  port = '5432'
  dbname = 'Inventory_system'
  user = 'postgres'
  password = 'Sh@gufta12'

  if __cnx is None:
    __cnx = psycopg2.connect(host=host, port=port,dbname=dbname, user=user, password=password)

  return __cnx

