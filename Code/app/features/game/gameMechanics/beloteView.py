"""Méthodes views correspondant au jeu de la belote
    """
from PyInquirer import prompt
from examples import custom_style_2
from pyfiglet import Figlet

from app.features.utils import *

from app.features.game.cardObjects.cards import Card


class BeloteView():

    @staticmethod
    def displayTourAppel(player, carteAppel):
        question1 = [
            {
                'type': 'list',
                'message': str(player.identifiant) + ': Voulez vous prendre ?',
                'name': 'pose',
                'choices':  [
                        'Oui',
                        'Non'
                ],
            },
        ]
        print("Carte d'appel : ")
        print(str(carteAppel))
        print("Vous avez ces cartes: \n")
        for card in player.handList:
            print("• "+str(card)+"\n")

        rep = prompt(question1, style=custom_style_2)
        if (rep['pose'] == 'Oui'):
            return True
        else:
            return False

    @staticmethod
    def displayTourAppel2(player):
        rep = ""
        question1 = [
            {
                'type': 'list',
                'message': str(player.identifiant) + ': Voulez vous prendre ?',
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
        for card in player.handList:
            print("• "+str(card)+"\n")
        rep = prompt(question1, style=custom_style_2)
        if (rep['pose'] == 'Oui'):
            color = prompt(question2, style=custom_style_2)
            if (color['couleur'] == 'PIQUES'):
                return(True, "SPADES")
            elif (color['couleur'] == 'COEUR'):
                return(True, "HEARTS")
            elif (color['couleur'] == 'TREFLES'):
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
        print("• {} et {}\n".format(
            team1[0].identifiant, team1[1].identifiant))
        print("• {} et {}\n".format(
            team2[0].identifiant, team2[1].identifiant))
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
        question = [
            {
                'type': 'list',
                'message': 'Voulez vous continuer ?',
                'name': 'choix',
                'choices': ['Oui', 'Non']
            }
        ]
        rep = prompt(question, style=custom_style_2)
        return(rep['choix'])

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
    def displayPoser(player, plis):

        question = [
            {
                'type': 'list',
                'message': str(player.identifiant) + ': Quelle carte voulez vous poser ?',
                'name': 'pose',
                'choices': [str(i)+". "+str(player.handList[i])for i in range(len(player.handList))]
            }
        ]
        print("Vous avez ces cartes : \n")
        for card in player.handList:
            print("• "+str(card))
        print("Les cartes du plis sont : ")
        if len(plis) == 0:
            print("Vous êtes maitre, posez ce que vous voulez \n")
        else:
            for card in plis:
                print("• "+str(card))
        rep = prompt(question, style=custom_style_2)
        index = int(rep['pose'][0])
        print(index)
        return(player.handList[index])
