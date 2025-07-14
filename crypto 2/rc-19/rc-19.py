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


IV_string = "3e29c114c2074b58c45f151478f305b5"
IV = bytes.fromhex(IV_string)

for a in range(256):
    for b in range(256):
        seed = bytes([a,b])
        key_material = key_expansion(seed)
        K = key_material[0:16]
        IV2 = key_material[16:32]
        #print(type(IV2),"\n")

        if IV == IV2:
            K_hex = K.hex()
            print(K_hex)
            print(IV2.hex())
            break
