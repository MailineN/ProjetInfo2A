""" Views correspondant aux méthodes de la classe Guest 
    """
from PyInquirer import prompt
from examples import custom_style_2


class AdminView():
        def displayUsertype():
            questions = [                
                {
                    'type': 'input',
                    'name': 'Usertype',
                    'message': 'Voulez-vous créer un Player ou un Admin?',
                    'choices':  [
                            'Player',
                            'Admin'

                    ],
                },
            ]
            print("Le type d\'utilisateur choisi est : \n")
            res = prompt(questions, style=custom_style_2)
            return(res['Usertype'])


        def displayCreateUserAccount():
            questions = [                
                {
                    'type': 'input',
                    'name': 'Pseudo',
                    'message': 'Entrez le nom d\'utilisateur : ',
                },
                {
                    'type': 'password',
                    'name': 'Mdp',
                    'message': 'Entrez le mot de passe : ',

                },
                {
                    'type': 'password',
                    'name': 'VerifMdp',
                    'message': 'Vérifiez le mot de passe : ',

                }
            ]
            print("Création de compte : \n")
            res = prompt(questions, style=custom_style_2)
            return(res['Pseudo'], res['Mdp'], res['VerifMdp'])

        def displayDeleteUserAccount():
            questions = [
                {
                    'type': 'input',
                    'name': 'Username',
                    'message': 'Entrez le nom d\'utilisateur du compte que vous voulez supprimer:', #?? jsp si ca se passe comme ca qd c'est un choix
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
                    'message': 'Entrez le nom d\'utilisateur du compte que vous voulez consulter:', #?? jsp si ca se passe comme ca qd c'est un choix
                },                

            ]
            print("Consultation de compte : \n")
            res = prompt(questions, style=custom_style_2)
            return(res['Username'])




if __name__ == "__main__":
    GuestView.displayConnexion() # ?? ca jsp cque ca fait 
