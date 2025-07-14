import sympy
import base64

def generate_p_q_d(e):
    while True:
        # Générer deux nombres premiers p et q
        p = sympy.randprime(2**510, 2**512)
        q = sympy.randprime(2**510, 2**512)

        # Calculer n
        n = p * q

        if(n<=e):print("error")
        else: print("OK")

        # Calculer l'inverse modulaire de e modulo (p-1)(q-1)
        phi_n = (p - 1) * (q - 1)
        
        # Vérifier si e et phi(n) sont premiers entre eux
        if sympy.gcd(e, phi_n) == 1:
            d = sympy.mod_inverse(e, phi_n)
            return p, q, n, d

# Exposant de chiffrement
e = 3  # Vous pouvez changer cette valeur

# Encodage de la chaîne en base64
chaine_base64 = "+++ATRIUM+++ABBB"

# Décodage de la chaîne base64 en bytes
bytes_resultats = base64.b64decode(chaine_base64)

# bytes_resultats += b'101101'
# bytes_resultats = b'101101' + bytes_resultats
# bytes_resultats = b'101101' + bytes_resultats

# Conversion des bytes en base 10
nombre_base_10 = int.from_bytes(bytes_resultats, byteorder='big')

print(nombre_base_10)
# nombre_base_10 += 101
print(base64.b64encode(bytes_resultats))
print(base64.b64encode(nombre_base_10.to_bytes((nombre_base_10.bit_length() + 7) // 8, byteorder='big')))
e = nombre_base_10 

# Générer p, q, n, et d pour l'exposant de chiffrement donné
p, q, n, d = generate_p_q_d(e)

print("p =", p)
print("q =", q)
print("n =", n)
print("e =", e)
print("d =", d)


from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

def generate_rsa_public_key(n, e):
    # Créer un objet de clé publique RSA
    rsa_public_key = rsa.RSAPublicNumbers(e, n)

    # Sérialiser la clé publique au format PEM
    pem_public_key = rsa_public_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return pem_public_key.decode('utf-8')

public_key = generate_rsa_public_key(n, e)
print("Clé publique RSA:")
print(public_key)