from .menu_interface import Menu_Interface
from app.features.users.individu import Individu


def connexion(previous_menu):
    """Menu intermédiaire de connection proposant à l'utilisateur de se connecter s'il ne l'est pas 
    Arguments:
        previous_menu {liste} -- Menu précédent de l'utilisateur spécifié 
    """
    menu_act = previous_menu

    if menu_act["individu"].connexion():
        del menu_act["options"][0]
        del menu_act["actions"][0]

    return((lambda previous_menu: indices_actions(User(), [1, 4, 9, 10])))


def indices_actions(ind, indice_taches):
    """Définit les actions possibles pour chaques classes dans le menu 
    Différent des indices d'appel de critère utilisés dans certaines fonctions
    Arguments:
        ind {Individu.class} -- Individu spécifié ayant des actions propres
        indice_taches {List} -- Liste des toutes les taches possibles
    """
    menu_act = {}
    menu_act["individu"] = ind
    menu_act["question"] = menu[1]["question"]
    menu_act["options"] = [menu[1]["options"][i] for i in indice_taches]
    menu_act["actions"] = [menu[1]["actions"][i] for i in indice_taches]
    menu_act["path"] = []
    return(Menu_Interface(menu_act))


""" def menu_age_des(previous_menu): 
    Exemple laissé pour démo
    menu_act = {}
    menu_act["individu"] = menu_act["individu"] = previous_menu["individu"]
    menu_act["question"] = "Selectionnez la tranche d'âge"
    menu_act["options"] = ["0-14 ans", #2
        "15-24 ans", #3
        "25-54 ans", #4
        "55-64 ans", #5
        "65 ans et plus", #6
        "Retour au menu précédent",
        "Quitter l'application"]
    menu_act["actions"] = [
            (lambda previous_menu :previous_menu["individu"].description('Classe des 0-14 ans',previous_menu)),
            (lambda previous_menu :previous_menu["individu"].description('Classe des 15-24 ans',previous_menu)),
            (lambda previous_menu :previous_menu["individu"].description('Classe des 25-54 ans',previous_menu)), # 
            (lambda previous_menu :previous_menu["individu"].description('Classe des 55-64 ans',previous_menu)),
            (lambda previous_menu :previous_menu["individu"].description('Classe des plus de 65 ans',previous_menu)),
            menu_des,
            Individu().quitter]
    menu_act["path"] = []
    return(Menu_Interface(menu_act)) """

menu = [
    {
        "question": "Que voulez vous faire ?",
        "options": ["Connexion", "Création de compte", "Jouer en tant qu'invité", "Quitter l'application"],
        "actions": [
            connexion, Individu().quitter],
        """ (lambda previous_menu :indices_actions(User(),[1,4,9,10])),
            (lambda previous_menu :indices_actions(Admin(),[0,1,2,3,5,6,7,8,9,10])), """

        "individu": Individu(),
        "path": []
    },


    {
        "question": "Que voulez vous faire ? ",
        "options": ["Jouer",
                    "Consulter vos statistiques",  # 0
                    "Gestion de la base de donnée (admin seulement)",  # 1
                    "Ajouter un jeu (admin seulement)",  # 2
                    "Quitter l'application"],  # 3
        "actions": [
            Individu().quitter],
        "individu": Individu(),
        "path": []
    }]
"""Menu principal et menu utilisateur proposant l'ensemble des actions possibles
"""
