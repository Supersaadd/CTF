import random
from sympy import isprime, mod_inverse

def find_generator(p, q):
    # Recherche d'un générateur d'ordre q modulo p
    for g in range(2, p):
        if pow(g, q, p) == 1:
            continue
        for j in range(1, q):
            if pow(g, j*(p-1)//q, p) == 1:
                break
        else:
            return g
    raise Exception("Aucun générateur n'a été trouvé")

def find_prime_generator(a, b, q):
    # Recherche d'un nombre premier p dans l'intervalle [a, b]
    while True:
        p = random.randint(a, b)
        if isprime(p) and (p-1) % q == 0:
            break
    
    # Recherche d'un générateur d'ordre q modulo p
    g = find_generator(p, q)
    
    return p, g

# Paramètres
a = int('e18df1090dd30c3466e4c1edd4a059e45236de0ad373e0267aaeb9552374efb41dfb4ffdcaad18222ba800316204faad4b375fffe1b2b18fe2b0cb3dc43824512bc3a5a7588b57aa500df082801eb0a438abb823b9ec75a5b3343c55d3cf754fe306deaf86e2c440151d674ba793f1b372bbe32a47fb0252b33d4c8c973e4b8a450bfadbb80ee40e5636e0645740f48f4e37f4684546402de4a4a051c226f553bd2057e6cdaf28697ff2f2c2253b361331437a21aebfdfb810e5954ada921a63c4c3a072fca8d8cf881fd43948391fae7d9ab940e583251a2e62b52422813ba9ed0dd4668e8317d57b7088c66df3be39504b630656ef33e50e4d1dc6fd032d7b', 16)
b = a + 2**1950
q = int('ff58a2ac8659a684492c54cf57366470308b427b4bc183d689e0f98edde7257b', 16)

# Recherche d'un couple (p, g) satisfaisant les conditions
p, g = find_prime_generator(a, b, q)
print("p = 0x%x" % p)
print("g = 0x%x" % g)