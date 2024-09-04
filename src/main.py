import cmd
import os
import platform

from db.connection import Conection
import npc
import player

class MyCmd(cmd.Cmd):
    prompt = '(mycmd) '
    trueLastCmd = ''        

    def printMenuAjuda(self):
      print("Bem vindo a Hora de Aventura")
      print("Para selecionar a opção basta digitar os comandos citados\n\n\n")
      
      print("criar - Criar um novo personagem")
      print("carregar personagem - Carregar um personagem existente")
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

    def default(self, line):
        if self.trueLastCmd == 'criar':
          self.create_new_character()
          return None 
        if self.trueLastCmd == 'move':
          self.player.moveToSpace(self,line)
          return None 
        self.trueLastCmd = ''
        
    def create_new_character(self):
        new_name = input('Digite o nome do seu personagem: ')
        if new_name == '':
            print("Não é possível registrar um nome vazio!")
            return None
        # self.player = Conection.get_character(self.connection, new_name)
        # while(self.player.idJogador != -1):
        #     new_name = input('Nome já registrado, escolha outro:')
        #     self.player = DataBase.get_character(self.connection, new_name)
        ## Fazer a conexão com o banco de dados AQUI
        Conection.create_new_character(self.conn, new_name)

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