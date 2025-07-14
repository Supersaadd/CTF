from sympy import isprime, primitive_root, primefactors, randprime, prime, factorint
import json

def premier2(a,b):

    # Multiplier les nombres premiers entre eux
    result = 1
    for i in range(123):
        result *= prime(i+1)
        
    prime_numbers = [prime(i+1) for i in range(123)]

    result = result * prime(2)
    prime_numbers.append(prime(2))

    # result = result * prime(123)
    # prime_numbers.append(prime(123))
    print(a)
    print(result)
    borne_a = (a-1)//result
    print(borne_a)
    borne_b = (b-1)//result
    while True:
        r = randprime(borne_a, borne_b)
        print(r)
        p = result * r + 1
        if isprime(p):
            if p>b or p<a :
                print('problem')
            #ajoute a prime_numbers r
            prime_numbers.append(r)
            return prime_numbers, p

def pratt_certificate(pm1_factors,p):

    g = primitive_root(p)
    for i in range(len(pm1_factors)) :
        if pm1_factors[i]>1024 :
            e = []
            facteurs = factorint(pm1_factors[i]-1)
            for facteur, puissance in facteurs.items():
                e.extend([facteur] * puissance)
            pm1_factors[i] = pratt_certificate(e,pm1_factors[i])
        else :
            pm1_factors[i] = {
            "p": pm1_factors[i]
            }
    certificate = {
        "p": p,
        "g": g,
        "pm1": pm1_factors
    }
    
    return certificate

# print(primitive_root(7919))
# print(primefactors(7918))
# print(pratt_certificate2(8675309))

a = int('a539aa5ff7c584023ce45bd0b08d4d2c599704619ddd9060e905374ceccc3a98b246356dbcc766a8e0bf1c6b2774793d6f2df79d7c421485472d531b864513b8a96246198aabd2e876dafe92ca19e2b782d2b413526df38dc68516168facc1f8971f7d98c7b7473799175c7c421518f4002b0d875276c877dcc47511e7c564ab',16)
b = a + 2**960

prime_numbers, p = premier2(a,b)
print(prime_numbers)
print(p>=a)
r=1
for i in range(len(prime_numbers)) :
    r=r*prime_numbers[i] 
print(r+1 == p)
print(r+1 <= b)
print(isprime(r+1))
print(prime_numbers[-1])
pr = primefactors(prime_numbers[-1]-1)
print(pr)
r = 1
for i in range(len(pr)) :
    r=r*pr[i] 
print(r+1)
print(12565235981)
print(factorint(12565235981-1))
facteurs = factorint(12565235981-1)

facteurs_premiers = []
for facteur, puissance in facteurs.items():
    facteurs_premiers.extend([facteur] * puissance)
print(facteurs_premiers)
certificat = print(pratt_certificate(prime_numbers,p))
print(json.dumps(certificat, indent=2))  # Version lisible avec indentation

# print(pow(3,85600,85601))
# print(pow(3,85600//5,85601))
# print(primefactors(7918))


