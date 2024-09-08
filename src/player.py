from db import connection
from classes import *

class Player():
  current_region=""
  current_player={}
  playerId=1 #Hardcoded por enquanto
  spaceOptions={}
  

  def __init__(self,db_connection: connection.Connection) -> None:
    self.db_connection = db_connection
    self.cursor = db_connection.cursor
    self.commit = db_connection.commit
    self.rollback = db_connection.rollback
  
  def getCurrentPlayer(self, nome):
    player = self.db_connection.get_character(nome)
    self.current_player = CurrentPlayer(player.id_jogador, player.nome, player.regiao, player.missao_atual, player.vida, player.qnt_ouro)
  
    return player
    
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
    self.current_region = self.db_connection.get_current_region(self.current_player.id_jogador)
    return self.current_region[1]
 
  def getAvailableRegions(self): 
    self.available_regions = self.db_connection.get_available_regions()
    print("Os destinos disponíveis são:")
    print("0 - Cancelar movimento")
    # TODO: Fazer um loop para printar as opções
    
    

