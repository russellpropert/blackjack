class Hand():
  def __init__(self, dealer = False):
    self.cards = []
    self.value = 0
    self.dealer = dealer

  def add_card(self, card_list: list):
    self.cards.extend(card_list)

  def check_for_aces(self, card):
    if card.rank['rank'] == 'A':
      return 1
    else:
      return 0

  def calculate_ace_value(self, aces):
    for ace in range(aces):
      if self.value > 21:
        self.value -= 10
  
  def calculate_value(self):
    self.value = 0 
    aces = 0
    for card in self.cards:
      self.value += int(card.rank['value'])
      aces += int(self.check_for_aces(card))
    if aces and self.value > 21:
      self.calculate_ace_value(aces)

  def get_value(self):
    self.calculate_value()
    return self.value
  
  def is_blackjack(self):
    return self.get_value() == 21 and len(self.cards) == 2
  
  def is_21(self):
    return self.get_value() == 21 and len(self.cards) > 2
  
  def is_bust(self):
    return self.get_value() > 21
  
  def display(self, show_all_dealer_cards = False):
    print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
    for index, card in enumerate(self.cards):
      if index == 0 \
        and self.dealer \
        and not show_all_dealer_cards \
        and not self.is_blackjack():
        print('Hidden')
      else:
        print(card)
    if not self.dealer or self.dealer and show_all_dealer_cards:
      print(f'Value: {self.get_value()}')