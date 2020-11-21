import os

# Fonction permettant de vider la console


def clear():
    return os.system('cls')


def getKey(dico):
    l = []
    for key, value in dico.items():
        l.append(key)
    return l
