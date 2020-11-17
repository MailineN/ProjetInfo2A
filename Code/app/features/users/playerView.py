""" View correspondant aux méthodes de la classe Player """

from PyInquirer import prompt
from examples import custom_style_2


class PlayerView():
    @staticmethod
    def displayChangePassword():
        questions = [
            {
                'type': 'input',
                'name': 'username',
                'message': 'Entrez votre pseudo : ',
            },
            {
                'type': 'password',
                'name': 'former_mdp',
                'message': 'Entrez votre mot de passe: ',
            },
            {
                'type': 'password',
                'name': 'new_mdp',
                'message': 'Entrez votre nouveau mot de passe : ',

            }
        ]
        print("Votre mot de passe a été modifié : \n")
        res = prompt(questions, style=custom_style_2)
        return(res['username'], res['former_mdp'], res['new_mdp'])

    @staticmethod
    def displayChangeName():
        questions = [
            {
                'type': 'input',
                'name': 'username',
                'message': 'Entrez votre pseudo : ',
            },

            {
                'type': 'password',
                'name': 'former_mdp',
                'message': 'Entrez votre mot de passe : ',
            },
            {
                'type': 'input',
                'name': 'new_mdp',
                'message': 'Entrez votre nouveau pseudo : ',

            }
        ]
        print("Changement de nom d'utilisateur : \n")
        res = prompt(questions, style=custom_style_2)
        return(res['username'], res['former_mdp'], res['new_mdp'])
