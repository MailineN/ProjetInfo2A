" Méthodes view de la classe Hand "

from PyInquirer import prompt
from examples import custom_style_2

from app.features.utils import *

from app.features.game.cardObjects.cards import Card


class HandView():

    @staticmethod
    def displayPoser(hand):

        question = [
            {
                'type': 'list',
                'message': 'Quelle carte voulez vous poser ?',
                'name': 'pose',
                'choices': [str(i)+". "+str(hand[i])for i in range(len(hand))]
            }
        ]
        print("Vous avez ces cartes : \n")
        for card in hand:
            print("• "+str(card)+"\n")

        rep = prompt(question, style=custom_style_2)
        index = int(rep['pose'][0])
        return(hand[index])
