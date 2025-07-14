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

mp = int('d4f6cce94a3db39c5b77b0bd4549bfefe44bf6d324ce1900fec6978239af62056e12617bb7c75e93674374384d94dd8b52cfe65b49aa17e5b7cf92ae3d6f8b5ea9137e1fa6bffabfac4cd9152a57a96c2e35c0ad4114d0530f6d6c685baf3c8fb8549133c4475f99f26387cf6651e66dbbefb3b768dfd3cc49951ad4d69371ac60984aa9d2f75cc681098a3260c7c63a301b04510b59741dd5b1b164173b1d6197532468b47a1cdcf2924d634ab8e5718efe860c1ffa5d8d778032b8713961768cfdaded03253c34a9aab65dfc888ba34d25fc3ad923316c2937e09a880763f362ab0f3123ab0afa50a9517e78d52ffa03be2f29504c7dd96eef8488d6262bb8',16)
mq = int('a20cf0a0b511aa050369d42fe1dfec3fa883984faa92c25c4fd41abaeac2eb4ea62ef83fed85ac3053b253250ae4aab0633f1f3a2d504bc00da1e1ae828c05dc44c6df63f862f3fef468e80107031e1854a9ceb335dc936e4a1f0dae7e276b8cca47a4b938cf8a27cbfaac29e1867026dd86e7e575eafa66a4e59c62f9b2120bb415a83084c58c0062f32ea6405c599233fdad920cf56db92ea5b9743d072995ae43f1648a1ffa0882f71dbe071450e614bafb9fef67524bb28180be713438ba69e7417d22aee1c811fb155b80ca24a2959a3dffbeb8228001d877a0db7262bd8bf0106a4d514c9c00040eaf2bd9baf5bb21cfdc78ad2e1c6b6b080f9a3d8676',16)
mg = int('19b965b2d5bd971f3685a7a5846cf651e6b8cbdb4338ee8787e4a3b03d8fd2eef1311a8c8bad915866e677658a11d5864980dc046d46f7c9c51168f382e4011fc94df9a83b29a0af4de467cffe099d706752008d68c9f342811e7542ad19b4a04d43a5f44b580556fd7c2d21d5b662ea01e1d4fede981512c6a18c27d931772f681f48f21639fb5a8c8e3224d72b3354fe8a6716a3743ca05d9536a66968796ab989e2eb3c95e18b6adec337f5215369e55a6a042a27db701156f026925dff820f952772f97dfdc182193cbb69b1088f2f929a5c3e6713d6e6725dceab5f561c6d3a3ff97b79b64154ce583dd23d4284d3322f2a8d1c9fc738837de3f4f387d9',16)

cle_p = """-----BEGIN PUBLIC KEY-----
MIIBIDANBgkqhkiG9w0BAQEFAAOCAQ0AMIIBCAKCAQEA2FNQ/v9oQIug5BOH0J/B
bTGek5wNqmF5DWyEAYQcwZE5ktffq2vU3Dg+zu03h3eA3LfNZ+guu1p5X363ojR1
nJnxhNxU+bTGe2pFPKgj07NYHbSN1TDAh4XMWxswHWtXqWdG5iQq4t/5drMxZa7z
+znBUcK10yRmliFoGUtMwLaZABEBE+7MNzSfmzSJrrM6IYjZQ0PtvpBcXXyLCvln
gsq2Djr9450pKKZkmJ4iU58zm9UKxpQV0kzKp1KVMuFealC2tKX8j3Y1N2UiVWDU
RXPv9xRNtxelP0EenINLUjoKZDzE80prMKVQb0NBOUm19B8IdlkbjU1dprpZcQKj
IQIBAw==
-----END PUBLIC KEY-----"""

cle_q = """-----BEGIN PUBLIC KEY-----
MIIBIDANBgkqhkiG9w0BAQEFAAOCAQ0AMIIBCAKCAQEArgNTOy5DruSBjBkCHZFV
UEb1PQRZ5Tjz3ZfFBqt0agbj1qYfLr/v7kKgKEy0zQBBxUQAUUUL7poZnJRKZD3x
3Sm5Hefp/nvBx71+LEpfFdCvdvm0sUm8u4MTivpJN0MjlX/2xy1JiYU19E7aTjHk
DJXFgHfpdvAinCsHrkoVfLx2oMd/eH6LYli4Ov+d0bq9Tj3hDzAm4q0ZF/s7U7D5
517ma4g9Rsx9wIBXfOfKUQ5pmCk22H6BRc33g4OSHgPHlMxbvinnmKz22yAZrHMN
M+XEOzCyZc0LMnSReSUx9ZTgQgdL8bioBmkzwkZ2c1DQKUtFOaXZG/MNaFAy7HGU
9wIBAw==
-----END PUBLIC KEY-----"""

cle_g = """-----BEGIN PUBLIC KEY-----
MIIBIDANBgkqhkiG9w0BAQEFAAOCAQ0AMIIBCAKCAQEA57Yuagh2bEgezlU+IIAA
biwB/lkvqLrUwIV6J6IuqLU/zBFSGYefDEZIQ2VJ2E7pOtAuk219hIjXWWxbO3lz
VV315DmXKVHddvJenJgP3ANyf1WWI7DPPabSKs3adu60Cwj/4EDufGw/NMd3yHdb
nAQqrZppm3q6IQ+UJOhIgLIs2c3Ylo86oZDnZBMLQZcyMRCFngE7iu6MGDJ7NuWz
4io0cX2cHSyd9icq8frEW6wvgJkOuK8xjgKIjWcvuQU0g0s7PNte5MBb1YGDuWeU
HS/reZPgIYFN9t8EdScJaCeVTF+IYz4pHVXBBUBhj0MKlGt7cVQRgot4K965u+LQ
IwIBAw==
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

m = 1376731892974245831350784146988377183474200455737254485095011207007252407911059771566012705766572844457139179612930410460001219185066725235028609755550410968737127584812104750887519827641093635933338812970971339158203882710295882074419745839507310872949187673562139721056236586591333131219005372740577903377344161088046391249518843150453667331809886116951377589378389149649957022976140552936437238826901851611449571178942537064163915894238831528991808058520496554974998900910215532818699595103704046034188458429442957901803039236585927723653316965144331103234793869127629671861633522050718974634490967762902868577

# Convertir l'entier en une chaîne d'octets hexadécimaux
# Convertir l'entier en une séquence d'octets (bytes)
byte_representation = m.to_bytes((m.bit_length() + 7) // 8, 'big')

print("Représentation en bytes:", byte_representation)

# Convertir les octets en base64
base64_representation = base64.b64encode(byte_representation)

print("Représentation en base64 de la séquence d'octets:", base64_representation.decode())