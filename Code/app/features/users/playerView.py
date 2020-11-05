""" View correspondant aux méthodes de la classe Player """

from PyInquirer import prompt
from examples import custom_style_2

class PlayerView():
    @staticmethod
    def displayChangePassword():
        questions = [
            {
                'type': 'password',
                'name': 'former_mdp',
                'message': 'Entrez votre nom d\'utilisateur : ',
            },
            {
                'type': 'password',
                'name': 'new_mdp',
                'message': 'Entrez votre mot de passe : ',

            }
        ]
        print("Votre mot de passe a été modifié : \n")
        res = prompt(questions, style=custom_style_2)
        return(res['former_mdp'], res['new_mdp'])
