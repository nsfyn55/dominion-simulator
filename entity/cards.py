class Card:
  def __init__(self):
    pass

class Action(Card):

  def __init__(self, 
               card_name, 
               action_modifier,
               buy_modifier, 
               card_modifier, 
               coin_modifier, 
               custom_behavior):

    self.card_name       = card_name
    self.action_modifier = action_modifier
    self.buy_modifier    = buy_modifier
    self.card_modifier   = card_modifier
    self.coin_modifier   = coin_modifier

  def __str__(self):
    strRepr = "[card_name:%s],[action_modifier:%s]," \
    "[buy_modifier:%s],[card_modifier:%s]" \
      % (self.card_name, self.action_modifier, 
          self.buy_modifier, self.card_modifier)
    return strRepr
      
class Coin(Card):
  def __init__(self, value):
    pass

class Green(Card):
  def __init__(self, value):
    pass

class GameBoard:
 #tuples of custom cards and count
 action_decks = {} 
 def __init__(self):
   self.province_count = 8
   self.duchy_count = 8
   self.estate_count = 8
   self.gold_count = 30
   self.silver_count = 40 
   self.copper_count = 46 
 
 def __str__(self):
    strRepr = "[province_count:%s]," \
    "[duchy_count:%s],[estate_count:%s]" \
    "[gold_count:%s],[silver_count:%s]" \
    "[copper_count:%s],[action_decks:%s]" \
      % (self.province_count, self.duchy_count, 
          self.estate_count, self.gold_count,
          self.silver_count, self.copper_count,
          self.action_decks)
    return strRepr
 
