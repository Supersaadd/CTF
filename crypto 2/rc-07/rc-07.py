from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import hashlib
from hashlib import sha256
import os
import math
from math import gcd
import random
from decimal import Decimal

cle_publique_1 = """-----BEGIN PUBLIC KEY-----
MIIBPTANBgkqhkiG9w0BAQEFAAOCASoAMIIBJQKCAQEAwA5CG8MryvLTC9uzPsG4
scvMbjuN7Pg61wLi17tQI5+t7ow4aSQ6kQnEH6Is7yB/ndzw2UzxX0Y5cjb6uzvj
jpPqIQbPnuswGiCyluchxGFIaboTt/Bs1bjJ1xCF22fjFK8kYbvy7wHExQP8q77R
IXSOn3OIIsPBJl0hilh+OCCWVz2iHPWKr2qbX3BCvcLP9jEbzPzhGoygZFI4UniE
LWViJ61ENrqXx6zT3+6Mr9Jc4OTupoSH/oFv8kgIRdEeBKMjHGAPUu5VblFVFMst
rkbGgnajOZFVU60sW751PNZLS5OBB48Mus+g8EPUHU7hhsB1JNYHSMWnKlC/ePwM
DQIeNgitlJj9U9aHkWUJ+dXu9QAAAAA+++ATRIUM+++B
-----END PUBLIC KEY-----"""



cle_publique_2 = """-----BEGIN PUBLIC KEY-----
MIIBQDANBgkqhkiG9w0BAQEFAAOCAS0AMIIBKAKCAQEAwA5CG8MryvLTC9uzPsG4
scvMbjuN7Pg61wLi17tQI5+t7ow4aSQ6kQnEH6Is7yB/ndzw2UzxX0Y5cjb6uzvj
jpPqIQbPnuswGiCyluchxGFIaboTt/Bs1bjJ1xCF22fjFK8kYbvy7wHExQP8q77R
IXSOn3OIIsPBJl0hilh+OCCWVz2iHPWKr2qbX3BCvcLP9jEbzPzhGoygZFI4UniE
LWViJ61ENrqXx6zT3+6Mr9Jc4OTupoSH/oFv8kgIRdEeBKMjHGAPUu5VblFVFMst
rkbGgnajOZFVU60sW751PNZLS5OBB48Mus+g8EPUHU7hhsB1JNYHSMWnKlC/ePwM
DQIhAO2iYQQ9dvomRwI0sHfhOJMAAAAAAAA+++ATRIUM+++B
-----END PUBLIC KEY-----"""

print(cle_publique_1==cle_publique_2)

cle_publique_1 = serialization.load_pem_public_key(cle_publique_1.encode(), backend=default_backend())
cle_publique_2 = serialization.load_pem_public_key(cle_publique_2.encode(), backend=default_backend())

print(cle_publique_1==cle_publique_2)
cle_prive_1 = """-----BEGIN PRIVATE KEY-----
MIICewIBADALBgkqhkiG9w0BAQEEggJnMIICYwIBAAKBgC1Nx0HEi53iDzbt40Vk
4a32fUmsiW/7oVoY4peVqfWIHFJgMedjSA5za/swzhchzNYhtiG+dVGtbgpn4pa1
fh5ypSSwcgsUsaSxFY2jLZOxRpT4lIx/zsO2e5zvPsyYdPOSLzuKk6o7sUW3SwOQ
uKZMmG5TJX4bRb2kpGmVTehlAg0A+++ATRIUM+++ABBBAoGAAeGPKZgPVwae75wZ
PNzUfNeRhgBXB/0gQQ/5VMP4GNKaUh2ze1RAYS1hZOWNkXw+d6i+1dQ9hqKpCjel
F4zBrMTzKr91MQtUNI4StJ+x5xg6Zk9Wq5T0xSKMVQVr4cVr+NEG2l/x4fXs2r84
gEOrUk2te9RK2YrLSCuMfhHtovUCQFltKWgArMjQETihfNt4SScivqGrFSLGsI3B
cB1FG9mGQh4reIRRcL0vjSvhEu1KthfFznYIqnSVhm540MmDhMcCQQCBsNTSY9BW
zg4k/vQe1xurELu1VFBjZjSQVMydiNDtbzdgjepKow1YcxZxgcdcLusW53kirm4w
WuzezKJxM6VzAkA6KLx/Vjh0JqTz2nQw5BnrDvzhYe3fCg9b8OI0HpQbwRRqX5eu
HQ/nLEfGtNBvOcwUC4fb+KoNbfAi7Agi0YClAkACneApv0almDqP++t5niRPK2QI
7dRDJMtURCl3AquW2f4wkwS3d8RxNR3BLiQQD2S1IDxZzgXj8LOBuHvc5J0bAkAy
3yaaKFXkMC7aJRKCJI0VQjiq12C0hcfWg/UgkoyeKTXZIZEtmJPHzUHIG1YoOb2O
EGFibGT0YlobEA/pcXcF
-----END PRIVATE KEY-----"""

cle_prive_1 = serialization.load_pem_private_key(cle_prive_1.encode(), password=None, backend=default_backend())

e1 = cle_publique_1.public_numbers().e
e2 = cle_publique_2.public_numbers().e

n = cle_publique_1.public_numbers().n
d = "8c4c89f9f3389b9ea0190390db0d834b9d84f84fc3ba559a523a28f1fbe01f264b5c904330ad496d8fc3f18d591d7a10d1eac14bc62720f5baf0ac126ed99d5cad96b6a43557bb3ffd56a4f34fb66046370ddb3f0b0eef77d3c2b5e62312c3ea036bf6890d455ce681208acfb9a4e1cc2837683fa1e2dd952383fca74bc36c1e92eedb296432224c03cf1be9f4e2430fba369017cafd530ba8194473987441e9b69674fa1024e824d19ad6f694eaf63e611963910f8a87717a1138bb8d9a8add25aba62edf54a9d83e3b68cab2bfbfc294c0341ccdfd367780387ef0d8f573afbafcbfc49c028c48411f3b13b5a10aef316dc188124b9a8fe774764f3db20a41".encode('utf-8')
# d = cle_prive_1.private_numbers().d
d_base10 = int(d,16)


# print (d_base10)

# # Encodage de la chaîne en utilisant UTF-8 et conversion en base 10
# m_base10 = int.from_bytes(m.encode('utf-8'), byteorder='big')

# print(m_base10)

# print(e1)
# print(n)

# c = pow(m_base10,e1,n)
# print(c)

# m2 = pow(c,d_base10,n)
# print(m2==m_base10)

# on se rend compe que d resout bien la clé publique

c = "lemma patio newel rends metal".encode('utf-8')
print("message en hex :", c.hex())

def facteur(N, e, d):
    s = 2
    ed_1 = e * d - 1
    while ed_1 % 2 == 0:
        s += 1
        print(s)
        ed_1 //= 2
        y = pow(s,ed_1,N)
        if not(y == 1 or y == -1):
            p = gcd(y-1,N)
            
            if (p != 1):
                print(s)
                return p, N//p

    return None

p,g = facteur(n,e1,d_base10)


print(n==p*g)

def euclidean_extended(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x, y = euclidean_extended(b, a % b)
        return (gcd, y, x - (a // b) * y)
    

print("d=",d_base10)

phi_n = (p - 1) * (g - 1)
gcd, x, y = euclidean_extended(e2, phi_n)
if gcd != 1:
    print("probleme")
else:
    d2 = x % phi_n
    print("d2=",d2)


print("p=",p)
print("g=",g)
print("e1=",e1)
print("e2=",e2)
print(d_base10 == d2)




