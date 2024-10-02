from src.clearScreen import ClearScreen

class Table(ClearScreen):
  def __init__(self, game_number, games_to_play, dealer_hand, player_hand):
    self.game_number = game_number
    self.games_to_play = games_to_play
    self.dealer_hand = dealer_hand
    self.player_hand = player_hand
  
  def display_table(self, game_end_message):
    self.clear_screen()
    if game_end_message:
      show_all_dealer_cards = True
    else:
      show_all_dealer_cards = False
    number_of_asterisks = 15
    print()
    print(f'Game {self.game_number} of {self.games_to_play}')
    print('*' * number_of_asterisks)
    self.dealer_hand.display(show_all_dealer_cards)
    print()
    self.player_hand.display()
    print('*' * number_of_asterisks)
    if game_end_message:
      print(game_end_message)
      input('Press return to continue.')