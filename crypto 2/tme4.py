from sympy import isprime, primitive_root, primefactors, randprime, prime, factorint

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

a = int('868abe6288c42c8318cf2e3a5cb475864428aff3e30fdbe849e82aadb049a8bca5c55cdac16d5e4e43ef344e97c625d1c1af766c96f87a8f380182afb515694ee6526baf9b5de88b6893b1b1eb435428dd3eceafa6b2054a667ca71d97762c88d953750e3840b9518df0a885346145b377ecb8c4c325238c500f08d39b0a8056',16)
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
print(pratt_certificate(prime_numbers,p))
# print(pow(3,85600,85601))
# print(pow(3,85600//5,85601))
# print(primefactors(7918))


