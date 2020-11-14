"""Méthodes views correspondant au jeu de la belote
    """
from PyInquirer import prompt
from examples import custom_style_2
from pyfiglet import Figlet

from app.features.utils import *

from app.features.game.cardObjects.cards import Card


class BeloteView():

    @staticmethod
    def displayTourAppel(hand, carteAppel):
        question1 = [
            {
                'type': 'list',
                'message': 'Voulez vous prendre ?',
                'name': 'pose',
                'choices':  [
                        'Oui',
                        'Non'
                ],
            },
        ]
        print("Vous avez ces cartes: \n")
        for card in hand:
            print("• "+str(card)+"\n")

        rep = prompt(question1, style=custom_style_2)
        if (rep == 'Oui'):
            return True
        return False

    @staticmethod
    def displayTourAppel2(hand, carteAppel):
        rep = ""
        question1 = [
            {
                'type': 'list',
                'message': 'Voulez vous appeler ?',
                'name': 'pose',
                'choices':  [
                    'Oui',
                    'Non'
                ],
            },
        ]
        question2 = [
            {
                'type': 'list',
                'message': 'Quelle couleur souhaitez vous appeler ?',
                'name': 'couleur',
                'choices':  [
                    'COEUR',
                    'CARREAU',
                    'TREFLES',
                    'PIQUES'
                ],
            },
        ]
        print("Vous avez ces cartes : \n")
        for card in hand:
            print("• "+str(card)+"\n")
        rep = prompt(question1, style=custom_style_2)
        if (rep['pose'] == 'Oui'):
            color = prompt(question2, style=custom_style_2)
            if (color == 'PIQUES'):
                return(True, "SPADES")
            elif (color == 'COEUR'):
                return(True, "HEARTS")
            elif (color == 'TREFLES'):
                return(True, "CLUBS")
            else:
                return(True, "DIAMONDS")

        return (False, None)

    @staticmethod
    def displayNewGame(team1, team2):
        clear()
        display = Figlet(font='big')
        print(display.renderText('Belote :'))
        print(" ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ \n")
        print("Les équipes sont : \n")
        print("• {} et {}\n".format(team1[0], team1[1]))
        print("• {} et {}\n".format(team2[0], team2[1]))
        print("Les cartes ont étés distribuées, la partie peut commencer !")

    @staticmethod
    def displayRedistrib():
        print("Aucun joueur n'a appelé, le deck va donc être redistribué. \n")
        print(" ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ \n")

    @staticmethod
    def displayAtoutPris(team: str, atout):
        print(team+"a pris à " + atout + "\n")
        print("Le reste du deck va donc être distribué\n")

    @staticmethod
    def displayFinTour(joueurGagnant, cartesPlis):
        print(joueurGagnant + " remporte le pli\n")
        print("Les cartes jouées sont : \n")
        print(str(carte) for carte in cartesPlis)

    @staticmethod
    def displayFinPartie(points):
        print("Le décompte des points est le suivant : \n")
        print("• "+"Team 1 :" + points[0] + "\n")
        print("• "+"Team 2 :" + points[1] + "\n")
        if points[0] > points[1]:
            print("Team 1 remporte donc la partie ! \n")
        else:
            print("Team 2 remporte donc la partie ! \n")
        print(" ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ \n")

    @staticmethod
    def displaySauvegarderJeu(joueurs):
        print(" ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ \n")
        print("La partie est maintenant terminée \n")
        print("Si vous êtes connectés, vous pouvez sauvegarder vos scores \n")
        questions = [
            {
                'type': 'confirm',
                'message': joueurs[0].nom + 'Voulez vous sauvegarder votre partie ?',
                'default': False
            },
            {
                'type': 'confirm',
                'message': joueurs[1].nom + 'Voulez vous sauvegarder votre partie ?',
                'default': False
            },
            {
                'type': 'confirm',
                'message': joueurs[2].nom + 'Voulez vous sauvegarder votre partie ?',
                'default': False
            },
            {
                'type': 'confirm',
                'message': joueurs[3].nom + 'Voulez vous sauvegarder votre partie ?',
                'default': False
            },
        ]
        answers = prompt(questions, style=custom_style_2)
        return(answers)

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
        print(index)
        return(hand[index])
