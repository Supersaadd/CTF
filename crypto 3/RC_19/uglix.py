import hashlib

def key_expansion(seed : bytes) -> bytes:
     """
     Renvoie 256 bits pseudo-aléatoires à partir de seed
     """
     state = seed
     output = b''
     for i in range(8):
         state = hashlib.sha256(state).digest()
         output += state[:4]
     return output


IV_string = "19d7ef1fe947402f344c7af3e3405cb5"
IV = bytes.fromhex(IV_string)

for i in range (0,65536):
    seed = i.to_bytes(2, byteorder='big')
    key_material = key_expansion(seed)
    K = key_material[0:16]
    IV2 = key_material[16:32]
    #print(type(IV2),"\n")

    if IV == IV2:
        K_hex = K.hex()
        print(K_hex)


K = "afcad3ab603c2d4b045f144a78678ded"

"""La stratégie consiste à essayer toutes les graînes possibles, calculer la clef,
calculer l'IV, vérifier si l'IV est le bon (le cas échéant la clef est bonne
aussi), puis déchiffrer et profiter."""

"""
IV = 19d7ef1fe947402f344c7af3e3405cb5

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
"""