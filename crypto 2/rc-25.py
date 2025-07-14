from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
import base64

# Fonction pour extraire e1 et e2 à partir de deux clés publiques RSA
def extract_exponents(public_key1, public_key2):
    e1 = public_key1.public_numbers().e
    e2 = public_key2.public_numbers().e
    n = public_key1.public_numbers().n

    # Vérifier si les deux clés publiques ont le même N
    if public_key1.public_numbers().n != public_key2.public_numbers().n:
        raise ValueError("Les clés publiques n'ont pas le même N")

    return e1, e2, n

import math

# Fonction pour trouver le PGCD (plus grand commun diviseur) avec l'algorithme d'Euclide
def gcd_extended(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, u_prime, v_prime = gcd_extended(b, a % b)
        u = v_prime
        v = u_prime - (a // b) * v_prime
        return gcd, u, v

# Fonction pour trouver l'inverse modulaire
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Fonction pour déchiffrer un message chiffré avec deux clés publiques RSA
def decrypt_with_two_public_keys(text1, text2, e1, e2, n):

    # Trouver les coefficients de Bézout u et v tels que u*e1 + v*e2 = 1
    gcd_val, u, v = gcd_extended(e1, e2)
    if gcd_val == 1:
        print("on est bien")    

    # Calculer le message déchiffré en utilisant la relation de Bézout
    m = pow(text1, u, n) * pow(text2, v, n) % n

    return m


# Clés publiques
cle_publique_1 = """-----BEGIN PUBLIC KEY-----
MIIBPTANBgkqhkiG9w0BAQEFAAOCASoAMIIBJQKCAQEA4g7HfABU/SLmqu0uEW8+
kvfNG+1VCjNMeQoMgPmbOEPZI21/VsZCbtSTLhnYg5XkA8Xp4EteqRmluFUk/tQs
95xPTTlt9sL+mmvrVzD73y/tFIw3UCWs4yZIw9cEKd0QB0vEb1FD2yKaNWVaDaKr
CQ1+KpCYHaj/g+yD1m/CPU+fjvQmRrOWCV7cPlV5U0EhXW7LteZm8nzWbvjSk+UT
gNJ/q+qyvdo7KXGwc0beV2mU0NiwAfvewRoy+T0oPQpjof2wXyES6DKyoT1x1hW2
VLUNwaUN1xj+R2AVcu9X3jYdvfG2z3RadAJhJUQlzNbWFflFouyNFmqntc66xe/l
gQIeRyQfhMYdxkTjzElYi4dWpQAAAAA+++ATRIUM+++B
-----END PUBLIC KEY-----"""

cle_publique_2 = """-----BEGIN PUBLIC KEY-----
MIIBPTANBgkqhkiG9w0BAQEFAAOCASoAMIIBJQKCAQEA4g7HfABU/SLmqu0uEW8+
kvfNG+1VCjNMeQoMgPmbOEPZI21/VsZCbtSTLhnYg5XkA8Xp4EteqRmluFUk/tQs
95xPTTlt9sL+mmvrVzD73y/tFIw3UCWs4yZIw9cEKd0QB0vEb1FD2yKaNWVaDaKr
CQ1+KpCYHaj/g+yD1m/CPU+fjvQmRrOWCV7cPlV5U0EhXW7LteZm8nzWbvjSk+UT
gNJ/q+qyvdo7KXGwc0beV2mU0NiwAfvewRoy+T0oPQpjof2wXyES6DKyoT1x1hW2
VLUNwaUN1xj+R2AVcu9X3jYdvfG2z3RadAJhJUQlzNbWFflFouyNFmqntc66xe/l
gQIeILmCOBaCo3/MXZRbbwVHwwAAAAA+++ATRIUM+++B
-----END PUBLIC KEY-----"""

cle_publique_1 = serialization.load_pem_public_key(cle_publique_1.encode(), backend=default_backend())
cle_publique_2 = serialization.load_pem_public_key(cle_publique_2.encode(), backend=default_backend())

e1,e2,n = extract_exponents(cle_publique_1,cle_publique_2)
print(e1)
print(e2)
print(n)
# Messages chiffrés
# Messages chiffrés en hexadécimal
message_chiffre_1_hex = "7e344e9ea474548854fa00eacf7981e085c4380f8cf10775b589671f5d1172787de87a19b53eac90de6ffd0f2b2ae3730ff5b83815e99752efb6c030d794234d97bcfac928dd7520f6c8f8eb94e7cbc446b98abc8414f0f79facc4935668bac70f32ddc1b61d9bf436c03abfe6539f7a5b2aa37a73d5c7e88a105225517bdd78be1413921e857e84ae80a227b85cd051f6560b7b4569c5de021edc36a055657e802827f44c82843776912d2c04617a5d43c38138a9b5f16f3585b0599576b6dbdab562537c1bdfb9d43cc75971c3021b8db354a72261badab5d103629d4b5537cb6d21045ca1f4f66ae39108c050753b151403d615d1ccb62ff959c135facd10" # exemple
message_chiffre_2_hex = "5cad9363628762f62f3cabaf4786f2f68b5bfa263783a1bfbb19e92cfa9ca442198e4d9bd91d355e6520f38c1953ae961ef0dc47136e09e81efc12e658e31241ea47b3cce8c4a1fea38365a24f6f98e17175ec36c4fce764f3894bc36714bebedf52d8302a9e0de8959ac60ec95ed5a92a0d6f3294410d406c87fa7177a1fc22315229191d2456cd179ecf70714c7baa5ea6234b1ab8e2395c187dc1b7d0aab2baaecb165d72c450a6ac98da8de02518393942250379a08f7efc982fdd279335afefd86eeaf61442bb19681637570ae22f89afd0bb19d02781fcd6e6edc1c7be3d268e27f44df02ff4fa89ab7ecfc7284416245e932e214ddad060a8d621bb31" # exemple



# Convertir les messages chiffrés en bytes
message_chiffre_1 = int(message_chiffre_1_hex,16)
message_chiffre_2 = int(message_chiffre_2_hex,16)

# # Déchiffrer les messages
# message_clair_1 = dechiffrer_message(message_chiffre_1, cle_publique_1)
# message_clair_2 = dechiffrer_message(message_chiffre_2, cle_publique_2)

# print("Message clair 1:", message_clair_1.decode())
# print("Message clair 2:", message_clair_2.decode())

# Déchiffrer le message chiffré
decrypted_message = decrypt_with_two_public_keys(message_chiffre_1, message_chiffre_2, e1, e2, n)
print("Message déchiffré:", decrypted_message)

# Convertir le nombre en octets (bytes)
number_bytes = decrypted_message.to_bytes((decrypted_message.bit_length() + 7) // 8, byteorder='big')

# Encoder les octets en base64
encoded_message_base64 = base64.b64encode(number_bytes)

print(encoded_message_base64.decode('utf-8'))

print(pow(decrypted_message,e1,n)==message_chiffre_1)
print(pow(decrypted_message,e2,n)==message_chiffre_2)

# Conversion en bytes avec une taille spécifiée
byte_array = decrypted_message.to_bytes((decrypted_message.bit_length() + 7) // 8, byteorder='big')

# Décodage des bytes en utilisant l'encodage approprié
# decoded_string = byte_array.decode()  # Ou utilisez l'encodage correct si différent

print(byte_array)

print('7a7b08d497e17adc1095fe4b618132ea')