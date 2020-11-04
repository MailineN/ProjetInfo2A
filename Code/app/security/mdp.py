def verif_init_mdp(mdp, vmdp):
    """ Vérifie que le mot de passe est le même que celui de la confirmation """
if mdp == vmdp :
    return mdp
else :
    mdp = input("Vos deux mots de passe ne correspondent pas. Veuillez entrer à nouveau votre mot de passe ")
    vmdp = input("Veuillez confirmer votre mdp")
    verif_mdp(mdp, vmdp)