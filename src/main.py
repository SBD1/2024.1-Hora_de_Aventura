import cmd
import os
import platform

from db.connection import Conection
import npc
import player

class MyCmd(cmd.Cmd):
    prompt = '(mycmd) '
    trueLastCmd = ''

    def __init__(self) -> None:
        conn = Conection()
        self.player = player.Player(conn.cursor)

    def printMenuAjuda(self):
      print("Bem vindo a Hora de Aventura")
      print("Para selecionar a opção basta digitar os comandos citados")
      print("COMANDO - FUNÇÂO")
      print("example - Exemplo de dialogo")
      print("move - Andar pelo mapa")
      print("help - Menu de ajuda")

    def preloop(self):
      self.printMenuAjuda()

    def default(self, line):
        if self.trueLastCmd == 'example':
          newNpc = npc.Npc() 
          newNpc.example_dialogue_options(self, line)
          return None 
        if self.trueLastCmd == 'move':
          self.player.moveToSpace(self,line)
          return None 
        self.trueLastCmd = ''

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
    MyCmd().cmdloop()