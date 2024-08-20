from db import connection

class Player():
  current_region=""
  playerId=1 #Hardcoded por enquanto
  spaceOptions={}

  def __init__(self,db_coonection: connection.Conection) -> None:
        self.cursor = db_coonection.cursor 
  
  def moveToSpace(self,optionNumber):
    selectedSpaceId = self.spaceOptions.get(optionNumber,-1)
    if selectedSpaceId == 0:
      return None
    if selectedSpaceId < 0:
      # retry moving
      self.cursor.excute("UPDATE Jogador SET regiao=%s WHERE id=%s;",(selectedSpaceId,self.playerId))
      self.cursor.excute("SELECT nome FROM Jogador WHERE id_regiao=%s;",(selectedSpaceId))
      self.current_region = self.cursor.fetchOne()[0]
      self.cursor.commit()
      return self.getCurrentPosition()
  
  def getCurrentPosition(self):
    self.cursor.execute("SELECT r.id_regiao, r.nome FROM Regiao r JOIN Caminhos c ON c.regiao_destino = r.id_regiao WHERE c.regiao=%s;")
    for it in self.cursor.fetchall():
        if it[0] not in self.spaceOptions:
            self.spaceOptions[it[0]]={'scheme':[]}
        else:
            self.spaceOptions[it[0]]['scheme'].append(it[1])
    print(self.spaceOptions)

  

