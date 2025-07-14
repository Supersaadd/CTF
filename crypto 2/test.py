def gcd_extended(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, u_prime, v_prime = gcd_extended(b, a % b)
        u = v_prime
        v = u_prime - (a // b) * v_prime
        return gcd, u, v

# Exemple d'utilisation
a = 47
b = 18
gcd, u, v = gcd_extended(a, b)
print("PGCD de", a, "et", b, ":", gcd)
print("Coefficients de Bézout (u, v) :", u, ",", v)
