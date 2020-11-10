from app.features.DAO.gameDAO import GameDAO
from app.features.DAO.pileDAO import PileDAO
from app.menus.menu_interface import MenuInterface
from app.menus.menu_data import menu
from threading import Timer


class CustomThread(Timer):
    def __init__(self, interval, function, args=[], kwargs={}):
        self._original_function = function
        super(CustomThread, self).__init__(
            interval, self._do_execute, args, kwargs)

    def _do_execute(self, *a, **kw):
        self.result = self._original_function(*a, **kw)

    def results(self):
        super(CustomThread, self).join()
        return self.result


def chargementGroupe(idGame, nameGame):
    print("*******************************************************\n")
    print("La partie commencera lorsqu'il y aura assez de joueurs\n")
    print("*******************************************************\n \n ")
    result = gameDAO.fetchNumberPlayer(idGame),
    if not result[0]:
        # Pour l'instant reviens au menu principal à tester après
        print('La partie que vous souhaitez rejoindre a déjà commencé\n')
        input('Appuyez sur Entrer pour revenir au menu principal')
        sortie = MenuInterface(menu[0])
    else:
        if nameGame == "Belote":
            if result[1] == 4:
                sortie = True
            while result[1] < 4:
                c = CustomThread(
                    60.0, gameDAO.fetchNumberPlayer(idGame)).start()
                c.start()
                result = c.join()
                print(
                    "*******************************************************\n")
                print(
                    "Il manque des joueurs, prochaine vérification dans une minute\n")
                print('Il y a actuellement '+str(result[1])+'joueurs \n')
                print(
                    "*******************************************************\n \n")
            sortie = True
            try:
                c.cancel()
    return sortie


def chargementPartie(idPli):
    print("*******************************************************\n")
    print("En attente des autres joueurs\n")
    print("*******************************************************\n \n ")
    plis = PileDAO.getPreviousPiles()
    if len(plis) == 4:
        return True
    while len(plis) < 4:
        c = CustomThread(20.0, gameDAO.fetchNumberPlayer(idGame)).start()
        c.start()
        result = c.join()
        print(
            "*******************************************************\n")
        print(
            "Tous les joueurs n'ont pas encore joué\n")
        print('Pli en cours :  \n')
        for card in plis:
            print("• "+str(card)+"\n")
        print(
            "*******************************************************\n \n")
    sortie = True
    try:
        c.cancel()
    return sortie
