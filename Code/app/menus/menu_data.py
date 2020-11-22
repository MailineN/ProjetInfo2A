from .menu_interface import MenuInterface
from app.features.users.individu import Individu
from app.features.users.guest import Guest
from app.features.users.admin import Admin
from app.features.users.player import Player,  GameService


def connexion(previous_menu):
    """Menu intermédiaire de connection proposant à l'utilisateur de se connecter s'il ne l'est pas
    Arguments:
        previous_menu {liste} -- Menu précédent de l'utilisateur spécifié
    """
    menu_act = previous_menu
    id_users = menu_act["individu"].connexion()
    if id_users:
        del menu_act["options"][0]
        del menu_act["actions"][0]

    return(MenuInterface(menu_act))


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
        (lambda previous_menu:GameService.initEmptyGame('Belote', previous_menu)),
        (lambda previous_menu:MenuInterface(menu[0])),
        Individu().quitter]
    menu_act["path"] = []
    return(MenuInterface(menu_act))


def menuChoixJeuReprise(previous_menu):
    menu_act = {}
    menu_act["individu"] = previous_menu["individu"]
    menu_act["question"] = "A quel jeu voulez vous jouer ? "
    menu_act["options"] = ["Belote",
                           "Retour au menu principal",
                           "Quitter l'application"]
    menu_act["actions"] = [
        (lambda previous_menu:GameService.initPreviousGame('Belote', previous_menu)),
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
                           "Retour au menu précédent",
                           "Quitter l'application"]
    menu_act["actions"] = [
        (lambda previous_menu:previous_menu["individu"].changeUsername(
            previous_menu)),
        (lambda previous_menu:previous_menu["individu"].changePassword(
            previous_menu)),
        (lambda previous_menu:MenuInterface(menu[0])),
        Individu().quitter]
    menu_act["path"] = []
    return(MenuInterface(menu_act))


def menuAjoutJeu():
    pass


def menuBase(previous_menu):
    menu_act = {}
    menu_act["individu"] = previous_menu["individu"]
    menu_act["question"] = "Que voulez vous consulter ? "
    menu_act["options"] = ["Utilisateurs",  # 2
                           "Précédentes parties ",
                           "Ajouter un administrateur",
                           "Supprimer un utilisateur",
                           "Effacer la base de données",
                           "Retour au menu précédent",
                           "Quitter l'application"]
    menu_act["actions"] = [
        (lambda previous_menu:previous_menu["individu"].seeUserData(
            previous_menu)),
        (lambda previous_menu:previous_menu["individu"].seeGameData(
            previous_menu)),
        (lambda previous_menu:previous_menu["individu"].createAdminAccount(
            previous_menu)),
        (lambda previous_menu:previous_menu["individu"].deleteUserAccount(
            previous_menu)),
        (lambda previous_menu:previous_menu["individu"].resetDatabase(
            previous_menu)),
        (lambda previous_menu:MenuInterface(menu[0])),
        Individu().quitter]
    menu_act["path"] = []
    return(MenuInterface(menu_act))


menu = [
    {
        "question": "Que voulez vous faire ?",
        "options": ["Menu Joueur", "Jouer", "Menu Administrateur", "Quitter l'application"],
        "actions": [
            (lambda previous_menu:indices_actions(
                Player(), [1, 2, 3, 8, 6, 7])),
            (lambda previous_menu:indices_actions(Guest(), [1, 9, 6, 7])),
            (lambda previous_menu:indices_actions(
                Admin(), [0, 1, 2, 3, 8, 4, 6, 7])),
            Individu().quitter],

        "individu": Individu(),
        "path": []
    },
    {
        "question": "Que voulez vous faire ? ",
        "options": [
            "Connexion",  # 0
            "Jouer/Reprendre une partie",  # 1
            "Créer un compte",  # 2
            "Voir ses statistiques",  # 3
            "Gérer la base de donnée",  # 4
            "Ajouter un jeu",  # 5
            "Revenir au menu précédent",  # 6
            "Quitter l'application",  # 7
            "Modifier ses informations ",  # 8
            "Reprendre une partie"],  # 9
        "actions": [
            connexion,
            menuChoixJeu,
            (lambda previous_menu:previous_menu["individu"].createAccount(
                previous_menu)),
            (lambda previous_menu:previous_menu["individu"].voirStat(
                previous_menu)),
            menuBase,
            menuAjoutJeu,
            (lambda previous_menu:MenuInterface(menu[0])),
            Individu().quitter,
            menuModif,
            menuChoixJeuReprise],
        "individu": Individu(),
        "path": []
    }]


"""Menu principal et menu utilisateur proposant l'ensemble des actions possibles
"""
