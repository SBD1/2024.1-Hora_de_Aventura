import cmd
from pyfiglet import Figlet

from db.connection import Connection # Importe a classe Connection
from db.seed import create_tables  # Importe a função para criar as tabelas]
from classes_dto import *
from util import *

#import npc
import player

class MyCmd(cmd.Cmd):
    prompt = '(mycmd) '
    trueLastCmd = ''

    def start(self):
      figlet = Figlet(font='slant')
      text = "Hora de Aventura Mud"
      print(figlet.renderText(text))
      print("Bem vindo a Hora de Aventura")
      
      print("Para selecionar a opção basta digitar os comandos citados\n\n\n")
      
      print("criar - Criar um novo personagem")
      print("carregar - Carregar um personagem existente")
      print("help - Menu de ajuda\n\n\n")
      
    def preloop(self):
      self.conn = Connection()
      self.playerClass = player.Player(self.conn)
      
      self.start()
        
    def do_criar(self, line):
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
        
    def do_carregar(self, line):
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

        
    def do_help(self,line):
      self.start()

    def do_move(self,line):
      self.playerClass.getCurrentPosition(self.currentPlayer.id_jogador)
             
    def default(self, line):
        if self.trueLastCmd == 'move':
          self.playerClass.moveToSpace(self,line)
          return None 
        self.trueLastCmd = ''

    def precmd(self, line):
        clear()
        if self.trueLastCmd == '':
          self.trueLastCmd = self.lastcmd
        return line

if __name__ == '__main__':
    create_tables()
    MyCmd().cmdloop()