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


a = "407517aa0806eeba85ad8db3227c4a0ea928e12ac8c6cafe5ccb9dff4d70c08f6bdedc66530b06999cb5026b432c2f12962cb05cc73d059b05a83a39f70ed310cabc5c42b3e33fba75d1049f97bac9183cc9a76025e032d4745f8bf031a6733e44cdfe8af3546a68647ae17d5f04c5dc6a2fe14bfac23c90f6e413a80f8349d673799fe2a6638c1ef408630cd632199fba20a244506f5c6a4b4f0c2df59e28037bb42c53cfe3a9c59bb750b80c1684a4626508999fda68a4390e9d795f3ef6de19c68009cc4b0a094698b594915d84583d5796ef3df09d2f68c15163e93c2abf150105d555c45203d0704243930e7d97306d0a8fae22f65940dbfda190b646cb"
a = int(a,16)
b = a + 2**1950
q = " e03099a8f8d888ff4aadda878af0345cfae003dce3f7b709c4f63f72709d4a02026e58ecd4e390b45d680d35750bc4e1"
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