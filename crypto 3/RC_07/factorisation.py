import math
from math import gcd
import random
from decimal import Decimal


def puissance_modulo(base, exposant, modulo):
    resultat = 1
    while exposant > 0:
        if exposant % 2 == 1:
            resultat = (resultat * base) % modulo
        base = (base * base) % modulo
        exposant //= 2
    return resultat


def factor(N, e, d):
    x = 7 # arbitraire + à changer si ça marche pas
    s = 0
    ed_minus_1 = e * d - 1
    while ed_minus_1 % 2 == 0:
        s += 1
        ed_minus_1 //= 2
        y = pow(x,ed_minus_1,N)
        if not(y == 1 or y == -1):
            p = gcd(y-1,N)
            return p, N//p

    return None


 #Samuelcooper
d1_string = "acc29327b9147142102c4cf26f18df4d8176007d8f5657972441c541ea4ebbdbdcf9f5e2a845f96e1bca2873277459e2f9f9a8ed2c5dce3f533619dfaa1687b8e688cf8cf551daac2dad3472ceeebf0892cad8f56c08c15f2bf4ca22a0d64839c977bbd6bd17f8563c8fb3826a84f60b8ccaef37e425e2bef120779dabf64bbb7eb7262b981794e1a20d5dd75c735f05255e9a27e99c319b744f1afeb134fde15f3fa71720c5543962c1b4a275e5e63147b684c16383c3f42b22626292f17ca9f78b5b54f9e743903453687690a089fd8b9a82d66d8de28b332da298332eaf11e68d666ce3d1e187129e8a57c1f3832e4033db6e38c87208010e48dee05c7aa1"
d1 = int(d1_string, 16)

e1_string = "2c4a097aee31acf9092aa96462314609000000003efbe01344850cfbef81"
e1 = int(e1_string,16)

N_string = "00c47c16cb5f88252a29c806a381cf0c809305d5eb2aa7192f44d82d5d83f890e93007c757c8cf8673f8172095942a70d3ffa00bc39b91dff5ff477048d42d673495747e8bce62d6cee33262e973543c67e4f41080d3193949ec6c88347e6f71ed7a325dfcc3b7b0bd654357191d47b1342feaafeb3de0210b69c11bc31e39c6921b51d658620a6276de03059ebb4e13abcb0be96f0407973be6391e948eea0194471cd388ff33c0fa81a741199411ed7a4a633ae3afa7a9045e2955354fc37cc14efa9ee99a617cf5645f12be5d61013d693dfc59e8183c7dc60a8e909d888ca8f576456e9e0bbea0d74e7597398c196a37c7383c8b871a31112213dc190eabe9"
N = int(N_string, 16)

 #Kelly05
e2_string = "7ed3389ef19040b32197eb970200cab5000000003efbe01344850cfbef81"
e2 = int(e2_string,16)


p,q= factor(N, d1, e1)

print('e=',e2)
print ('p=',p)
print('q=',q)
print(p*q==N)

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


def mod_inverse(e, p, q):
    phi_n = (p - 1) * (q - 1)
    gcd, x, y = extended_euclidean_algorithm(e, phi_n)
    if gcd != 1:
        return None
    else:
        return x % phi_n

d2 = mod_inverse(e2,p,q)
print('d2=',d2)