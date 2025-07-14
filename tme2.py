import random

def xrange(k):
    return (i for i in range(k))

def miller_rabin(n, k):

    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in xrange(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in xrange(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def bit_size(a:int) -> int:
    return int((a.bit_length()+7)//8)

def int_to_bytes(a):
    return a.to_bytes(bit_size(a),'big')

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x


a = "3ed5fe8a510c1864203e13b0a92fdfcb95cbc3f1137af1407ba0983dd5ab59dcae800c3e94eff41e4493eacf33407f344060956a0064e0069b0d5f2ee93aa15d8c406ccc6b02442f19c9f5d051e3c7dcb6f65f2349b12fba57ae26e43f724305ca5d6d375e6c358accf93a627ece0618994b9f57185e98a6c6708f98c03092de1a5548e63f33ab005e4ddc53704483161c762fb7ceddc213aa76d604ddbe2c6ef50e8f554c1a79ce808d390282a3f7740decbb3cd53155335c4202c3775ba552a8de71a852f603fb31c8cc7bab2f227b8ffab2f354e245d1afd897c0829af15afa2ebb05a03998cdf6381cdb87dc48d1ec39c9f6eb7a5ab61a70e056cc49451f"
a = int(a,16)
b = a + 2**1950
q = " b79197fcbea7e4502d30deee08a05efa277d86e25a4f26f90d4b216b12f0b0da3899210366c64be21c6f83d86c71f497"
q = int(q,16)



c = 20000 #constante arbitraire
len_b = bit_size(b)
maxQprim = (b-a)//(c*pow(len_b,2))
sizeQprim = bit_size(maxQprim)#242

Qprim = 2*q 
diviseur = [2]    
#contruire Q'
while(sizeQprim != bit_size(Qprim)):
    
    pi = random.randrange(2,min(q-1, pow(2,8*(sizeQprim-bit_size(Qprim)))))

    if(miller_rabin(pi,10) == False):
        continue

    Qprim *= pi
    diviseur.append(pi)


ak = a // Qprim
bk = b // Qprim

while(True):
    pk = random.randrange(ak,bk)

    if(miller_rabin(pk,2) == False):
        continue
    
    if(miller_rabin(Qprim*pk + 1,2) == False): # p premier ?
        continue

    Q = Qprim*pk
    diviseur.append(pk)

    p = Q + 1
    print('p = ',p)
    
    break


n_try = 100

for _ in range(n_try):
    g = random.randrange(2,p-1)
    test = True
    for pi in diviseur:
        if (pow(g,Q//pi,p) == 1):
            test = False
            break

    if test:
        print('g = ',g)
        break

print('(p-1)//q = ',str(diviseur)[1:-1])