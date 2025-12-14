import hashlib
import secrets
from datetime import datetime

def generate_256bit_key(number_people, number_meteo, output_Key_Filename):
    salt = secrets.token_bytes(32)
    timestamp = str(datetime.now().timestamp()).encode()
    
    entropy_sources = [
        str(number_people).encode(),
        str(number_meteo).encode(),
        timestamp,
        salt
    ]
    
    combined_entropy = b''.join(entropy_sources)
    key_256bit = hashlib.sha256(combined_entropy).digest()
    key_hex = key_256bit.hex()
    
    with open(output_Key_Filename, "w") as f:
        f.write(f"Clé 256 bits (hex): {key_hex}\n")
        f.write(f"Clé 256 bits (bytes): {key_256bit}\n")
    
    return key_256bit, key_hex