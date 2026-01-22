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

def nuage_points_tries_from_values(values):
    if DEBUG:
        print(f"graphique.py -> func nuage_points_tries_from_values -> {len(values)} valeurs reçues")

    # Trier les valeurs par ordre croissant
    valeurs_triees = sorted(values)
    x = list(range(len(valeurs_triees)))
    
    plt.figure(figsize=(10, 5))
    plt.scatter(x, valeurs_triees, s=10, alpha=0.6, label="Points triés")
    
    # Tracer une droite au milieu (régression linéaire)
    if len(x) > 1:
        # Calculer la droite de régression: y = ax + b
        x_mean = sum(x) / len(x)
        y_mean = sum(valeurs_triees) / len(valeurs_triees)
        
        numerator = sum((x[i] - x_mean) * (valeurs_triees[i] - y_mean) for i in range(len(x)))
        denominator = sum((x[i] - x_mean) ** 2 for i in range(len(x)))
        
        a = numerator / denominator
        b = y_mean - a * x_mean
        
        # Points de la droite
        y_regression = [a * xi + b for xi in x]
        plt.plot(x, y_regression, 'r-', linewidth=2, label="Droite de régression")
    
    plt.xlabel("Index trié")
    plt.ylabel("Valeur (0 à 36)")
    plt.title(f"Nuage de points triés – {len(values)} nombres générés via entropie réelle")
    plt.legend()
    plt.grid(True)

    plt.savefig(OUTPUT["nuage_points_graph_trie"], dpi=300, bbox_inches="tight")
    plt.close()