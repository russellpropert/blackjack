import os

class ClearScreen:
  def clear_screen(self):
    os.system('cls' if os.name == 'nt' else 'clear')