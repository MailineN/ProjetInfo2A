from .menu_interface import MenuInterface
from app.features.users.individu import Individu
from app.features.users.guest import Guest
from app.features.users.player import Player


def connexion(previous_menu):
    """Menu intermédiaire de connection proposant à l'utilisateur de se connecter s'il ne l'est pas 
    Arguments:
        previous_menu {liste} -- Menu précédent de l'utilisateur spécifié 
    """
    menu_act = previous_menu

    if menu_act["individu"].connexion():
        del menu_act["options"][0]
        del menu_act["actions"][0]

    return((lambda previous_menu: indices_actions(Player(), [1, 4, 9, 10])))


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
    return(MenuInterface(menu_act))


def menuChoixJeu(previous_menu):
    menu_act = {}
    menu_act["individu"] = previous_menu["individu"]
    menu_act["question"] = "A quel jeu voulez vous jouer ? "
    menu_act["options"] = ["Belote",
                           "Retour au menu principal",
                           "Quitter l'application"]
    menu_act["actions"] = [
        menuChoixGroupeBelote
        (lambda previous_menu:MenuInterface(menu[0])),
        Individu().quitter]
    menu_act["path"] = []
    return(MenuInterface(menu_act))


def menuChoixGroupeBelote(previous_menu):
    menu_act = {}
    menu_act["individu"] = previous_menu["individu"]
    menu_act["question"] = "Que voulez vous faire ? "
    menu_act["options"] = ["Créer un groupe de joueurs",
                           "Rejoindre un groupe de jouers",
                           "Revenir au menu précédent"
                           "Quitter l'application"]
    menu_act["actions"] = [
        (lambda previous_menu:previous_menu["individu"].initEmptyGame()),
        (lambda previous_menu:previous_menu["individu"].joinGame()),
        menuChoixJeu,
        Individu().quitter]
    menu_act["path"] = []
    return(MenuInterface(menu_act))


def menuPlayer(previous_menu):
    menu_act = {}
    menu_act["individu"] = previous_menu["individu"]
    menu_act["question"] = "Que voulez vous faire ? "
    menu_act["options"] = ["Jouer",  # 2
                           "Consulter vos statistiques",
                           "Modifier vos informations",
                           "Retour au menu principal",
                           "Quitter l'application"]
    menu_act["actions"] = [
        menuChoixJeu,
        menuStatistiques,
        menuModif,
        (lambda previous_menu:MenuInterface(menu[0])),
        Individu().quitter]
    menu_act["path"] = []
    return(MenuInterface(menu_act))


def menuStatistiques(previous_menu):
    menu_act = {}
    menu_act["individu"] = previous_menu["individu"]
    menu_act["question"] = "Pour quel jeu voulez vous consulter vos statistiques ? "
    menu_act["options"] = ["Belote",  # 2
                           "Retour au menu précédent",
                           "Quitter l'application"]
    menu_act["actions"] = [
        # Statistiques belote,
        (lambda previous_menu:MenuInterface(menu[0])),
        Individu().quitter]
    menu_act["path"] = []
    return(MenuInterface(menu_act))


def menuModif(previous_menu):
    menu_act = {}
    menu_act["individu"] = previous_menu["individu"]
    menu_act["question"] = "Que voulez vous modifier ? "
    menu_act["options"] = ["Nom public",  # 2
                           "Mot de passe",
                           "Retour au menu précédent"
                           "Quitter l'application"]
    menu_act["actions"] = [
        # Modif nom
        # Modif mdp
        (lambda previous_menu:MenuInterface(menu[0])),
        Individu().quitter]
    menu_act["path"] = []
    return(MenuInterface(menu_act))


menu = [
    {
        "question": "Selectionnez votre statut ?",
        "options": ["Invité", "Joueur", "Quitter l'application"],
        "actions": [
            (lambda previous_menu:indices_actions(Guest(), [1, 2, 3])),
            (lambda previous_menu:indices_actions(Player(), [0, 1, 2, 3])),
            connexion, menuChoixJeu, Individu().quitter],

        "individu": Individu(),
        "path": []
    },


    {
        "question": "Que voulez vous faire ? ",
        "options": [
            "Connexion",  # 0
            "Jouer",  # 1
            "Créer un compte"
            "Voir ses statistiques",
            "Gérer la base de donnée"
            "Ajouter un jeu"
            "Revenir au menu précédent",  # 7
            "Quitter l'application"],  # 8
        "actions": [
            connexion,
            menuChoixJeu,
            #(lambda previous_menu:previous_menu["individu"].reprendre(previous_menu))
            (lambda previous_menu:previous_menu["individu"].creerCompte(
                previous_menu)),
            (lambda previous_menu:previous_menu["individu"].voirStat(
                previous_menu)),
            (lambda previous_menu:previous_menu["individu"].gestionBase(
                previous_menu)),
            (lambda previous_menu:previous_menu["individu"].ajoutJeu(
                previous_menu)),
            (lambda previous_menu:MenuInterface(menu[0])),
            Individu().quitter],
        "individu": Individu(),
        "path": []
    }]
"""Menu principal et menu utilisateur proposant l'ensemble des actions possibles
"""
