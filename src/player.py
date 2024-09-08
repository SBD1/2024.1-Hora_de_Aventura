from db import connection

class Player():
  current_region=""
  playerId=1 #Hardcoded por enquanto
  spaceOptions={}

  def __init__(self,db_connection: connection.Connection) -> None:
        self.cursor = db_connection.cursor
        self.commit = db_connection.commit
        self.rollback = db_connection.rollback
  
  def moveToSpace(self, cmdSelf,optionNumber):
    if int(optionNumber) == 0:
      return None
    selectedSpaceId = self.spaceOptions.get(int(optionNumber),-1)

    if selectedSpaceId < 0:
      print("Opção inválida, por favor selecione um destino disponível")
      self.getCurrentPosition()
      return None
    self.cursor.execute("UPDATE Jogador SET regiao=%s WHERE id_jogador=%s;",[selectedSpaceId,self.playerId])
    self.cursor.execute("SELECT nome FROM Regiao WHERE id_regiao=%s;",[selectedSpaceId])
    self.current_region = self.cursor.fetchone()[0]
    self.commit()
    return self.getCurrentPosition()
  
  def getCurrentPosition(self):
    self.cursor.execute("SELECT j.regiao, r.nome FROM Jogador j INNER JOIN Regiao r ON j.regiao = r.id_regiao WHERE id_jogador=%s;",[self.playerId])
    currentPosition = self.cursor.fetchone()
    self.current_region = currentPosition[1].strip()
    self.cursor.execute("SELECT r.id_regiao, r.nome FROM Regiao r JOIN Caminhos c ON c.regiao_destino = r.id_regiao WHERE c.regiao=%s;",[currentPosition[0]])
    print(f"Você esta em {self.current_region}, os destinos disponíveis são:")
    print("0 - Cancelar movimento")
    for index, row in enumerate(self.cursor.fetchall()):
        id, nome = row
        self.spaceOptions[index+1] = id
        print(f"{index+1} - {nome.strip()}")

