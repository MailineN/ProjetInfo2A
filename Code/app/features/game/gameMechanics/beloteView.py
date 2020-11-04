from app.menus.menu_interface import MenuInterface


class BeloteView():

    """ A déplacer dans les menus ou autre """
    @staticmethod
    def menuTour(previous_menu, hand):
        menu_act = {}
        menu_act["individu"] = previous_menu["individu"]
        menu_act["question"] = "Quelle carte voulez vous poser ? "
        menu_act["options"] = [str(hand[i])for i in len(hand)]
        menu_act["actions"] = []
        # TODO : Mettre la fonction qui pose la carte et update le game
        menu_act["path"] = []
        return()  # TODO : Retourner la vue du tour en cours

    @staticmethod
    def displayTourAppel(previous_menu, hand, carteAppel):
        rep = ""
        while not (rep == "y" or rep == "Y" or rep == "n" or rep == "N"):
            print("Vous avez ces cartes : \n")
            for card in hand : 
                print(str(card)+"\n")
            rep = input(
                "La couleur proposée est {}, voulez vous prendre ? (Y/N) ".format(carteAppel.couleur))
            if (rep == "y" or rep == "Y"):
                return True
            return False
        
    @staticmethod
    def displayTourAppel2(hand):
        rep = ""
        while not (rep == "y" or rep == "Y" or rep == "n" or rep == "N"):
            print("Vous avez ces cartes : \n")
            for card in hand : 
                print(str(card)+"\n")
            rep = input(
                "Souhaitez vous appeler ? (Y/N) ")
        if (rep.upper() == "Y"):
            player.drawCard(carteAppel)
            color = ""
            while not (color == "S" or color == "H" or color == "C" or color == "D"):
                color = input(
                    "Quelle couleur souhaitez vous appeler ? (S/H/C/D) ")
            if (rep == "S"):
                return(True, "SPADES")
            elif (rep == "H"):
                return(True,"HEARTS")
            elif (rep == "C"):
                return(True,"CLUBS")
            else:
                return(True,"DIAMONDS")
        return (False,None)

    @staticmethod
    def displayNewGame(team1, team2):
        clear()
        display = Figlet(font='big')
        print(display.renderText('Belote :'))
        print(" ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ \n")
        print("Les équipes sont : \n")
        print("{} et {}\n".format(team1[0], team1[1]))
        print("{} et {}\n".format(team2[0], team2[1]))
        print("Les cartes ont étés distribuées, la partie peut commencer !")

    @staticmethod
    def displayRedistrib():
        print("Aucun joueur n'a appelé, le deck va donc être redistribué. \n")
        print(" ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ \n")

    @staticmethod
    def displayAtoutPris(joueur, atout):
        print(joueur+"a pris à " + atout "\n")
        print("Le reste du deck va donc être distribué\n")

    def displayFinTour(joueurGagnant, cartesPlis):
        print(joueurGagnant + " remporte le pli\n")
        print("Les cartes jouées sont : \n")
        print(str(carte) for carte in cartesPlis)

    def displayFinPartie(points):
        print("Le décompte des points est le suivant : \n")
        print("Team 1 :" + points[0] + "\n")
        print("Team 2 :" + points[1] + "\n")
        if points[0] > points[1]:
            print("Team 1 remporte donc la partie ! \n")
        else:
            print("Team 2 remporte donc la partie ! \n")
        print(" ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ \n")
