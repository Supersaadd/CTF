def separate_hex_to_64bit(hex_number):
    """
    Divise une chaîne hexadécimale de 64 octets (256 bits) en 4 blocs de 64 bits (16 hex chars chacun).
    """
    if len(hex_number) != 64:
        raise ValueError(f"Longueur invalide : {len(hex_number)} caractères au lieu de 64")
    return [hex_number[i:i+16] for i in range(0, 64, 16)]

def read_hex_numbers_from_file(file_path):
    """
    Lit les lignes d’un fichier contenant des nombres hexadécimaux (un par ligne).
    """
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
    return [line for line in lines if len(line) == 64]

def extract_points(file_path, block_index):
    """
    Extrait les couples (X, Y) où :
    - X est le bloc 0 (premiers 64 bits)
    - Y est le bloc `block_index` (1 pour A, 2 pour B, 3 pour C)
    """
    hex_numbers = read_hex_numbers_from_file(file_path)
    points = []
    for hex_number in hex_numbers:
        blocks = separate_hex_to_64bit(hex_number)
        X = int(blocks[0], 16)
        Y = int(blocks[block_index], 16)
        points.append((X, Y))
    return points

def lagrange_interpolation_zero(xs, ys, p):
    """
    Interpolation de Lagrange pour évaluer f(0) modulo p.
    """
    result = 0
    k = len(xs)
    for i in range(k):
        xi, yi = xs[i], ys[i]
        num, den = 1, 1
        for j in range(k):
            if i != j:
                xj = xs[j]
                num = (num * (-xj % p)) % p
                den = (den * ((xi - xj) % p)) % p
        inv_den = pow(den, -1, p)
        term = (yi * num * inv_den) % p
        result = (result + term) % p
    return result

# --------------------------
# Configuration
# --------------------------
file_path = "mac.txt"
block_index = 2  # 1 pour A (R), 2 pour B (S), 3 pour C (T)
p = 2**64 - 59

# Extraction des points et interpolation
points = extract_points(file_path, block_index)
X_vals = [x for x, _ in points]
Y_vals = [y for _, y in points]

# Vérification
print(f"{len(points)} points chargés pour interpolation degré {len(points) - 1}")

# Interpolation
constante = lagrange_interpolation_zero(X_vals, Y_vals, p)
print("Constante =", constante)
print("Constante en hexadécimal :", hex(constante))
