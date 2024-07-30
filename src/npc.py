import os
import platform

class Npc():
  def example_dialogue(self):
    print("Esse é um exemplo de dialogo")
    print("Selecione uma das opções:")
    print("1 - Numero 1")
    print("2 - Numero 2")
    print("3 - Numero 3")
    
  def example_dialogue_options(self, cmdSelf,options):
    arr = ['1','2','3']
    try:
      optionSelected = arr.index(options)
      if optionSelected == 0:
        print("opção 1")
      if optionSelected == 1:
        print("opção 2")
      if optionSelected == 2:
        print("opção 3")
      cmdSelf.trueLastCmd = ''
    except Exception as e:
      if platform.system() == 'Windows':
        os.system('cls')
      else:
        os.system('clear')
      cmdSelf.trueLastCmd = 'example'
      self.example_dialogue()