from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_message_hex(message, public_key_pem):
    # Convert the key string to a proper PEM format
    public_key_pem = f"-----BEGIN PUBLIC KEY-----\n{public_key_pem}\n-----END PUBLIC KEY-----"
    
    # Load the public key
    public_key = RSA.import_key(public_key_pem)
    
    # Create cipher object
    cipher = PKCS1_OAEP.new(public_key)
    
    # Encrypt the message
    encrypted_message = cipher.encrypt(message.encode())

    # Encode in hexadecimal
    return encrypted_message.hex()

# Given public key
public_key = """MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApCypcnapVKDb9aTG69qv0F7QUrgxWuNoKNuUVEdTWGiivN+Co8VHMpcB5Hh7LhRvx0DxdPluPWYVptWNjoAw5s9FgTwNe4/74Ckhpiv5BdtPxlpt5onbjfOsdXw8RuiH55LXOMY6kNa1wINHGD+LgUqk8eIQ1Archoc4BAjkEwDodAzk27TyESoJx+dUQ06fzzu4m+gyAjVDH77Sm9Jg3MTbmYtnpng7ICwfCbhwEqP46NwomQJJejpJeZbJ3E5OioKBfGMui4H7UaLTYFRm6RUtJtdJRQVpcNvhyBJGM1xcEq2GgEniHx9OF254D0HlN5xJqJfB7q8zQ6CpnI+AfQIDAQAB"""

# Encrypt message and get hex output
encrypted_hex = encrypt_message_hex("I got it!", public_key)
print("Encrypted (hex):", encrypted_hex)
