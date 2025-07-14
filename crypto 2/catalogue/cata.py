# import hashlib
from hashlib import sha256
import base64
import json


def sign(key, m):
        """
        Sign a message using this private key
        """
        sig = b''
        h = int.from_bytes(sha256(m.encode('utf-8')).digest(), byteorder='big')
        for i in range(256):
            b = (h >> i) & 1
            sig += key[2 * i + b]
        return sig.hex()
def pk(self):
        """
        Return the public key associated to this private key
        """
        pk = b''
        for i in range(512):
            pk += sha256(self[i]).digest()
        return pk


# Liste pour stocker les messages
messages = []
signatures = []

# Lecture du fichier et stockage des messages dans la liste
# with open('messages.txt', 'r') as file:
#     for line in file:
#         # Supprimer les caractères de nouvelle ligne (\n) à la fin de chaque ligne et ajouter le message à la liste
#         messages.append(line.strip())

# with open('sigtest.txt', 'r') as file:
#     for line in file:
#         # Supprimer les caractères de nouvelle ligne (\n) à la fin de chaque ligne et ajouter le message à la liste
#         signatures.append(line.strip())

with open('json.json', 'r') as file:
     for line in file:
        data = json.loads(line)
        messages.append(data["message"])
        signatures.append(data["signature"])

# Utilisation de zip pour combiner les messages et les signatures en paires de tuples
resultat = zip(messages, signatures)

key = {}

# Affichage des paires de messages et de signatures
for message, signature in resultat:
    signature_b = bytes.fromhex(signature)
    # Obtenir le hachage SHA-256 de la chaîne sous forme de bytes
    hash_b = sha256(message.encode('utf-8')).digest()
    hash_int = int.from_bytes(hash_b, byteorder='big')
    

    for i in range(256):  # Pour chaque bit dans le hachage
        bit = (hash_int >> i) & 1
        # Calcul de l'indice pour ce bit dans la clé privée
        index = 2 * i + bit

        # Extrait la composante de la signature correspondante à l'indice actuel
        component = signature_b[i * 32:(i + 1) * 32] 
        # print(component)
        # print(component.hex())
        
        # Stocke le composant révélé dans le dictionnaire
        key[index] = component






# for i in range(512):
    # print(key[i].hex())
        
# Convertir l'entier en une chaîne d'octets
# byte_string = pk(key).to_bytes((pk(key).bit_length() + 7) // 8, 'big')

# Convertir la chaîne d'octets en base64
base64_encoded = base64.b64encode(pk(key))
        
print(base64_encoded)
print(len(key))
# print(signatures[0])
s = sign(key,messages[0])

assert s == signatures[0]
# print(messages[0])
# # print(s)
# # print(signatures[0])
print('\n\n\n\n')
print(sign(key,'unban nobly chaws suite oiler'))



