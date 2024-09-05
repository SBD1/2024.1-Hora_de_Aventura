import cmd
import os
import platform

from db.connection import Conection
import npc
import player
from db.seed import create_tables  # Importe a função para criar as tabelas

class MyCmd(cmd.Cmd):
    prompt = '(mycmd) '
    trueLastCmd = ''        

    def printMenuAjuda(self):
      print("Bem vindo a Hora de Aventura")
      print("Para selecionar a opção basta digitar os comandos citados\n\n\n")
      
      print("criar - Criar um novo personagem")
      print("carregar - Carregar um personagem existente")
      print("help - Menu de ajuda\n\n\n")
      
      while True:
        print("Digite o comando desejado")
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
        print("Comando inválido, tente novamente")

    def preloop(self):
      self.conn = Conection()
      self.player = player.Player(self.conn)
      self.printMenuAjuda()
        
    def create_new_character(self):
        new_name = input('Digite o nome do seu personagem: ')
        if new_name == '':
            print("Não é possível registrar um nome vazio!")
            return None
        self.conn.create_new_character(new_name)

    def precmd(self, line):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        if self.trueLastCmd == '':
          self.trueLastCmd = self.lastcmd
        return line

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