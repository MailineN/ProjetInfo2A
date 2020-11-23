"""Ce fichier sert à tester des fonctions individuelles du code 

    """
from app.features.game.cardObjects.deck import PileCard


deck = PileCard.generateNewCustomDeck("7S,7D,7C,7H,8S,8D,8C,8H,9S,9D,9C,9H,0S,0D,0C,0H,JS,JD,JC,JH,QS,QD,QC,QH,KS,KD,KC,KH,AS,AD,AC,AH")

for i in range(32):
    carteAppel = deck.drawDeck(1)[0]
    print(str(i+1)+ " " + str(carteAppel))
