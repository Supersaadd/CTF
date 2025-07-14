from hashlib import sha256

# Function names respect those in https://www.ietf.org/rfc/rfc3447.txt

# SHA-256
HASH_ID = b'010\r\x06\t`\x86H\x01e\x03\x04\x02\x01\x05\x00\x04 '

def extended_euclidean_algorithm(a, b):
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def mod_inverse(e, n):
    
    gcd, x, y = extended_euclidean_algorithm(e, n)
    if gcd != 1:
        return None
    else:
        return x % n
    
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

def emsa_pkcs1_decode(EM : bytes, k : int) -> bytes:
    """
    Given an EMSA_PKCS1-encoded message, returns the Hash

    >>> x = emsa_pkcs1_encode("toto", 128)
    >>> emsa_pkcs1_decode(x, 128) == sha256("toto".encode()).digest()
    True
    """
    if len(EM) != k:
        raise ValueError("Incorrect Size")
    if EM[:2] != bytes([0x00, 0x01]):
        raise ValueError("Incorrect Header")
    i = 2
    while EM[i] != 0:
        if EM[i] != 0xff:
            raise ValueError("Incorrect Filler")
        i += 1
        if i == k:
            raise ValueError("Only Filler")
    if i < 10:
        raise ValueError("Not enough filler")
    T = EM[i+1:]
    if T[:len(HASH_ID)] != HASH_ID:
        raise ValueError("Bad Hash ID")
    H = T[len(HASH_ID):]
    return H

def key_length(n : int) -> int:
    """
    key length in bytes
    """
    return (n.bit_length() + 7) // 8

def rsa_pkcs_sign(n : int, d : int, M : bytes,x : int):
    """
    RSA Signature using PKCS#1 v1.5 encoding
    """
    k = key_length(n)
    E = emsa_pkcs1_encode(M, k)
    Msg = os2ip(E)
    m = (Msg* pow(x,e,n))%n # "masque" le msg renvoie un int
    #m = os2ip(EM)
    s = pow(m, d, n)
    S = i2osp(s, k)
    return S

def rsa_pkcs_verify(n : int, e : int, M : bytes, S : bytes,x : int) -> bool:
    """
    Verify RSA PKCS#1 v1.5 signatures
    """
    k = key_length(n)
    if len(S) != k:
        raise ValueError("Bad length")
    s = os2ip(S)
    new_s = (s*mod_inverse(x,n))%n # on enlève le masque
    m = pow(new_s, e, n)
    EM = i2osp(m, k)
    H = emsa_pkcs1_decode(EM, k)
    return (H == sha256(M).digest())


# Avant d'utiliser fonction de hachage il faut encoder msg (str) en séquence d'octets (bytes)
msg = "I, the lab director, hereby grant lucie.miniaou permission to take the BiblioDrone-NG."
M = bytes(msg, 'utf-8')

"""
C = emsa_pkcs1_encode(M,128) # renvoie haché + bourré
C_hex = C.hex() # on encode en hex pour pouvoir l'envoyer sur le laptop
D = emsa_pkcs1_decode(C, 128) # quand on déchiffre renvoie msg haché
"""

"""
# Pour faire des tests
p= 156301611243904127570418288894110519710586145252297905037920162558768676977571134894211980196428993225545882394929470365182963234518861819347190322809703599567788514634457762705839656105921316570275686086204516489690079287703732342429993844001860962351964335907234702828734126933925466313241908265924807752459
q= 158692531462322899623219730604257843779550564762240175358037344233620627395235550578983205720504171190738526455139889514968141467207097868430059274563556939131862140265997200610516671472015262738425778500740032242650671973001686014190025419142593392499475560901171800964311930595898308495028354215070798490971
n = p*q
e = 875314551316320833352656573463853722192827407721124435544214772419129217
d = 3823304331075417366637177549554574250582303565489708236632910831300404431597837156160402539378780413579785827038695066275159826799897623421846930107713164814069224945154309354481081796681592343281964202758783281815373541850795718025162265869533455875900407773829470254198668925163391507422075763644149636024151195422995822928118705619093317653390552779557734786208484173411012226027108013884984514039094433385838087630914502834062080978982070911502535774613649326278926518410146002354534836070740963494828681140987686175499636266755299049486109950003511690613340951927904137877336066759766744000264830118430221387353

x = 26

S = rsa_pkcs_sign(n,d,M,x) # avec dernière étape de l'encodage effectuée par laptop
print(S)
print(S.hex())
print(rsa_pkcs_verify(n,e,M,S,x))
"""


#Msg = int.from_bytes(msg.encode(), byteorder='big') # transforme str en int
#New_C = (os2ip(C)* pow(x,e,n))%n # "masque" le chiffré
#New_M = i2osp(New_msg,128*2) #converti int en bytes

#print(hex(New_C))

#New_s = rsa_pkcs_sign(n,d,New_M) # signe msg masqué
#print(rsa_pkcs_verify(n,e,M,New_s*mod_inverse(x,n)))

#New_c = emsa_pkcs1_encode(New_M,128)
#New_c_hex = New_c.hex()

#print(D == sha256(M).digest())
#print(C_hex)


# clé publique directeur
n_string = "00bed6cdc8f142d61854b6bddc6f9eb36bbbf4e5dab77207240078293c384eb53d4e3a0b2f250d6dd1192448973b250d563517218c90a12c0447f5b31df37410d8a2e21573c0f05a8aa9924114708053b08878d3b53ccd35ba3516c02c3692d048ad46e98b7fbe13a99b4670fcc96dd51e7a04a3da93493ab5b5b0ff7ae77708d74f8c964112523fed59c1bdc949bfea248ff0a39285302b0292a6b8de23f98a920135cf1b5660e16eb4fddbb24b4312ef5c59f4a02a67dff2b28a6d1b0c3e3942c1736faa43a94f0995e04bda6c873a1cbaf6685424196abc6185d3e40fc1cc276fae72de0465d9748e6eb7e165b62800a53f2c67e4693cc92b37a9ee4bc449e9"
n = int(n_string, 16)
e = 65537

### Création de la signature ###
msg = "I, the lab director, hereby grant lucie.miniaou permission to take the BiblioDrone-NG."
M = bytes(msg, 'utf-8')
k = key_length(n)
C = emsa_pkcs1_encode(M,k) # renvoie haché + bourré

x = 26
New_C = (os2ip(C)* pow(x,e,n))%n # "masque" le chiffré
print(hex(New_C))


S = "bb7e4c28ed63d08c5a9d575acdefc1bbbb8a8824228d66b0c8cf4b8ead827f18dbed93335341639ce76bb1747d2a860b6e5a80b9cd969305c32cf372e4fd1dd1b0896d696120335b1292e2c03cb9b9a66ea4751c4a78941a1b99071ff07a14aa9d348144139b816929c3d64619aa5d95458683ae846bef672a54d02f8a60aab5ca7cdff96d87ae50244282acf9bfb491f658d18b1120a86f88017cd58f82b625bb9ee42aab1442f7eac96b38d245a3824b1931543b5ffdf971ac5f6c4e27b4ee2e4c29554b5cfad92cd320621c0753ee6b901887513d92563edaa0e066f1e6c8c90fec328b655c5e8c19214eec685d2a0cb4411a36794a44bb959d5dd759cb73"
sign = int(S,16)
print("oui")
New_sign = (sign*mod_inverse(x,n))%n
test = i2osp(New_sign,k)
print(test.hex()) #on élimine le masque

