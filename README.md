# Données Netflix (extrait) pour les systèmes de recommandation

Ce dépôt offre un extrait des données du concours Netflix (Netflix Prize, 2006–2009) pour
mettre à l'essai des algorithmes de filtrage collaboratif, comme Slope One.

L'extrait correspond au premier fichier de l'ensemble d'entraînement original
(`combined_data_1.txt`) : les films 1 à 4499, soit 24 053 764 évaluations.
Pour respecter la limite de taille de GitHub, il est découpé en quatre fichiers compressés.

## Contenu

| Fichier | Contenu |
|---|---|
| `data/ratings_0001_1000.txt.gz` | évaluations des films 1 à 1000 |
| `data/ratings_1001_2000.txt.gz` | évaluations des films 1001 à 2000 |
| `data/ratings_2001_3000.txt.gz` | évaluations des films 2001 à 3000 |
| `data/ratings_3001_4499.txt.gz` | évaluations des films 3001 à 4499 |
| `movie_titles.csv` | identifiant, année et titre des 17 770 films du concours |
| `charger.py` | exemple de lecture en Python (bibliothèque standard seulement) |
| `LICENSE` | licence d'utilisation des données Netflix |

## Format des évaluations

Chaque fichier (une fois décompressé) suit le format original du concours. Une ligne
`MovieID:` annonce un film ; les lignes suivantes sont ses évaluations, une par ligne :

```
1:
1488844,3,2005-09-06
822109,5,2005-05-13
...
2:
...
```

- **CustomerID** : identifiant du client, de 1 à 2649429 avec des écarts.
- **Rating** : note entière de 1 à 5 étoiles.
- **Date** : date de l'évaluation, au format AAAA-MM-JJ.

## Format des films

`movie_titles.csv` contient une ligne par film : `MovieID,YearOfRelease,Title`.

- **MovieID** : de 1 à 17770, séquentiel. Il ne correspond pas aux identifiants Netflix ou IMDB.
- **YearOfRelease** : de 1890 à 2005 ; correspond parfois à la sortie en DVD plutôt qu'en salle.
- **Title** : titre anglais. Attention : un titre peut contenir des virgules sans
  guillemets. Ne coupez la ligne qu'aux deux premières virgules.

Le fichier ne contient que des caractères ASCII.

## Utilisation

Il n'est pas nécessaire de décompresser les fichiers : Python les lit directement avec
le module `gzip`.

```bash
git clone https://github.com/lemire/netflix_data.git
cd netflix_data
python3 charger.py 0001_1000   # un seul fichier, quelques secondes
python3 charger.py             # tout l'extrait, plus long
```

Les fonctions `lire_films()` et `lire_evaluations()` de `charger.py` peuvent être importées
dans vos propres programmes :

```python
from charger import lire_films, lire_evaluations

films = lire_films()
for id_film, id_client, note, date in lire_evaluations("data/ratings_0001_1000.txt.gz"):
    ...
```

Pour une première expérience, un seul fichier (environ 5 millions d'évaluations) suffit
largement.
