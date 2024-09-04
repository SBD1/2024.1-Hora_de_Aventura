import psycopg2

class Conection:
   __instance = None
   def __new__(cls):
       if Conection.__instance is None:
          Conection.__instance = super().__new__(cls)
       return Conection.__instance

   def __init__(self):
    conn = psycopg2.connect(database="test", host="localhost",user="user",password="password",port="5432")
    self.cursor = conn.cursor()
   
   def create_new_character(connection, nome):
      cursor = connection.cursor()

      querry = "INSERT INTO Jogador (nome, regiao, missao_atual, vida, qntOuro) VALUES ('%s', 2, 0, 500, 0)" % (nome)

      cursor.execute(querry)
      
      connection.commit()
      cursor.close()

