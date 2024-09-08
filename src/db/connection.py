import psycopg2
from classes import *


class Connection:
   __instance = None
   
   def __new__(cls):
       if Connection.__instance is None:
          Connection.__instance = super().__new__(cls)
       return Connection.__instance

   def __init__(self):
      if not hasattr(self, 'conn'):
         try:
            self.conn = psycopg2.connect(database="test", host="localhost",user="user",password="password",port="5432")
            self.cursor = self.conn.cursor()
            self.commit = self.conn.commit
            self.rollback = self.conn.rollback
         
         except psycopg2.OperationalError as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.conn = None
   
   def create_new_character(self, nome):    
      try:
         with self.conn.cursor() as cursor:
            print("\nCriando novo personagem...")
            query = """
               INSERT INTO Jogador (nome, regiao, missao_atual, vida, qnt_ouro)
               VALUES (%s, 2, NULL, 500, 0)
            """
            cursor.execute(query, (nome,))
            self.conn.commit()
            print("Personagem criado com sucesso!")
            
      except Exception as e:
         print(f"Erro ao criar personagem: {e}")
         self.conn.rollback()

   def get_character(self, name):
      cursor = self.conn.cursor()
        
      query = """SELECT id_jogador FROM Jogador
                    WHERE( Jogador.nome = '%s') 
                    """ % (name)
         
      cursor.execute(query)
      rtn = cursor.fetchone()
      if(rtn == None):
         cursor.close()
         return CurrentPlayer(-1, -1, -1, -1, -1, -1)
      else:
         query = """SELECT * FROM Jogador
                    WHERE( Jogador.nome = '%s') 
                    """ % (name)
                    
         cursor.execute(query)
         id_jogador, nome, regiao, missao_atual, vida, qnt_ouro = cursor.fetchone()

         cursor.close()
         return CurrentPlayer(id_jogador, nome, regiao, missao_atual, vida, qnt_ouro)
         
   def get_current_region(self, id_jogador):
      cursor = self.conn.cursor()
      queryOne = """
         SELECT j.regiao, r.nome FROM Jogador j 
         INNER JOIN Regiao r ON j.regiao = r.id_regiao 
         WHERE id_jogador=%s
            """ % (id_jogador)
      cursor.execute(queryOne)
      region = cursor.fetchone()
     
      cursor.close()
      return region

   def get_available_regions(self):
      cursor = self.conn.cursor()
      query = """
         SELECT id_regiao, nome FROM Regiao
         """
      cursor.execute(query)
      regions = cursor.fetchall()
      cursor.close()
      return regions
   
   def close(self):
      self.conn.close()

