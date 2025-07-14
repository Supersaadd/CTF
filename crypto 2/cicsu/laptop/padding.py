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

m = "I, the lab director, hereby grant quentin.de_magalhaes permission to take the BiblioDrone-NG.".encode('utf-8')
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

# print(i2osp(pad_m_mask,key_length(pad_m_mask)).hex())

m2 = '690681bcd32c2e1cb40f27232a8a64ac748362c4b66febbdd1cdd087bdfd7aa9a0d1503b752c92e68dba5e4a66b098c502ba3cff4b05701eec2b9c2b6eb57393283465bc250a2437b0e30a1f6c0053a7cb13b7d2ad2bb1793bb4b41d446f1f08251ce30b356a3cc7851a57b6c1e80060e098d67503da4551656f68cb54b3669581f8e228dfe124f8e725f9f7b07cca81bc0d3626d35d68d030ea1333c36e0eb68f0a22617d9313b20f76147ad22cd06b11bf72ef757c38b386f6c00bcc0da604f08435e20439c1162f24af52ec0b2f766d186071d523dbd65b2d6c084455646a66ab8daea7cc21d6b17ae6f05dd988f51d3310fd5397b68419ae742e45721a1e'
m2_int = int(m2, 16)

m2_int_mask = m2_int * modinv(random_number,n_dir) % n_dir
# calcul de l'inverse de random modulo n
print(i2osp(m2_int_mask,key_length(m2_int_mask)).hex())


