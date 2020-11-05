""" Objets Cartes utilisés pendant les jeux de cartes de l'application

"""


class Card:

    def __init__(self, valeur, couleur, code=None) -> None:
        """Initialisation des cartes, attributs en anglais pour correspondre à L'API

        Args:
            valeur (str): Valeur de 2 à AS
            couleur (str): Signes (SPADES, HEARTS, DIAMONDS,CLUBS)
            code ([type], optional): Code correspondant à l'identifiant API
        """
        self.valeur = valeur,
        self.couleur = couleur,
        self.code = code

    def __str__(self) -> str:
        return("{} de {}".format(self.valeur[0], self.couleur[0]))

    def __eq__(self, autrecarte) -> bool:
        if isinstance(autrecarte, Card):
            return(self.valeur == autrecarte.valeur) and (self.couleur == autrecarte.couleur)
        raise TypeError("La comparaison n'est possible qu'entre deux cartes")

    def compareColor(self, autrecarte) -> bool:
        if isinstance(autrecarte, Card):
            return(self.couleur == autrecarte.couleur)
        raise TypeError("La comparaison n'est possible qu'entre deux cartes")

    @staticmethod
    def toCards(text):
        """Transforme une carte sous format text en instance de l'objet Card

        Args:
            text (str): Sous format Valeur de Couleur
        """

        mots = text.split()
        return(Card(mots[0], mots[2]))
