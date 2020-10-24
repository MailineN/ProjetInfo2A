from enum import Enum, unique

@unique
class Color(Enum):
    CLUBS, DIAMONDS, HEARTS, SPADES = range(4)


@unique
class Rank(Enum):
    ACE, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING = range(8)
  
  
class Card:

    def __init__(self, valeur: Rank, couleur : Color , code=None) -> None:
        self.valeur = valeur,
        self.couleur = couleur,
        self.code = code

    def __str__(self) -> str:
        data = (self.valeur, self.couleur)
        return("{} de {}".format(*data))

    def __eq__(self, autrecarte) -> bool:
        if isinstance(autrecarte, Card):
            return(self.valeur == autrecarte.valeur) and (self.couleur == autrecarte.couleur)
        raise TypeError("La comparaison n'est possible qu'entre deux cartes")

    def compareRank(self, autrecarte) -> bool:
        if isinstance(autrecarte, Card):
            return(self.valeur < autrecarte.valeur)
        raise TypeError("La comparaison n'est possible qu'entre deux cartes")

    def compareColor(self, autrecarte) -> bool:
        if isinstance(autrecarte, Card):
            return(self.couleur == autrecarte.couleur)
        raise TypeError("La comparaison n'est possible qu'entre deux cartes")