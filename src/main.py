import cmd
import os
import platform
from pyfiglet import Figlet

from db.connection import Connection # Importe a classe Connection
from db.seed import create_tables  # Importe a função para criar as tabelas]
from classes import *

import npc
import player

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

    def printMenuAjuda(self):
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
          self.trueLastCmd = 'carregar personagem'
          break
        if cmd == 'help':
          self.do_help()
          break
        print("Comando inválido, tente novamente\n")

    def preloop(self):
      self.conn = Connection()
      self.player = player.Player(self.conn)
      self.printMenuAjuda()
        
    def create_new_character(self):
        new_name = input('Digite o nome do seu personagem: \n\n')
        if new_name == '':
            print("Não é possível registrar um nome vazio!\n")
            return None
          
        self.jogador = self.conn.get_character(new_name)
        
        print ("Verificando se o nome já está registrado...\n")
        while(self.jogador.id_jogador != -1):
            new_name = input('Nome já registrado, escolha outro:\n')
            self.jogador = self.conn.get_character(new_name)
     
        self.conn.create_new_character(new_name)
        self.jogador = self.conn.get_character(new_name)
        
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
        self.precmd()

    def precmd(self):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        if self.trueLastCmd == '':
          self.trueLastCmd = self.lastcmd
   
    def do_example(self, line):
      self.trueLastCmd = 'example'
      newNpc = npc.Npc()
      newNpc.example_dialogue()
      print("finished", self.trueLastCmd)

    def do_help(self,line):
      self.printMenuAjuda()

    def do_move(self,line):
        self.player.getCurrentPosition()


if __name__ == '__main__':
    create_tables()
    MyCmd().cmdloop()