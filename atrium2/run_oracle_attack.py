from binascii import unhexlify, hexlify

# Given ciphertext blocks
Y2_hex = "f56946ddd15e6c1be7c124de6a8999e4"  # block before the last
Y3_hex = "85a60fef7f30a77e7991d929259e3c66"  # last ciphertext block

Y2 = bytearray(unhexlify(Y2_hex))
Y3 = unhexlify(Y3_hex)

print("🧪 Trying all guesses for last byte of plaintext...\n")
for guess in range(256):
    # forge IV such that last byte of plaintext becomes 0x01 if guess is correct
    forged_iv = Y2.copy()
    forged_iv[-1] = Y2[-1] ^ guess ^ 0x01

    iv_ct = hexlify(forged_iv + Y3).decode()
    print(f"👉 Input into tas (Single or Batch):")
    print(iv_ct)

    user_input = input("✅ Was padding valid? (y/n): ").strip().lower()
    if user_input == 'y':
        # Found the correct guess, calculate plaintext byte
        dkn_last = forged_iv[-1] ^ 0x01
        plaintext_last_byte = dkn_last ^ Y2[-1]
        print(f"\n🔓 Recovered last plaintext byte: {plaintext_last_byte:#04x} ({chr(plaintext_last_byte) if 32 <= plaintext_last_byte <= 126 else '.'})")
        break
