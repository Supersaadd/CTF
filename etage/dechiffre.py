import galois

# Define GF(2^64) with the given irreducible polynomial Q(x)
Q = galois.Poly.Int(0x1000000000000001B)
GF = galois.GF(2**64, irreducible_poly=Q)

# Define the divisor: x^4 + x^3 + x + 1 = 0b11011 = 27
divisor = GF(0b11011)

# Compute inverse of divisor in GF(2^64)
divisor_inv = GF(1) / divisor

# Given CRC64 value as hex
target_crc_hex = "f70a4644680f7443"
S = GF(int.from_bytes(bytes.fromhex(target_crc_hex), byteorder="big"))

# Solve for P(x): the input whose CRC equals the target
P = divisor_inv * S

# Convert result to bytes
P_int = int(P)  # This replaces P.integer
password_bytes = P_int.to_bytes(8, byteorder="big").lstrip(b"\x00")

# Print results
print("Recovered password bytes:", password_bytes)
print("Recovered password (ASCII):", password_bytes.decode(errors="ignore"))
print("Recovered password (hex):", password_bytes.hex())
