import psycopg2

class Conection:
   __instance = None
   
   def __new__(cls):
       if Conection.__instance is None:
          Conection.__instance = super().__new__(cls)
       return Conection.__instance

   def __init__(self):
      if not hasattr(self, 'conn'):
         try:
            self.conn = psycopg2.connect(database="test", host="localhost",user="user",password="password",port="5432")
            self.cursor = self.conn.cursor()
         
         except psycopg2.OperationalError as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.conn = None
   
   def create_new_character(self, nome):
      cursor =  self.cursor
     
      try:
       
            print("Criando novo personagem...")
            query = """
               INSERT INTO Jogador (nome, regiao, missao_atual, vida, qntOuro)
               VALUES (%s, 2, 0, 500, 0)
            """
            cursor.execute(query, (nome,))
            self.conn.commit()
            print("Personagem criado com sucesso!")
            
      except Exception as e:
         print(f"Erro ao criar personagem: {e}")
         self.conn.rollback()

         
   def close(self):
      self.conn.close()

