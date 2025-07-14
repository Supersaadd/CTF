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
MIIBQDANBgkqhkiG9w0BAQEFAAOCAS0AMIIBKAKCAQEAvdjcKfwvVSl5gJjotm9M
tmA31YixDRfOjbA11LyF0so8VkU2s50zztag26/Ad7HSaqhZZHBWnvBzso9iLNdO
wfWNeX8opcaiYjaXpOGMHTjHcw06V15lra8mOR69mAl3moKwRoko5WBj6yREmFR3
cgIf1Y+S7Sk1fQQ905dpvaZc6AF/SZzj8CFlxWXEXSdXUuEr1UsLggGLduWVnbc5
HpEoEjcnp1ngMSKbmIec3ufBdvmBujDom20evLt+lZUzKjvr8shVlsZYJg9+yobE
n9wYQzRVHYcle3RrE702vIoW5bmyAZClwiXA6N/DYejiuTXTbVu9EBwMXy1V+gqh
9QIhAMsFA/gjl3OruG52bfp0xbkAAAAAAAA+++ATRIUM+++B
-----END PUBLIC KEY-----"""

cle_publique_2 = """-----BEGIN PUBLIC KEY-----
MIIBPTANBgkqhkiG9w0BAQEFAAOCASoAMIIBJQKCAQEAvdjcKfwvVSl5gJjotm9M
tmA31YixDRfOjbA11LyF0so8VkU2s50zztag26/Ad7HSaqhZZHBWnvBzso9iLNdO
wfWNeX8opcaiYjaXpOGMHTjHcw06V15lra8mOR69mAl3moKwRoko5WBj6yREmFR3
cgIf1Y+S7Sk1fQQ905dpvaZc6AF/SZzj8CFlxWXEXSdXUuEr1UsLggGLduWVnbc5
HpEoEjcnp1ngMSKbmIec3ufBdvmBujDom20evLt+lZUzKjvr8shVlsZYJg9+yobE
n9wYQzRVHYcle3RrE702vIoW5bmyAZClwiXA6N/DYejiuTXTbVu9EBwMXy1V+gqh
9QIePdIfiYN5yfX0k+5rd9BakQAAAAA+++ATRIUM+++B
-----END PUBLIC KEY-----"""

cle_publique_1 = serialization.load_pem_public_key(cle_publique_1.encode(), backend=default_backend())
cle_publique_2 = serialization.load_pem_public_key(cle_publique_2.encode(), backend=default_backend())

e1,e2,n = extract_exponents(cle_publique_1,cle_publique_2)
print(e1)
print(e2)
print(n)
# Messages chiffrés
# Messages chiffrés en hexadécimal
message_chiffre_1_hex = "bdbc0ec53ea8881c8ea584ca50c1f9f4c3637d4735585e12995417a43fd2ce24dcdba394e1ebf929cb88be8b3e7038a1304e19e6638349085fb44ec1c3ccd69fc2164cc13197a920d83bc99e649dc612e38e5e023985298fef2ac7952a066bd34d98bfb9eafc576e3dffc69f2f5a1234f790425db6b5c345234afa11bc47281264c5a158c425c67208d32dcadf558c5e593b2088da621bc636ac36eab7f179ef0c577d85c6f412e799190341b59cf82ccf44d0cd7d14b8882f17934779557fa140a847c46150e0c76f1921c02669a70a9827cd37ca016361f78f68041f980d1a7cac6396e45db2da0a76c9cb9595a49a19950378316e779a09360d6940f1d42c" # exemple
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