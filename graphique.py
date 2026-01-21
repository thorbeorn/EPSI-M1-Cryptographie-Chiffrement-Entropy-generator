import random
import matplotlib.pyplot as plt
from config import OUTPUT, DEBUG

def nuage_points_from_values(values):
    if DEBUG:
        print(f"graphique.py -> func nuage_points_from_values -> {len(values)} valeurs reçues")
    
    x = list(range(len(values)))
    plt.figure(figsize=(10, 5))
    plt.scatter(x, values, s=10)
    plt.xlabel("Index")
    plt.ylabel("Valeur (0 à 36)")
    plt.title(f"Nuage de points – {len(values)} nombres générés via entropie réelle")
    plt.grid(True)

    plt.savefig(OUTPUT["nuage_points_graph"], dpi=300, bbox_inches="tight")
    plt.close()