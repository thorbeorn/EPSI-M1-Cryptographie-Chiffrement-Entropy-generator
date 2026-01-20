import random
import matplotlib.pyplot as plt
from config import OUTPUT, DEBUG

def nuage_points(hex_key):
    if DEBUG:
        print("graphique.py -> func nuage_points.py -> clé hexa entrer : ", hex_key)
    seed = int(hex_key, 16)
    if DEBUG:
        print("graphique.py -> func nuage_points.py -> seed generer : ", seed)
    random.seed(seed)

    values = [random.randint(0, 36) for _ in range(1000)]
    x = list(range(1000))
    plt.figure(figsize=(10, 5))
    plt.scatter(x, values, s=10)
    plt.xlabel("Index")
    plt.ylabel("Valeur (0 à 36)")
    plt.title("Nuage de points – 1000 nombres pseudo-aléatoires (clé 256 bits)")
    plt.grid(True)

    plt.savefig(OUTPUT["nuage_points_graph"], dpi=300, bbox_inches="tight")

    plt.close()
