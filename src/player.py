from db import connection
from classes_dto import *
from util import *


class Player():
  current_region=""
  current_player={}
  spaceOptions={}
  
  def __init__(self,db_connection: connection.Connection) -> None:
    print("here")
    self.db_connection = db_connection
    self.cursor = db_connection.cursor
    self.commit = db_connection.commit
    self.rollback = db_connection.rollback
  
  def getCurrentPlayer(self, nome):
    player = self.db_connection.get_character(nome)
    self.current_player = CurrentPlayer(player.id_jogador, player.nome, player.regiao, player.missao_atual, player.vida, player.qnt_ouro)
    return player
  
  def new_player(self):
    clear()
    new_name = input('Digite o nome do seu personagem: \n\n')
    if new_name == '':
        print("Não é possível registrar um nome vazio!\n")
        return None
      
    self.currentPlayer = self.getCurrentPlayer(new_name)
    
    print ("Verificando se o nome já está registrado...\n")
    
    while(self.currentPlayer.id_jogador != -1):
        new_name = input('Nome já registrado, escolha outro:\n')
        self.currentPlayer= self.getCurrentPlayer(new_name)
  
    self.db_connection.create_new_character(new_name)
    self.currentPlayer = self.getCurrentPlayer(new_name)
    
    print(
        f'\nSeja bem vindo(a) ao jogo, {new_name}! (Nâo que isso seja um jogo hahaha)')
    print(
        f'Você caiu de paraquedas no mundo de Ooo igual a todos!')
    print(
        f'Não se sinta especial.')
    print(
        f'Me chamo Finn, e este é o meu cachorro Jake!\n')
    print(
        f'Venha, vamos começar a sua jornada!\n')
    input('pressione _enter_ para continuar...')

  def moveToSpace(self, cmdSelf,optionNumber):
    if int(optionNumber) == 0:
      return None
    selectedSpaceId = self.spaceOptions.get(int(optionNumber),-1)

    if selectedSpaceId < 0:
      print("Opção inválida, por favor selecione um destino disponível")
      self.getCurrentPosition()
      return None
    self.cursor.execute("UPDATE Jogador SET regiao=%s WHERE id_jogador=%s;",[selectedSpaceId,self.current_player.id_jogador])
    self.cursor.execute("SELECT nome FROM Regiao WHERE id_regiao=%s;",[selectedSpaceId])
    self.current_region = self.cursor.fetchone()[0]
    self.commit()
    return self.getCurrentPosition()
  
  def getCurrentPosition(self):
    self.current_region = self.db_connection.get_current_region(self.current_player.id_jogador)[1]
    return self.current_region
 
  def getAvailableRegions(self): 
    self.available_regions = self.db_connection.get_available_regions(self.current_player.regiao)

    print(f"Você esta em {self.current_region}, os destinos disponíveis são:")
    print("0 - Cancelar movimento")
    for index, row in enumerate(self.available_regions):
        id, nome = row
        self.spaceOptions[index+1] = id
        print(f"{index+1} - {nome.strip()}")


