import cmd
import os
import platform
from pyfiglet import Figlet

from db.connection import Connection # Importe a classe Connection
from db.seed import create_tables  # Importe a função para criar as tabelas]
from classes import *

#import npc
import player

def clear():
  if platform.system() == 'Windows':
    os.system('cls')
  else:
    os.system('clear')

class MyCmd(cmd.Cmd):
    prompt = '(mycmd) '
    trueLastCmd = ''        
    
    def artAscii(self):
      # Cria uma instância do Figlet
      figlet = Figlet(font='slant')  # Você pode escolher outros estilos de fonte

      # Texto que você deseja converter
      text = "Hora de Aventura Mud"

      # Gera o texto em ASCII
      ascii_art = figlet.renderText(text)
      
      return ascii_art

    def start(self):
      print(self.artAscii())
      print("Bem vindo a Hora de Aventura")
      
      print("Para selecionar a opção basta digitar os comandos citados\n\n\n")
      
      print("criar - Criar um novo personagem")
      print("carregar - Carregar um personagem existente")
      print("help - Menu de ajuda\n\n\n")
      
      while True:
        print("Digite o comando desejado\n")
        cmd = input()
        if cmd == 'criar':
          self.create_new_character()
          break
        if cmd == 'carregar':
          self.load_character()
          break
        if cmd == 'help':
          self.do_help()
          break
        print("Comando inválido, tente novamente\n")

    def preloop(self):
      self.conn = Connection()
      self.playerClass = player.Player(self.conn)
      
      self.start()
        
    def create_new_character(self):
        clear()
        new_name = input('Digite o nome do seu personagem: \n\n')
        if new_name == '':
            print("Não é possível registrar um nome vazio!\n")
            return None
          
        self.currentPlayer= self.playerClass.getCurrentPlayer(new_name)
        
        print ("Verificando se o nome já está registrado...\n")
        
        while(self.currentPlayer.id_jogador != -1):
            new_name = input('Nome já registrado, escolha outro:\n')
            self.currentPlayer= self.playerClass.getCurrentPlayer(new_name)
     
        self.conn.create_new_character(new_name)
        self.currentPlayer= self.playerClass.getCurrentPlayer(new_name)
        
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
        self.gameplay()
        
    def load_character(self):
      clear()      
      nome = input('Digite o nome do personagem que deseja carregar ou digite o comando: ')
      self.currentPlayer= self.playerClass.getCurrentPlayer(nome)
      while(self.currentPlayer.id_jogador == -1):
            if nome == 'sair':
                self.start()
            nome = input("Jogador não encontrado! digite outro ou sair: ")
            self.currentPlayer= self.playerClass.getCurrentPlayer(nome)
      
      print(
            f'\nBem vindo de volta, {self.currentPlayer.nome}\n')
      input('pressione _enter_ para continuar...')
      self.gameplay()
        
    def gameplay(self):
        clear()
        self.show_player_info()
  
    def do_example(self, line):
      self.trueLastCmd = 'example'
      newNpc = npc.Npc()
      newNpc.example_dialogue()
      print("finished", self.trueLastCmd)

    def do_help(self,line):
      self.start()

    def do_move(self,line):
      self.playerClass.getCurrentPosition(self.currentPlayer.id_jogador)
             
    def show_player_info(self):  
      print(f'Nome: {self.currentPlayer.nome}\n' +
      f'PV(Pontos de vida): {self.currentPlayer.vida}\n' +
      f'Quantidade de ouro: {self.currentPlayer.qnt_ouro}\n' +
      f'Você está em: {self.playerClass.getCurrentPosition()}\n' +
      f'\n\n'
      )


if __name__ == '__main__':
    create_tables()
    MyCmd().cmdloop()