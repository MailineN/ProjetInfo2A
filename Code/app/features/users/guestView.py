""" Views correspondant aux méthodes de la classe Guest 
    """
from PyInquirer import prompt
from examples import custom_style_2


class GuestView():
    @staticmethod
    def displayConnexion():
        questions = [
            {
                'type': 'input',
                'name': 'Pseudo',
                'message': 'Entrez votre nom d\'utilisateur : ',
            },
            {
                'type': 'password',
                'name': 'Mdp',
                'message': 'Entrez votre mot de passe : ',

            }
        ]
        print("Connection : \n")
        res = prompt(questions, style=custom_style_2)
        return(res['Pseudo'], res['Mdp'])

        def displayCreateAccount():
            questions = [
                {
                    'type': 'input',
                    'name': 'Pseudo',
                    'message': 'Entrez votre nom d\'utilisateur : ',
                },
                {
                    'type': 'password',
                    'name': 'Mdp',
                    'message': 'Entrez votre mot de passe : ',

                },
                {
                    'type': 'password',
                    'name': 'VerifMdp',
                    'message': 'Vérifiez votre mot de passe : ',

                }
            ]
            print("Création de compte : \n")
            res = prompt(questions, style=custom_style_2)
            return(res['Pseudo'], res['Mdp'], res['VerifMdp'])


if __name__ == "__main__":
    GuestView.displayConnexion()
