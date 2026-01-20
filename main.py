from utils.file_and_folder import init_File_And_Folder, remove_Temp_File

from config import TEMP_OUTPUT, OUTPUT, REMOVETEMPFILE
from entropy import entropy_generation
from graphique import nuage_points
from roulette import create_roulette

init_File_And_Folder(TEMP_OUTPUT, OUTPUT)

print(f"Génération de l'entropie pour la clé 256 bits...")
key_bytes, key_hex, Number_People, Number_Meteo = entropy_generation()
print(f"\n{'='*60}")
print(f"CLÉ 256 BITS GÉNÉRÉE")
print(f"{'='*60}")
print(f"Format hexadécimal: {key_hex}")
print(f"Format bytes: {key_bytes}")
print(f"Longueur: {len(key_bytes)} bytes ({len(key_bytes)*8} bits)")
print(f"Sauvegardée dans: {OUTPUT['Key_File']}")
print(f"{'='*60}")

create_roulette(key_hex)

print(f"Génération du nuage de points...")
nuage_points(key_hex)
print(f"\n{'='*60}")
print(f"NUAGE DE 1000 POINT GÉNÉRÉE")
print(f"{'='*60}")
print(f"Nuage de points sauvegardé dans: {OUTPUT['nuage_points_graph']}\n")

if REMOVETEMPFILE :
    remove_Temp_File(TEMP_OUTPUT)
