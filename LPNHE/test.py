from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
import base64

# La chaîne chiffrée (Base64)
ciphertext_b64 = "U2FsdGVkX1/VqXBdVAkskTqQ2mj4b1tYJSQ8SDxD+6Y21jE5vFnbYRiZe+tVBEui"

# Décodage de la chaîne Base64
ciphertext = base64.b64decode(ciphertext_b64)

# Si vous avez un mot de passe, vous pouvez l'utiliser pour dériver une clé
password = b"winos bries golfs pawky savor"

# Utiliser Scrypt pour dériver une clé de chiffrement (selon la méthode standard de chiffrement)
key = scrypt(password, b"salt", 32, N=2**14, r=8, p=1)

# Initialiser le déchiffreur AES
cipher = AES.new(key, AES.MODE_CBC, iv=ciphertext[:16])

# Déchiffrement
plaintext = cipher.decrypt(ciphertext[16:])

# Afficher en hexadécimal
print(plaintext.hex())
# Convertir la chaîne hexadécimale en texte
plaintext_from_hex = bytes.fromhex('e363d100ce57ba4d8e446f780b51340573dac648150f5076aa831c9bef60fb18')
try:
    print(plaintext_from_hex.decode('utf-8'))
except UnicodeDecodeError:
    print("Impossible de décoder en UTF-8.")
