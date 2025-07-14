def separate_hex_to_64bit(hex_number):
    # Vérifier que la longueur de la chaîne hexadécimale est correcte
    if len(hex_number) != 64:
        raise ValueError("La longueur du nombre hexadécimal doit être de 64 caractères")

    # Diviser la chaîne hexadécimale en blocs de 16 caractères
    blocks = [hex_number[i:i+16] for i in range(0, 64, 16)]

    return blocks

# Fonction pour lire les nombres hexadécimaux à partir d'un fichier
def read_hex_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        hex_numbers = file.readlines()
    return [line.strip() for line in hex_numbers]

# Nombre hexadécimal de 256 bits
hex_number = "3F1A7BCE9D2F864A5B71E09832FA6254E34D17B79CA7F8B9F01E2D635A47BC9A"

# Lire les nombres hexadécimaux à partir du fichier
hex_numbers = read_hex_numbers_from_file('mac.txt')

# Afficher le deuxième message de chaque nombre hexadécimal
for hex_number in hex_numbers:
    # print(hex_number)
    messages_64bit = separate_hex_to_64bit(hex_number)
    print("(", int(messages_64bit[0],16),",", int(messages_64bit[2],16), ")")


print(hex(5265777339925664956))