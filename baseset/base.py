from entity.cards import Card
from entity.cards import Action 
from entity.cards import Coin 
from entity.cards import Green 
from entity.cards import GameBoard

#Deck is a tuple of card definitions and counts
village = Action("Village", 2, 0, 1, 0, None)
market = Action("Market", 1, 1, 1, 1, None)
smithy = Action("Smithy", 0, 0, 3, 0, None)
moat = Action("Moat", 0, 0, 2, 0, None)
wood_cutter = Action("Moat", 0, 0, 2, 0, None)
cellar = Action("Cellar", 0, 0, 1, 0, None)
workshop = Action("Workshop", 0, 0, 0, 0, None)
remodel = Action("Remodel", 0, 0, 0, 0, None)
militia = Action("Militia", 0, 0, 0, 2, None)
mine = Action("Mine", 0, 0, 0, 0, None)

#Intialize Game 
game_state = GameBoard()
game_state.action_decks['village'] = (village,10)
game_state.action_decks['market'] = (market,10)
game_state.action_decks['smithy'] = (smithy,10)
game_state.action_decks['moat'] = (moat,10)
game_state.action_decks['wood_cutter'] = (wood_cutter,10)
game_state.action_decks['cellar'] = (cellar,10)
game_state.action_decks['workshop'] = (workshop,10)
game_state.action_decks['militia'] = (militia,10)
game_state.action_decks['mine'] = (mine,10)
game_state.action_decks['remodel'] = (remodel,10)



