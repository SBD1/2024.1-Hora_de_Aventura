from db import connection

class Player():
  current_region=""
  playerId=1 #Hardcoded por enquanto
  spaceOptions={}

  def __init__(self,db_coonection: connection.Connection) -> None:
        self.cursor = db_coonection.cursor 
  
  def moveToSpace(self, cmdSelf,optionNumber):
    selectedSpaceId = self.spaceOptions.get(optionNumber,-1)
    if selectedSpaceId == 0:
      return None
    if selectedSpaceId < 0:
      print("Opção inválida, por favor selecione um destino disponível")
      self.getCurrentPosition()
      return None
    self.cursor.excute("UPDATE Jogador SET regiao=%s WHERE id=%s;",(selectedSpaceId,self.playerId))
    self.cursor.excute("SELECT nome FROM Jogador WHERE id_regiao=%s;",(selectedSpaceId))
    self.current_region = self.cursor.fetchOne()[0]
    self.cursor.commit()
    return self.getCurrentPosition()
  
  def getCurrentPosition(self):
    self.cursor.execute("SELECT r.id_regiao, r.nome FROM Regiao r JOIN Caminhos c ON c.regiao_destino = r.id_regiao WHERE c.regiao=%s;")
    listToPrint = []
    listToPrint.append("0 - Cancelar movimento")
    for index, row in enumerate(self.cursor.fetchall()):
        id, nome = row
        self.spaceOptions[index+1] = id
        listToPrint.append(f"{index+1} - {nome}")
    print(f"Você esta em {self.current_region}, os destinos disponíveis são:")
    print(listToPrint)

