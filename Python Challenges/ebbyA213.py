import itertools, random

class Deck:
    def __init__(self):
        self.suits = ['Spades','Hearts','Diamonds','Clubs']
        self.values = range(1,14)
        self.cards = []
        for card in itertools.product(self.suits,self.values):
            self.cards.append(card) #Cartesian Product to Create Deck
    def GetRandomCard(self):
        random_card = self.cards[random.randint(0,len(self.cards))]
        del(self.cards.index(random_card))
        return random_card

class Player:
    def __init__(self,ID,Card):
        self.PlayerID = ID
        self.CardForPlayer = Card

class SimpleWar:
    def __init__(self,NumberOfPlayers):
        self.NumberOfPlayers = NumberOfPlayers
        self.PlayerList = []
        
    def StartGame(self):
        DeckOfCards = Deck()
        for playerID in range(0,self.NumberOfPlayers):
            CardForPlayer = DeckOfCards.GetRandomCard()
            NewPlayer = Player(playerID,CardForPlayer)
            self.PlayerList.append(NewPlayer)
        self.DecideWinner()
        
    def DecideWinner(self):
        WinningID = self.PlayerList[0]
        for playerID in self.PlayerList:
            if(playerID.CardForPlayer[1]>WinningID.CardForPlayer[1]):
                WinningID = playerID
        print ("Winner is Player "+str(WinningID.PlayerID))
        print ("Their Card was "+ str(WinningID.CardForPlayer[1]) + " of " + str(WinningID.CardForPlayer[0]))

NewGame = SimpleWar(2)
NewGame.StartGame()
    
