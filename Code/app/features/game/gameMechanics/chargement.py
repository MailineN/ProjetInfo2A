from app.features.DAO.gameDAO import gameDAO
from app.menu.menu_interface import MenuInterface
from app.menu.menu_data import menu
from threading import _Timer


class CustomThread(_Timer):
    def __init__(self, interval, function, args=[], kwargs={}):
        self._original_function = function
        super(CustomThread, self).__init__(
            interval, self._do_execute, args, kwargs)

    def _do_execute(self, *a, **kw):
        self.result = self._original_function(*a, **kw)

    def results(self):
        super(CustomThread, self).join()
        return self.result


def chargement(idGame, nameGame):
    print("*******************************************************\n")
    print("La partie commencera lorsqu'il y aura assez de joueurs\n")
    print("*******************************************************\n \n ")
    c = CustomThread(60.0, gameDAO.fetchNumberPlayer(idGame)).start()
    result = c.results(),
    if not result[0]:
        # Pour l'instant reviens au menu principal à tester après
        print('La partie que vous souhaitez rejoindre a déjà commencé\n')
        input('Appuyez sur Entrer pour revenir au menu principal')
        sortie = MenuInterface(menu[0])
    else:
        if nameGame == "Belote":
            while result[1] < 4:
                print(
                    "*******************************************************\n")
                print(
                    "Il manque des joueurs, prochaine vérification dans une minute\n")
                print('Il y a actuellement '+result[1]+'joueurs \n')
                print(
                    "*******************************************************\n \n")
            c.cancel()
            sortie = True
    return sortie

