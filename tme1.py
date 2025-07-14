import random
import sympy

a = int("3cfb7e74b46f1386e31e932bebbc272032213afb50a0c3611db16829036bd1729b3cbd736779dc9ce12204ae8198f77ed064501dd83034473aa5f4e0c2cff52cfb5439751ca54e2dcb5b6a02196b5c14d4c055793d674948d4c8a9bdd80110aafcaaa610de652e3edfd1f5ddfe075384a8136915ca13d67f269468396c0db485d5a80bf8d4d7392c9bf410446afcc7739e05fd3a74504d2022d3c46cce6eaeb4678e892ab197644b60c1b9523aa7b6f9ab2b36ef911578dff05eca5e662ad849e509c159d02aa88ac0aff46ef0f46722b14ecd2dfc78187b1a33b8c979da64fffee26c445afb98bdc3a75cc329b0825c4d598b226265bd6c52fc010095f140b7",16)
print(a)
print('\n')
b = a + pow(2,1950)
q = int("8f114ce7e1eeee3672b938da301c90fff5b592a72d988065994113c819cdd521",16)
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
