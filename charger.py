"""Lecture des données Netflix (extrait : films 1 à 4499).

Usage :
    python charger.py            # affiche quelques statistiques
    python charger.py 0001_1000  # ne lit qu'un fichier (plus rapide)
"""
import glob
import gzip
import sys
from collections import Counter


def lire_films(chemin="movie_titles.csv"):
    """Retourne un dictionnaire {id_film: (année, titre)}.

    Les titres peuvent contenir des virgules : on ne coupe qu'aux deux
    premières.
    """
    films = {}
    with open(chemin, encoding="latin-1") as f:
        for ligne in f:
            id_film, annee, titre = ligne.rstrip("\n").split(",", 2)
            films[int(id_film)] = (annee, titre)
    return films


def lire_evaluations(motif="data/ratings_*.txt.gz"):
    """Produit des tuples (id_film, id_client, note, date), un par évaluation.

    Dans les fichiers, une ligne « 123: » annonce le film 123 ; les lignes
    suivantes, « id_client,note,AAAA-MM-JJ », sont ses évaluations.
    """
    for chemin in sorted(glob.glob(motif)):
        with gzip.open(chemin, "rt", encoding="ascii") as f:
            id_film = None
            for ligne in f:
                ligne = ligne.rstrip("\n")
                if ligne.endswith(":"):
                    id_film = int(ligne[:-1])
                else:
                    client, note, date = ligne.split(",")
                    yield id_film, int(client), int(note), date


if __name__ == "__main__":
    motif = "data/ratings_*.txt.gz"
    if len(sys.argv) > 1:
        motif = f"data/ratings_{sys.argv[1]}.txt.gz"
    films = lire_films()
    notes = Counter()
    par_film = Counter()
    clients = set()
    for id_film, client, note, _ in lire_evaluations(motif):
        notes[note] += 1
        par_film[id_film] += 1
        clients.add(client)
    total = sum(notes.values())
    print(f"{total} évaluations, {len(par_film)} films, {len(clients)} clients")
    print("Répartition des notes :", dict(sorted(notes.items())))
    print(f"Note moyenne : {sum(n * c for n, c in notes.items()) / total:.3f}")
    print("Films les plus évalués :")
    for id_film, n in par_film.most_common(5):
        annee, titre = films[id_film]
        print(f"  {n:7d}  {titre} ({annee})")
