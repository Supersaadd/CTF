import random
from sympy import isprime

a = 0xee7960b85d8b002fb44abdb79be48337d2f06e2e24e25f25a01313a6585163becae9627da975310e93d3b6badbf2bd66ea63d31e24c3a3cebde42fe7e8afb99d84e17b204e7c470ce7359ec29ef93eb77a6b5c7c1eb6f41628c3dc7671f488b1051ed8f582ffa2db13ea147b87e69a6ec1aabed005ef776fcb35b9040b46a66197af8a1fd08ce1bda932c99bb0bdfccf5f58af41c0f18b3bd6e0a33b223609ce51e59df132fc2689a0cd073ab6778456ec45c3d40a4ae65dbaa81be4aa1d7fb638c01af172bca05bb83efc5bb40661e71c33a3063c5b2e74fca308d3b9da6eda61277b47279d8b311b83b550da10dc05a0e559b6590f6a99abf78f6172e2ed58
q = 0xa693cb7881951a874044864c9e4be9f080ca83e3fcbb2a5c3466d43b09e4a75b

#k = (b - a) // (q * 2)  # diviser la longueur de l'intervalle par 2*q
p_found = False

while (p_found==False):
    # choisir un entier aléatoire k entre 1 et 1000
    k = random.randrange(a//q,b//q)
    p_candidate = k * q + 1  # vérifier si p_candidate est premier
    if isprime(p_candidate):
        # vérifier si g est d'ordre q modulo p_candidate
        if(a<=p_candidate<=b):
            p_found=True

# afficher les résultats
print("p = 0x{:x}".format(p_candidate))

print('p = ?',p_candidate)

print('oui = ',pow(134,((p_candidate-1)//q),p_candidate))