import psycopg2

class Conection:
   __instance = None
   def __new__(cls):
       if Conection.__instance is None:
          Conection.__instance = super().__new__(cls)
       return Conection.__instance

   def __init__(self):
    conn = psycopg2.connect(database="db_name", host="db_host",user="db_user",password="db_pass",port="db_port")
    self.cursor = conn.cursor()

