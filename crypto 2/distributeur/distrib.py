from sympy.ntheory.modular import crt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import base64
from gmpy2 import mpz

def cube_root_reconstruction(mp, mq, mg, np, nq, ng):
    # Calculer les valeurs de N et de N_3
    N = np * nq * ng
    Np = N // np
    Nq = N // nq
    Ng = N // ng
    
    # Appliquer le théorème chinois des restes
    M = crt([np, nq, ng], [mp, mq, mg])[0]
    
    # Prendre la racine cubique de la valeur reconstituée
    m_cube = M % N
    
    return m_cube

def integer_cube_root(n):
    # Initialisation de la racine à n (juste pour initialiser la boucle)
    root = n
    # Tant que la racine au cube est plus grande que n
    while root ** 3 > n:
        # Mettre à jour la racine en utilisant la méthode de Newton
        root = (2 * root + n // (root ** 2)) // 3
    return root

mp = int('843186f5fd336293c42010bcdf4bdf3821486e8ab30c5aa81c10d8acfbb34f4027be679f769e8c90ab9b0f9cfd8f2a765c8f70c66b3da58fe836cfada10d1760ac07dbda18a2480b52a2ca29682876e8b20e9495ab908c0be1be5297b74e51a69f73765eddfa232a4af85aeb252351751467603f54934eae018fee9297a9aa0502c7621f3f0813484c93676cedb63e3e58057380ae8367a54e073e095804d6494b327d861be2126433722723841a18b24e89f559e3a94357a19c83603dcfc4e011c971614779d88e1a12e456931fe9843aaadd84254b819a5e5e24448350c2a4d422cb214d8ee9fb60c4d28b4ebb289ca935dc8b5d9fd51ae4257ff74e9815df',16)
mq = int('d6e2953f8e1338ddb0a29ad3334c2facad7e5c0b40e972b7a5ce744fa203fb93a8338e240da422388b9b30c31689a90f6db4948c2a042e1b574e61aba70df4379f9bfc795ba030357f552d98e5dff705e7b22233972a6ab1284f533c63895939f44da338322e63f88b11a8ead362722ebeab83524f9f799d378a7ef415895eb5157e36816f638c506381b40d7f8cefa09d5c638688514d4c5fb701635740f2b103f79101ad71237810162e641e0b2900d53da01b0e90a16123117a32acdf383ded3901e4b4d4ccf03a3021b94e530ef10299a97cbfa62a2924bc46be111c3e61f00645013ba4eeca9371756dead1f9a3519ed10f0e6340da9bc18d2b257295fb',16)
mg = int('919af6e2fb48d3dc45b165790e787a23a777e662112ff7195fd28525cbe7d00f8209df20b13bda6f37b28fd2dfa0a296e9ee6de4efc83cc2e62deec8ec3935bb652be742a74cb676905956c83564ba550238d2f15d27cbe4e049f14a5e6bd2d79c3c30e5fcd1b3f8aed4f21b622e19e4f3e7fc482d395fe605147c58f5417a77abb04e165408f7d965bc1bb37348734f6e592d52d4807d79d08137b31a983eb6aed6e302095927b66bb785dca8c7221b14a4d9ed1babbff67d21b7a0e0a6acd85484f6fc6a3a6184fd311bee14a390a76106b16d4c82a23a4305f297c13e335961e8687c48fac1880e736c065c91bc116a45019db6fd3bdb4d2962acfcffe761',16)

cle_p = """-----BEGIN PUBLIC KEY-----
MIIBIDANBgkqhkiG9w0BAQEFAAOCAQ0AMIIBCAKCAQEArYV0+ukBxa/YWexDAtdq
MaG6AWhEY92ktxum6BldFp/H2+DvtDYfgi42obsf52LQACO9/KObtF/TICC2eMYg
4VMxcRSRLsNgWhDlzV7c9gihfRP1PBZnFUL8WCExlaYIKOv2bhIrYpHKjFR95k4G
sGVKvrGe1qy+RLTVpJUhKJzIdWHHcKn6j2qPUfpcMfQsVvvOjygDd5L9Yz+6lr3L
oLusQ2IOCQtGxiSQ4jKfRrCcOQsz0DRcjEF1sRISb8XRArb8YMc3rBoZ+mVDJwuK
nuBYoRNb6gA/79Hx6m+s/CjL6B6KfLIGb38IHmEip6BZAur3esGOmdldDnLyvUAw
6wIBAw==
-----END PUBLIC KEY-----"""

cle_q = """-----BEGIN PUBLIC KEY-----
MIIBIDANBgkqhkiG9w0BAQEFAAOCAQ0AMIIBCAKCAQEA8eKZDZavUdfDxjqLJ2rV
yh+zgaf+RYNSy9LVtHXLP1LzfxxoIC1P8lFPnwQLCIgDaqWSts+FZ/QcSL3uAoLY
IRu86XDJjLg2XbJoaVObZRLX1kbjjKYXGPxC99IxP9f9X0IOeH4cDcqwEtna4ufQ
81pRgb9OaZFHCw1RXiK9JvymCMOymmISVS1qK+h9mJQpHnaZcuGZPaV9OGcKgaDk
SIFDK7wQsJUoHFdMaXj2ZcZirl2ZxsnZkjjsJPWNJRl+JiVChR24evvNvCIKZ4UU
muZv/nN2yM23l9U4BNW3FR+R6/CjCNTUr5L+pAb1l2T/rSNC6NMSrGSUYWGDhFM+
TQIBAw==
-----END PUBLIC KEY-----"""

cle_g = """-----BEGIN PUBLIC KEY-----
MIIBIDANBgkqhkiG9w0BAQEFAAOCAQ0AMIIBCAKCAQEAuTR2Zo4BpHcR3PGmVK7W
qXHtyq9jDS70JLU4O+W7kYfu6PElHSFkNaSVJcC/beORIH6YlybM+8NhJc0W4xUs
AWCQWQIp02dwWI6VmBn1CtQOd05ISU6luV5vM/J8bdW2SiTsjx12ykdfPeSI8bFp
FJUy4dPFHWq4kPx+ggTm+4dNzxRONg7oXnkzpn0NLUk48Q99oWfGwwnrrrXloR9l
2BWZsj83cXTjjUazky+ohHhfV48vjtursQuXasD6dPwsWzBbkI3NkoNecF6tGSoz
Qtq3Tj0yTJBIvvn3Tq0XVQYq5Zl1RJrm/oga2fJG0cNM1kMYspLi1W7Az3fQ8Pvj
gQIBAw==
-----END PUBLIC KEY-----"""

cle_p = serialization.load_pem_public_key(cle_p.encode(), backend=default_backend())
cle_q = serialization.load_pem_public_key(cle_q.encode(), backend=default_backend())
cle_g = serialization.load_pem_public_key(cle_g.encode(), backend=default_backend())

np = cle_p.public_numbers().n
nq = cle_q.public_numbers().n
ng = cle_g.public_numbers().n

m = integer_cube_root(cube_root_reconstruction(mp,mq,mg,np,nq,ng))

print(hex(m)[2:])

print(m)

m = 1214642772668550160063992247101035870676692021719489047471783769075236190713184058703920283686761781704776964642601768547774674133950990519711537888134720235653670884134470757532625214232820473885260125359458407521928434798749186500086409311662794485541660252112496011463152464791247050672791540849534146810794430440121222201289964438154200234075139495707907084404023704147918800494954148903540847371136798273586614313102206098114112126187905786787919972980633528702205302039025543847035853100976947814902472898033952592391901149498088722215569157042258450186688349183063394012035283238492691409902320462229431858

# Convertir l'entier en une chaîne d'octets hexadécimaux
# Convertir l'entier en une séquence d'octets (bytes)
byte_representation = m.to_bytes((m.bit_length() + 7) // 8, 'big')

print("Représentation en bytes:", byte_representation)

# Convertir les octets en base64
base64_representation = base64.b64encode(byte_representation)

print("Représentation en base64 de la séquence d'octets:", base64_representation.decode())










