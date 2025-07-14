import json
import base64
import subprocess

def encrypt_with_session_key(message, recipient_public_key_path):
    # Charger la clé publique du destinataire
    with open(recipient_public_key_path, 'r') as file:
        recipient_public_key = file.read()

    # Générer une clé de session aléatoire pour le chiffrement symétrique
    session_key = subprocess.check_output("openssl rand -hex 16", shell=True).decode().strip()

    print(bytes.fromhex(session_key))

    # Chiffrer le message avec la clé de session
    openssl_command = f'echo -n "{message}" | openssl enc -e -aes-128-cbc -pass pass:{session_key} -pbkdf2 '
    ciphertext = subprocess.check_output(openssl_command, shell=True)

    # Chiffrer la clé de session avec la clé publique du destinataire
    openssl_command = f'echo -n "{session_key}" | openssl pkeyutl -encrypt -pubin -inkey {recipient_public_key_path}'
    encrypted_session_key = subprocess.check_output(openssl_command, shell=True).strip()

    print(encrypted_session_key)

    # Encoder la clé de session chiffrée en hexadécimal
    hex_encrypted_session_key = encrypted_session_key.hex()

    # Encoder le message chiffré en base64
    base64_ciphertext = base64.b64encode(ciphertext).decode()+'\n'

    # Créer un dictionnaire contenant la clé de session chiffrée et le message chiffré
    encrypted_data = {
        "session-key": hex_encrypted_session_key,
        "ciphertext": base64_ciphertext
    }

    # Retourner les données chiffrées sous forme de JSON
    return json.dumps(encrypted_data)

# Exemple d'utilisation{"session-key": "4571209b55f685175160f148132c5231d59d5330942a38a869edd2c3d8cf65457f16c7373094b9c549855b3a3debda40ed2c2b136d2021bb61d6a9b811f2f269449366fc25862aa832c34b25400f4a3eba5fc3a2961387ab5eba815808888b8723e14ce2d35bfa33f902b52506bf8de958a1149efa1eb9c02cb820e36c49b994915081c3e28a77ea4598dd49ac13465ebdff9de81e333e542d2e4a4671ad0cad712d22ebff732aa9eea3ae48138154736eabd57f6ee0e8fb7dff49c7caf9f9b71afe6e86865a4f527487daef603135bd09aea4878d22c0f38c95937e27fd3187a20930d312af493f1aad81621e08675299bcbbae7a7c0167c8ba521936", "ciphertext": "U2FsdGVkX18QjhF7Get2mFNcHBmKFnBVR00xD+IgxtOyFO8vyxZ0gE03A454LzKrw+WHG4E7NyUGStHKySX/bA=="}
recipient_public_key_path = "cle.txt"
message = "Bonjour voici un message pour vous."
encrypted_message = encrypt_with_session_key(message, recipient_public_key_path)

# Envoyer les données chiffrées à la personne
# Exemple : ici vous devrez envoyer le contenu de `encrypted_message` à la personne concernée
print(encrypted_message)
