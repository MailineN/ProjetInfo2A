""" Views correspondant aux méthodes de la classe Guest 
    """
from PyInquirer import prompt
from examples import custom_style_2


class AdminView():
        def displaydisplayCreateUserAccount():
            questions = [
                {
                    'type': 'input',
                    'name': 'Usertype',
                    'message': 'Voulez-vous créer un Player ou un Admin?', #?? jsp si ca se passe comme ca qd c'est un choix
                },                
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
            return(res['Usertype'], res['Pseudo'], res['Mdp'], res['VerifMdp'])

        def displayDeleteUserAccount():
            questions = [
                {
                    'type': 'input',
                    'name': 'Usertype',
                    'message': 'Voulez-vous créer un Player ou un Admin?', #?? jsp si ca se passe comme ca qd c'est un choix
                },                
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
            return(res['Usertype'], res['Pseudo'], res['Mdp'], res['VerifMdp'])




if __name__ == "__main__":
    GuestView.displayConnexion() # ?? ca jsp cque ca fait 
