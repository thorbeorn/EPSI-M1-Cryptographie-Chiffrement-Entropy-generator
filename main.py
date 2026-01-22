from utils.file_and_folder import init_File_And_Folder, remove_Temp_File
from config import TEMP_OUTPUT, OUTPUT, REMOVETEMPFILE
from entropy import generate_single_number
from graphique import nuage_points_from_values
from roulette import create_roulette

NOMBRE_GENERATIONS = 1

init_File_And_Folder(TEMP_OUTPUT, OUTPUT)

print(f"Génération de {NOMBRE_GENERATIONS} nombres via entropie...")
print(f"{'='*60}")

generated_numbers = []
generated_hex = []

for i in range(NOMBRE_GENERATIONS):
    number, key_hex = generate_single_number()
    generated_numbers.append(number)
    generated_hex.append(key_hex)
    
    if (i + 1) % 100 == 0:
        print(f"Progression: {i + 1}/{NOMBRE_GENERATIONS} nombres générés")

print(f"\n{'='*60}")
print(f"{NOMBRE_GENERATIONS} NOMBRES GÉNÉRÉS")
print(f"{'='*60}")
print(f"Premiers 10 nombres: {generated_numbers[:10]}")
print(f"Derniers 10 nombres: {generated_numbers[-10:]}")
print(f"Min: {min(generated_numbers)}, Max: {max(generated_numbers)}")
print(f"{'='*60}")

create_roulette(key_hex[0])

print(f"\nGénération du nuage de points...")
nuage_points_from_values(generated_numbers)
print(f"\n{'='*60}")
print(f"NUAGE DE {NOMBRE_GENERATIONS} POINTS GÉNÉRÉE")
print(f"{'='*60}")
print(f"Nuage de points sauvegardé dans: {OUTPUT['nuage_points_graph']}\n")

if REMOVETEMPFILE:
    remove_Temp_File(TEMP_OUTPUT)