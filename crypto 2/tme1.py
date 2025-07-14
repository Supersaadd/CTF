import random
import sympy

a = int("3fe59ed3ea8d7045ff2d02eb1fd1af5ea99db536783b1a716f7e9dd47d5c040e26e5a21c06d75e74cb3f142e9d1aa5a8f447ee3885dca4470f352f90614e6a21f89692b4be205e2186ed18d62a557368c53e3f433f7bb44c52535bb3a2ea17eaeaf60977c177ab8162dfdad2d1bf9e3a7d38fb36f3e8ad260741dd05dafd4202b2cd35a6eeb3721d9f7bcb12df53c0bcecef2f43f416fe09e3981ed440c02e6b85d7c5ee560c26b67602f05ff9018448b2e53a3bb964f8e9be5d3897e84b3638dce9370de3536b195e8bc5e4a588da5beaefe60440833034b34288cdc9b0b91f7a87763a7fd02224ccaecbcedc82e21ca7f6255bbe1ef3894b7245eeb1738c84",16)
print(a)
print('\n')
b = a + pow(2,1950)
q = int("eddf9bf686c41183ce2f6ba574cfc3d428fbc507be923f0240a666d01631a70f",16)
print(q)

def is_prime(n):
    return sympy.isprime(n)

def find_prime_in_range_with_condition(a, b, q):
    b1 = a//q
    b2 = b//q
    pair = b1
    if(pair%2 !=0) :pair+=1
    p = 1 + q * pair
    
    while is_prime(p) == False:
        pair += 2
        # if(pair%2 !=0) :pair+=1
        p = 1 + q * pair
    return p

def fast_pow(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result
   

def find_generator(q, p):
    g = 1
    print(g)
    while (g == 1) :
        x = random.getrandbits(256)
        print(x)
        g = fast_pow(x,(p-1)//q,p)
        print(g)
    return g


        

p = find_prime_in_range_with_condition(a,b,q)
g = find_generator(q, p)

print("p =", p)
print("g =", g)

if(fast_pow(g,q,p)==1) : print("on est bon")
else : print (fast_pow(g,q,p))
