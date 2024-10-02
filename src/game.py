from src.clearScreen import ClearScreen
from src.hand import Hand
from src.deck import Deck
from src.table import Table

class Game(ClearScreen):
  def __init__(self):
    self.statistics = {
      'player_wins': 0,
      'dealer_wins': 0,
      'pushes': 0,
      'player_blackjacks': 0,
      'dealer_blackjacks': 0
    }

  def check_blackjack(self, dealer_hand, player_hand):
    if player_hand.is_blackjack() and dealer_hand.is_blackjack():
      check_blackjack_game_end_message = 'Both players have a blackjack. es.'
      self.statistics['pushes'] += 1
      self.statistics['dealer_blackjacks'] += 1
      self.statistics['player_blackjacks'] += 1
    elif player_hand.is_blackjack():
      check_blackjack_game_end_message = 'You have a blackjack. You win.'
      self.statistics['player_wins'] += 1
      self.statistics['player_blackjacks'] += 1
    elif dealer_hand.is_blackjack():
      check_blackjack_game_end_message = 'The dealer has a blackjack. You lose.'
      self.statistics['dealer_wins'] += 1
      self.statistics['dealer_blackjacks'] += 1
    else:
      check_blackjack_game_end_message = ''
    return check_blackjack_game_end_message


  def check_bust(self, dealer_hand, player_hand):
    if player_hand.is_bust():
      check_bust_game_end_message = 'You busted. Dealer wins.'
      self.statistics['dealer_wins'] += 1
    elif dealer_hand.is_bust():
      check_bust_game_end_message = 'Dealer busted. You win.'
      self.statistics['player_wins'] += 1
    else:
      check_bust_game_end_message = ''
    return check_bust_game_end_message

  def check_winner(self, dealer_hand, player_hand):
    if player_hand.is_21() and dealer_hand.is_21():
      check_winner_game_end_message = 'Both players have 21. Push.'
      self.statistics['pushes'] += 1
    elif player_hand.is_21():
      check_winner_game_end_message = 'You have 21. You win.'
      self.statistics['player_wins'] += 1
    elif dealer_hand.is_21():
      check_winner_game_end_message = 'The dealer has 21. You lose.'
      self.statistics['dealer_wins'] += 1
    elif player_hand.get_value() > dealer_hand.get_value():
      check_winner_game_end_message = 'You win.'
      self.statistics['player_wins'] += 1
    elif dealer_hand.get_value() > player_hand.get_value():
      check_winner_game_end_message = 'Dealer wins.'
      self.statistics['dealer_wins'] += 1
    elif player_hand.get_value() == dealer_hand.get_value():
      check_winner_game_end_message = 'Push.'
      self.statistics['pushes'] += 1
    return check_winner_game_end_message
  
  def show_statistics(self):
    self.clear_screen()
    print(f'Player Wins: {self.statistics['player_wins']}')
    print(f'Dealer Wins: {self.statistics['dealer_wins']}')
    print(f'Pushes: {self.statistics['pushes']}')
    print(f'Player Blackjacks: {self.statistics['player_blackjacks']}')
    print(f'Dealer Blackjacks: {self.statistics['dealer_blackjacks']}')
    input('Press return to exit.')
  
  def play(self):
    game_number = 0
    games_to_play = 0
    game_end_message = ''

    # Clear screen
    self.clear_screen()

    while games_to_play <= 0:
      try:
        games_to_play = int(input('How many games would you like to play? '))
      except:
        print('The input needs to be a positive number.')

    while game_number < games_to_play:
      game_number += 1

      # Set up game
      deck = Deck()
      deck.shuffle()

      player_hand = Hand()
      dealer_hand = Hand(True)

      table = Table(game_number, games_to_play, dealer_hand, player_hand)

      # Deal cards
      dealer_hand.add_card(deck.deal(2))
      player_hand.add_card(deck.deal(2))

      # Check for blackjack
      game_end_message = self.check_blackjack(dealer_hand, player_hand)
      table.display_table(game_end_message)

      # Player's turn
      choice = 0
      error = False
      
      while not game_end_message and player_hand.get_value() < 21 and choice != 2:
        try:
          if not error:
            choice = int(input('Enter 1 for hit or 2 for stand: '))
          else:
            error = False
            choice = int(input('Invalid entry. Please enter 1 for hit or 2 for stand: '))
          if choice not in [1, 2]:
            error = True
        except:
          error = True
        
        if choice == 1:
          player_hand.add_card(deck.deal(1))
          game_end_message = self.check_bust(dealer_hand, player_hand)
          if player_hand.get_value() != 21:
            table.display_table(game_end_message)

      # Dealer's turn
      while not game_end_message and dealer_hand.get_value() < 17 and dealer_hand.get_value() <= player_hand.get_value():
        dealer_hand.add_card(deck.deal(1))
        game_end_message = self.check_bust(dealer_hand, player_hand)
        if game_end_message:
          table.display_table(game_end_message)
      
      # Game over
      if not game_end_message:
        game_end_message = self.check_winner(dealer_hand, player_hand)
        table.display_table(game_end_message)

    # Show statistics
    self.show_statistics()