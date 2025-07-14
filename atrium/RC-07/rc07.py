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
MIIBPTANBgkqhkiG9w0BAQEFAAOCASoAMIIBJQKCAQEAnBr09mrmQvoGweTHxKQ2
/dOG1VdjvIIP4Sa/TRt1CaZkA+rLqZ13nUCvIGBC5wmN+DCBcXuSIcjtAmuKCQNL
xQI1t2QD2ImPuRWT96MpGnSydglLTgF7ZmL6SbR+Bqm9RomM9FVngYd3pk18GwSF
63FOqY4C/4gton+5C7yuPk5XTHYYDx2lDnqfsVnwt8UpJp+Gflpog6xJixbwCTGD
pBB51S8C246nEu5s3RgG84MhSxjAj2iyPZVvIYdc84gzKxwr0rQBbkBQXy1fx9rb
XUtOLkK5rQpB8oxVtrpePgUOaPYNay4jWyK09G3g8o0sg+FTuLxqe9IEBOW+IsoF
WwIeULJEU6RappGE8aJGjeNXRwAAAAA+++ATRIUM+++B
-----END PUBLIC KEY-----"""



cle_publique_2 = """-----BEGIN PUBLIC KEY-----
MIIBQDANBgkqhkiG9w0BAQEFAAOCAS0AMIIBKAKCAQEAnBr09mrmQvoGweTHxKQ2
/dOG1VdjvIIP4Sa/TRt1CaZkA+rLqZ13nUCvIGBC5wmN+DCBcXuSIcjtAmuKCQNL
xQI1t2QD2ImPuRWT96MpGnSydglLTgF7ZmL6SbR+Bqm9RomM9FVngYd3pk18GwSF
63FOqY4C/4gton+5C7yuPk5XTHYYDx2lDnqfsVnwt8UpJp+Gflpog6xJixbwCTGD
pBB51S8C246nEu5s3RgG84MhSxjAj2iyPZVvIYdc84gzKxwr0rQBbkBQXy1fx9rb
XUtOLkK5rQpB8oxVtrpePgUOaPYNay4jWyK09G3g8o0sg+FTuLxqe9IEBOW+IsoF
WwIhANzMfAtyXQ/9vjjrebuZgzsAAAAAAAA+++ATRIUM+++B
-----END PUBLIC KEY-----"""

print(cle_publique_1==cle_publique_2)

cle_publique_1 = serialization.load_pem_public_key(cle_publique_1.encode(), backend=default_backend())
cle_publique_2 = serialization.load_pem_public_key(cle_publique_2.encode(), backend=default_backend())

print(cle_publique_1==cle_publique_2)
cle_prive_1 = """-----BEGIN RSA PRIVATE KEY-----
MIIEvgIBAAKCAQEAnBr09mrmQvoGweTHxKQ2/dOG1VdjvIIP4Sa/TRt1CaZkA+rL
qZ13nUCvIGBC5wmN+DCBcXuSIcjtAmuKCQNLxQI1t2QD2ImPuRWT96MpGnSydglL
TgF7ZmL6SbR+Bqm9RomM9FVngYd3pk18GwSF63FOqY4C/4gton+5C7yuPk5XTHYY
Dx2lDnqfsVnwt8UpJp+Gflpog6xJixbwCTGDpBB51S8C246nEu5s3RgG84MhSxjA
j2iyPZVvIYdc84gzKxwr0rQBbkBQXy1fx9rbXUtOLkK5rQpB8oxVtrpePgUOaPYN
ay4jWyK09G3g8o0sg+FTuLxqe9IEBOW+IsoFWwIeULJEU6RappGE8aJGjeNXRwAA
AAA+++ATRIUM+++BAoIBABoFj7Kriiwo/UwhybK+WaR8Wg7tbP0RbzpuVbKxyadp
tCbT5NSxAQJ/rcwUYb6TZUbAH9OY38J846W0ilb9tSIqhy3GD8GtBt/wOZuBBpmE
UaIrtQ7gHb2pTDAsVZtfH3EkvBRezw8Lbe2WRBSBTqThTviIYaG6bxGydLCqIofq
5B+jy+D2Dwp5/ciHu6ly+NQRn6XCqtkgQbrEWYS7H1LTlZ2E4VCTkHFBOUnmBoSA
TLneJcmy1j0/sE2WBR2sdVOUoDlmrrgX0wNYsMTaUkQHHbG3m7wTNBRqunbMyhM1
/dLU4QmtWizHWvBwzL5EvVLloHvxVKfxHHzdmgBvEzECgYEA1lrRcBao4SVr2cFn
qNYLrViL2QnGjlHEcwkF3MWHV85u58It4g0XrlT6l0Sj+9P5vRkkT8HIMI+hs1Ho
U6Z9ZO6ndgp0q9GlntPO2MPs98GzjOBgZAQ+Q0OgqJNx+KskM8lZUCslmOGoP0it
cIYMntGGTVZIkf7qtz+eyw/2xQcCgYEAum8I2vJh9/NGpNJIPr1F+seoUfcVE2DA
LLb3/eGuQV2m+sVNrOpR6jP7xaiztOeBUckXpADh8qRxWHF9IIsINjbdEyFxR2iz
mwE984LRTM6NTDX9dvf9IyvnSZ/tv2+Wsp939d/oUT+P4m/gpV6SpskyMtMW+C+V
oedQv6KQ3A0CgYAd5Z+gF2yDTqcehmMTMwt910RCuR2gV4okSGdSHTSL+tReFGmY
cWW9jYwaTpmo6JZ9EJyST9k7WHPere0MkGWKaAKXEPy+NkeF4FlRpIFNP5teFFdF
LJCEyhXeUB8AfusqNh+402IdCB7eEB4lUd6uzKc+e1jp5MMSXVf02PUtawKBgQCG
xXG3eyJ26omXezqBHR5n44bRem0USLf2RTR7sePz/mRbq3y7M7FASihgpqcrialI
UQuqFvdnPTqyyMq/UcSwsoqT3PTOu9H62qMQwgV9BZCAShmxeEGJBnNvFcTeLxMU
wC35DcZTZKuHGNTZF3zorkIxSUQhYlJMdr0m4QVFBQKBgHew8u0pP/Vc3gMkan6R
VNmhZBo+bGixuYnddMVGG03CzAGRBVGjuHWrpZJRSsEz+zTpeCdFIVPv9Prr83Gu
bEi2DehgJzf8pCvo2DcIDxcY9xXb0c5f+9GS66aKiyAHrMKLtdpZTxRCmCusnWUP
pEZIEbeuTSQJC8YPt7ZP1Zxo
-----END RSA PRIVATE KEY-----"""

cle_prive_1 = serialization.load_pem_private_key(cle_prive_1.encode(), password=None, backend=default_backend())

e1 = cle_publique_1.public_numbers().e
e2 = cle_publique_2.public_numbers().e

n = cle_publique_1.public_numbers().n
d = "1a058fb2ab8a2c28fd4c21c9b2be59a47c5a0eed6cfd116f3a6e55b2b1c9a769b426d3e4d4b101027fadcc1461be936546c01fd398dfc27ce3a5b48a56fdb5222a872dc60fc1ad06dff0399b8106998451a22bb50ee01dbda94c302c559b5f1f7124bc145ecf0f0b6ded964414814ea4e14ef88861a1ba6f11b274b0aa2287eae41fa3cbe0f60f0a79fdc887bba972f8d4119fa5c2aad92041bac45984bb1f52d3959d84e150939071413949e60684804cb9de25c9b2d63d3fb04d96051dac755394a03966aeb817d30358b0c4da5244071db1b79bbc1334146aba76ccca1335fdd2d4e109ad5a2cc75af070ccbe44bd52e5a07bf154a7f11c7cdd9a006f1331".encode('utf-8')
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

c = "sonny threw mamas lemma doted".encode('utf-8')
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




