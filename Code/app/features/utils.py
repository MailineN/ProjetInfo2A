import os

# Fonction permettant de vider la console


def clear():
    return os.system('cls')


def rotate(l, n = 1):
    return l[n:] + l[:n]


def getKey(dico):
    l = []
    for key, value in dico.items():
        l.append(key)
    return l
