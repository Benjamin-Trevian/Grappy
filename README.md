# Grappy

Grappy est une librairie Python basée sur matplotlib, qui simplifie la création de graphiques.

## Installation

Vous pouvez Installer Grappy avec [pip](https://pypi.org/project/GrappyLfjv/)

```bash
pip install GrappyLfjv
```

## Guide d'utilisation

Création graphique à partir de points:

```python
from grappy import graphe

exemple = graphe("Nom graphique", "labelx", "labely").points([(3,4),(6,5),(8,9)]).afficher()
```

Exportation graphique vers fichier csv:

```python
from grappy import graphe

exemple = graphe("Nom graphique", "labelx", "labely").points([(3,4),(6,5),(8,9)]).exporter("nomFichier")
```

Importation depuis csv:

```python
from grappy import graphe

exemple = graphe().importer("nomFichier", "h").afficher()

#h si tableau horizontale, v si verticale
```

Création graphique à partir d'une fonction:

```python
from grappy import graphe

exemple = graphe().fonction("x**2+2", 0, 100).afficher()
```

Merci de vous référer à la documentation pour plus plus d'informations

## Documentation

```python
graphe(titre, labelx, labely)
```

-Paramètres:

titre: string -> titre du graphique

labelx: string -> titre du label sur l'axe x

labely: string -> titre du label sur l'axe y

renvoie: rien

-Description: Créer la base du graphe, titre, titre labelx, titre labely

```python
graphe.points(liste_points)
```

-Paramètres:

liste_points: liste -> liste de points sous forme de tuples pour construire le graphique

renvoie: rien

-Description: ajoute les points dans liste_points dans le graphique

```python
graphe.points().exporter(nom)
```

-Paramètres:

nom: string -> nom du nouveau fichier csv qui sera crée

renvoie: rien

-Description: Créer un fichier csv avec comme contenu la liste de points entrées dans graphe.points()

```python
graphe.points().afficher()
```

-Paramètres:

renvoie: rien

-Description: affiche le graphique à partir des points entrées dans graphe.points()

```python
graphe.importer(nom_fichier, configuration, logiciel)
```

-Paramètres:

nom_fichier: string -> Nom du fichier à importer

configuration: string -> "v" si le tableau importé est verticale, "h" si le tableau importé est horizontale

logiciel: string -> optionel, permet de définir le logiciel ayant exporté le csv (pour le delimiteur)

renvoie: rien

-Decription: importe un graphique depuis un fichier csv

```python
graphe.importer().afficher()
```

-Paramètres:

renvoie: rien

-Description: affiche le graphique construit à partier du fichier importé

```python
graphe.fonction(fonction, xdebut, xfin, pas)
```

-Paramètres:

fonction: string -> fonction à afficher sous écriture python

xdebut: integer -> première valeur du x à afficher

xfin: integer -> dernière valeur du x à afficher

pas: int -> optionel, pas entre chaque x

renvoie: rien

-Description: Créer un graphique à partir d'une fonction

```python
graphe.fonction().afficher()
```

Paramètres:

renvoie: rien

Description: affiche le graphique à partir de la fonction entrée précédemment

## License

[MIT](https://choosealicense.com/licenses/mit/)
