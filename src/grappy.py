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

    class points:
        def __init__(self, liste_points: list):
            self.x = []
            self.y = []
            for i in liste_points:
                self.x.append(i[0])
                self.y.append(i[1])

        def afficher(self):
            plt.plot(self.x, self.y)
            plt.show()

    class fonction:
        def __init__(self, fonction: str, xdebut: float, xfin: float, pas: float = 1): #le pas est optionnel est de base sera egal à 1
            self.x = []
            self.y = []
            copieFonction = string_liste(fonction)
            for i in range ((xfin-xdebut) + 1):                                         #pb de priorite, il faut rajouter des parenthese autour du x pour le cas ou x est negatif
                while "x" in copieFonction:                                             # donc je rajoute des parenthese autour de chaque x
                    indice = copieFonction.index("x")
                    copieFonction[indice] = xdebut
                    copieFonction.insert(indice, "(")
                    copieFonction.insert(indice+2, ")")
                self.x.append(xdebut)
                xdebut = xdebut + pas
                self.y.append(eval(liste_string(copieFonction)))
                copieFonction = string_liste(fonction)
        
        def afficher(self):
            plt.plot(self.x, self.y)
            plt.show()




a = graphe("test", "test", "test").fonction("4*x**2+2", -30, 30, 1)
a.afficher()
print(a.maximum())


    
    # def afficherPoints(self, liste_points: list):
    #     x = []
    #     y = []
    #     for i in liste_points:
    #         x.append(i[0])
    #         y.append(i[1])
    #     plt.plot(x,y)
    #     plt.show()        

    # def afficherFonction(self, fonction: str, xdebut: float, xfin: float):
    #     x = []
    #     y = []
    #     copieFonction = string_liste(fonction)
    #     for i in range ((xfin-xdebut) + 1): 
    #         while "x" in copieFonction:                                             
    #             indice = copieFonction.index("x")
    #             copieFonction[indice] = xdebut
    #             copieFonction.insert(indice, "(")
    #             copieFonction.insert(indice+2, ")")
    #         x.append(xdebut)
    #         xdebut+=1
    #         y.append(eval(liste_string(copieFonction)))
    #         copieFonction = string_liste(fonction)
    #     plt.plot(x, y)
    #     plt.show()


