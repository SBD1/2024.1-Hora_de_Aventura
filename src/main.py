import cmd
import os
import platform

import npc
import player

class MyCmd(cmd.Cmd):
    prompt = '(mycmd) '
    trueLastCmd = ''

    def default(self, line):
        if self.trueLastCmd == 'example':
          newNpc = npc.Npc() 
          newNpc.example_dialogue_options(self, line)
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

if __name__ == '__main__':
    MyCmd().cmdloop()