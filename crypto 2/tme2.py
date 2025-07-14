import random
import sympy

a = int("ae95278ea9a5f5d4b5fed076c8724234b44583404bb92ec874cb9f32e4ebe061c099485c081da0de1a3b88908e34d1dc90abb4a951cf71b6f630415127139b376014d3ec0894037d85a8494531b9a08658c42492c937be6c3ce577c2aca63367fcc5e4b89305a926f7386cde1245c653460f123c81d8d300aa89e7d093c86491841afb8f3ed1c4b550e24e7439ba6dbe3103187451f21adac2255c4016d7b6cbca02f4a870d3bcf9de7c08cf3e279917570d1b044ac0510201a5fa77982c24f64d1748bb82a7ea5e3e283197bc50ea5cf09ff681cb0f13c6ed3297bcd9a81990ca80f34c2b47a66f67c7d418101ecabd65be44c90f29ade0f036ef2c532df4bf",16)
print(a)
print('\n')
b = a + pow(2,1950)
q = int("fb309af7d26648de3ed00651e101c29ecaddf0ab528d943c62b8426b18b912493cf628b30d28eaaab5779e0df19b1cb3",16)
print(q)
print('\n')

def premier(a,b,q):
    r = random.randint((a-1)//(2*q),(b-1)//(2*q))
    p = 2*q*r+1
    
    while True :
        r = random.randint((a-1)//(2*q),(b-1)//(2*q))
        if (sympy.isprime(r)):
            p = 2*q*r+1
            print('oui')
            if (sympy.isprime(p)):
                return r

def premier2(a,b,q):

    # Multiplier les nombres premiers entre eux
    result = 1
    for i in range(150):
        result *= sympy.prime(i+1)
    result = result * q
    borne_a = (a-1)//result
    borne_b = (b-1)//result
    while True:
        r = sympy.randprime(borne_a, borne_b)
        p = result * r + 1
        if sympy.isprime(p):
            return r, p
    

r, p = premier2(a,b,q)

g = q-1

print(p)
print("\n")
print(r)
print(a<=p)
print(b>=p)




