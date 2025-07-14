
import math

def xgcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        g, y, x = xgcd(b, a % b)
        return (g, x, y - (a // b) * x)

def crc64(m : bytes) -> bytes:
    i = int.from_bytes(m, byteorder='big')
    i <<= 64
    k = i.bit_length()
    Q = 0x1000000000000001b
    while k > 64:
        i ^= Q << (k - 65)
        k = i.bit_length()
    return i.to_bytes(8, byteorder='big')

hash_pwd = "7c9f22238d53ff18"

def find_input_polynomial(crc_output):
    # Step 1: compute inverse of (x^4 + x^3 + x + 1) modulo Q(x)
    q = 0x1000000000000001b
    _, inv, _ = xgcd(0b100011011, q)  # 0b100011011 = x^4 + x^3 + x + 1
    inverse = inv % q
    
    # Step 2: compute P(x) = I(x) * S(x) modulo Q(x)
    s = int.from_bytes(crc_output, byteorder='big')
    p = (inverse * s) % q
    
    # Step 3: add zeros to the left of P(x) to get degree 63
    degree_p = p.bit_length() - 1
    p = p << (63 - degree_p)
    
    # Step 4: return P(x)
    return p.to_bytes(8, byteorder='big')

polynomial = find_input_polynomial(bytes.fromhex(hash_pwd))
print(polynomial.hex())

hashpwd = 0x7c9f22238d53ff18 ## se trouve dans le menu 1 du terminal salle 112 
binary_pwd = bin(hashpwd)[2:] 
print(binary_pwd)
#code sage

bin = 0b0100110011101100110001001010100100001110101100000010111101001110

print(hex(bin))