class GameService :

    def __init__(self,score = [0,0],PileList,HandList,PlayerList) :

        self.score = score
        self.PileList = PileList
        self.HandList = HandList
        self.PlayerList = PlayerList

    def DisplayGameState(self) :

        print(self.score,self.PileList,self.HandList,self.PlayerList)

