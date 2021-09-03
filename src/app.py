#!/usr/bin/python3

def mettre_majuscule(string):
    cap_string= string.capitalize()
    return cap_string

### string=input("Veuillez écrire votre phrase en minuscule")
## string="la première lettre de cette phrase n'est plus une minuscule"
## fonction(string)

def capital_case(v):
    return v.capitalize()

def test_mettre_majuscule():  
    resultat= capital_case("adrien")
    assert resultat == 'Adrien'

    #lancer pytest <chemin>, il va lancer le test et reconnaitre la fonction test grâce à la partie du nom de la fonction "test_"