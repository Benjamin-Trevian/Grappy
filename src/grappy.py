import matplotlib.pyplot as plt

def string_liste(string: str): #convertit string en lite
    resultat = []
    for u in string:
        resultat.append(u)
    return resultat
    
def liste_string(liste: list): #convertit liste en string 
    resultat = ""
    for t in liste:
        resultat += str(t)
    return resultat

class graphe:
    def __init__(self, titre: str, labelx: str, labely: str):
        plt.title(titre)
        plt.ylabel(labely)
        plt.xlabel(labelx)
    
    def afficherPoints(self, liste_points: list):
        x = []
        y = []
        for i in liste_points:
            x.append(i[0])
            y.append(i[1])
        plt.plot(x,y)
        plt.show()        

    def afficherFonction(self, fonction: str, xdebut: float, xfin: float):
        x = []
        y = []
        copieFonction = string_liste(fonction)
        for i in range ((xfin-xdebut) + 1):                                         #pb de priorite, il faut rajouter des parenthese autour du x pour le cas ou x est negatif
            while "x" in copieFonction:                                             # donc je rajoute des parenthese autour de chaque x
                indice = copieFonction.index("x")
                copieFonction[indice] = xdebut
                copieFonction.insert(indice, "(")
                copieFonction.insert(indice+2, ")")
            x.append(xdebut)
            xdebut+=1
            y.append(eval(liste_string(copieFonction)))
            copieFonction = string_liste(fonction)
        plt.plot(x, y)
        plt.show()


