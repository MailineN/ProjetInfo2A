def verif_init_mdp(mdp, vmdp):
    """ Vérifie que le mot de passe est le même que celui de la confirmation """
    if mdp == vmdp:
        return True
    else:
        return False
