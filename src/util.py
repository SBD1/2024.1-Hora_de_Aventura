import platform
import os

def clear():
  if platform.system() == 'Windows':
    os.system('cls')
  else:
    os.system('clear')