from hashlib import sha256
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import random

HASH_ID = b'010\r\x06\t`\x86H\x01e\x03\x04\x02\x01\x05\x00\x04 '

def emsa_pkcs1_encode(M : bytes, k : int) -> bytes:
    """
    Encode a message into k bytes for RSA signature
    """
    h = sha256(M)
    T = HASH_ID + h.digest()
    if len(T) + 11 > k:
        raise ValueError("Message Too Long")
    PS = bytes([0xff] * (k - len(T) - 3))
    EM = bytes([0x00, 0x01]) + PS + bytes([0x00]) + T
    return EM

def i2osp(x : int, k : int) -> bytes:
    """
    Convert the integer x to a sequence of k bytes
    """
    return x.to_bytes(k, byteorder='big')

def os2ip(x : bytes) -> int:
    """
    Convert the sequence of bytes to an integer
    """
    return int.from_bytes(x, byteorder='big')

def key_length(n : int) -> int:
    """
    key length in bytes
    """
    return (n.bit_length() + 7) // 8

# Fonction pour trouver l'inverse modulaire
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

m = "I, the lab director, hereby grant saad permission to take the BiblioDrone-NG.".encode('utf-8')
m_int = os2ip(m)
k = key_length(m_int)
print(i2osp(m_int,k)==m)

random_number = 3

cle_dir = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvtbNyPFC1hhUtr3cb56z
a7v05dq3cgckAHgpPDhOtT1OOgsvJQ1t0RkkSJc7JQ1WNRchjJChLARH9bMd83QQ
2KLiFXPA8FqKqZJBFHCAU7CIeNO1PM01ujUWwCw2ktBIrUbpi3++E6mbRnD8yW3V
HnoEo9qTSTq1tbD/eud3CNdPjJZBElI/7VnBvclJv+okj/CjkoUwKwKSprjeI/mK
kgE1zxtWYOFutP3bsktDEu9cWfSgKmff8rKKbRsMPjlCwXNvqkOpTwmV4EvabIc6
HLr2aFQkGWq8YYXT5A/BzCdvrnLeBGXZdI5ut+FltigApT8sZ+RpPMkrN6nuS8RJ
6QIDAQAB
-----END PUBLIC KEY-----"""

cle_dir = serialization.load_pem_public_key(cle_dir.encode(), backend=default_backend())
n_dir = cle_dir.public_numbers().n
e_dir = cle_dir.public_numbers().e

pad_m = emsa_pkcs1_encode(m,key_length(n_dir))

# print(pad_m.hex())

pad_m_mask = os2ip(pad_m)*pow(random_number,e_dir,n_dir) % n_dir

# print(pad_m_mask)

# print("")

#print(i2osp(pad_m_mask,key_length(pad_m_mask)).hex())

m2 = '5968ebbfe00e862ddb35625c14d27e68bc0573e4ef93afded601efcd637be95f62e1696ff57a45b866ab80f81dc718ed4a00caa1b737db1cfdc0aa12bd8bb5d5d79298d35ecb68153ba5d9bb2bb06d66d0675aad359f632afdaca7046289a14217ff8d395dcdcf67bdf1b3b41ffc09d444b1a21d2799fee5361104879e7b7acfa165ee48f5964c5a62fb393aafb23ba6af86f9241ec5a9940a83d294aa67d7a650d02a8f80fadd851adeecdd4ed4f6bfe35db4b7bdca4e3aeada93961787835b56d5a383a641603090283c100bf2a0440336e1c558f5c00b46778b05eac31df9fe503a445f66c0252d0bfbb8347d2d027aa02b3c7764d39a26baf22b89069424'
m2_int = int(m2, 16)

m2_int_mask = m2_int * modinv(random_number,n_dir) % n_dir
# calcul de l'inverse de random modulo n
print(i2osp(m2_int_mask,key_length(m2_int_mask)).hex())


