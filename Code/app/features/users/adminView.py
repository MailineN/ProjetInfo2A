""" Views correspondant aux méthodes de la classe Guest 
    """
from PyInquirer import prompt
from examples import custom_style_2


class AdminView():

    def displayDeleteUserAccount():
        questions = [
            {
                'type': 'input',
                'name': 'Username',
                # ?? jsp si ca se passe comme ca qd c'est un choix
                'message': 'Entrez le nom d\'utilisateur du compte que vous voulez supprimer:',
            },

        ]
        print("Suppression de compte : \n")
        res = prompt(questions, style=custom_style_2)
        return(res['Username'])

    def displaySeeUserAccount():
        questions = [
            {
                'type': 'input',
                'name': 'Username',
                'message': 'Entrez le nom d\'utilisateur du compte que vous voulez consulter:',
            },

        ]
        print("Consultation de compte : \n")
        res = prompt(questions, style=custom_style_2)
        return(res['Username'])

    def displayResetDataBase():
        questions = [
            {
                'type': 'input',
                'name': 'reset',
                'message': 'ATTENTION : Cette action est irréversible. Tapez SUPPRIMER pour confirmer',
            },

        ]
        print("Réinitialisation de la base de donnée : \n")
        res = prompt(questions, style=custom_style_2)
        return(res['reset'])

if __name__ == "__main__":
    AdminView.displayConnexion()  # ?? ca jsp cque ca fait
