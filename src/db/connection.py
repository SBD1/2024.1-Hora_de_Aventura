import psycopg2
from classes_dto import *


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
            self.cursor 2= self.conn.cursor()
            self.commit = self.conn.commit
            self.rollback = self.conn.rollback
         
         except psycopg2.OperationalError as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.conn = None
   
   def create_new_character(self, nome):    
      try:
            print("\nCriando novo personagem...")
            query = """
               INSERT INTO Jogador (nome, regiao, missao_atual, vida, qnt_ouro)
               VALUES (%s, 2, NULL, 500, 0)
            """
            self.cursor.execute(query, (nome,))
            self.commit()
            print("Personagem criado com sucesso!")
            
      except Exception as e:
         print(f"Erro ao criar personagem: {e}")
         self.rollback()

   def get_character(self, name):

        
      query = """SELECT id_jogador FROM Jogador
                    WHERE( Jogador.nome = '%s') 
                    """ % (name)
         
      self.cursor.execute(query)
      rtn = cursor.fetchone()
      if(rtn == None):
         return CurrentPlayer(-1, -1, -1, -1, -1, -1)
      else:
         query = """SELECT * FROM Jogador
                    WHERE( Jogador.nome = '%s') 
                    """ % (name)
                    
         self.cursor.execute(query)
         id_jogador, nome, regiao, missao_atual, vida, qnt_ouro = cursor.fetchone()

         return CurrentPlayer(id_jogador, nome, regiao, missao_atual, vida, qnt_ouro)

   def get_current_region(self, id_jogador):
      queryOne = """
         SELECT j.regiao, r.nome FROM Jogador j 
         INNER JOIN Regiao r ON j.regiao = r.id_regiao 
         WHERE j.id_jogador=%s
            """ % (id_jogador)
      self.cursor.execute(queryOne)
      region = self.cursor.fetchone()
      return region
   
   def get_current_sala(self, id_jogador):
      queryOne = """
         SELECT j.sala, CONCAT(r.nome,'_',s.id_sala) FROM Jogador j 
         INNER JOIN Sala s ON j.sala = s.id_sala
         INNER JOIN Regiao r ON s.regiao = r.id_regiao
         WHERE j.id_jogador=%s
            """ % (id_jogador)
      self.cursor.execute(queryOne)
      region = self.cursor.fetchone()
      return region

   # TODO:  Trocar por sala
   def get_available_regions(self, id_regiao):
      query = """
         SELECT r.id_regiao, r.nome FROM Regiao r 
         JOIN Caminhos c ON c.regiao_destino = r.id_regiao
         WHERE c.regiao=%s;
         """ % (id_regiao)
      self.cursor.execute(query)
      regions = self.cursor.fetchall()
      return regions

   # TODO:  Trocar por sala
   def update_player_position(self, id_jogador, id_regiao):
      query = """
         UPDATE Jogador SET regiao=%s WHERE id_jogador=%s;
         """ % (id_regiao,id_jogador)
      self.cursor.execute(query)
      self.commit()

   # TODO:  Trocar por sala
   def get_available_inimigos_regiao(self, id_regiao):
      query = """
         SELECT r.id_regiao, r.nome FROM Regiao r 
         JOIN Caminhos c ON c.regiao_destino = r.id_regiao
         WHERE c.regiao=%s;
         """ % (id_regiao)
      self.cursor.execute(query)
      qEnemys = self.cursor.fetchall()
      enemies = []
      for row in qEnemys:
         id_instancia_inimigo, id_inimigo, nome, descricao,regiao,dano,defesa,vida, drop = row
         enemies.append(Enemy(id_instancia_inimigo, id_inimigo, nome, descricao,regiao,dano,defesa,vida, drop))
      return enemies
   
   
   def close(self):
      self.conn.close()

