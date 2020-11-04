class Card:

    def __init__(self, valeur, couleur, code=None) -> None:
        self.valeur = valeur,
        self.couleur = couleur,
        self.code = code

    def __str__(self) -> str:
        return("{} de {}".format(self.couleur[0], self.valeur[0]))

    def __eq__(self, autrecarte) -> bool:
        if isinstance(autrecarte, Card):
            return(self.valeur == autrecarte.valeur) and (self.couleur == autrecarte.couleur)
        raise TypeError("La comparaison n'est possible qu'entre deux cartes")

    def compareColor(self, autrecarte) -> bool:
        if isinstance(autrecarte, Card):
            return(self.couleur == autrecarte.couleur)
        raise TypeError("La comparaison n'est possible qu'entre deux cartes")
