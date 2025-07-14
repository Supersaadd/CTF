import json
import subprocess

class OpensslError(Exception):
    pass

def extract_public_key(cert_path):
    args = ['openssl', 'x509', '-pubkey', '-noout', '-in', cert_path]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode()

def verifysign(signature, pubkey_key, mot):
    args = ['openssl', 'dgst', '-sha256', '-verify', pubkey_key, '-signature', signature]
    if isinstance(mot, str):
        mot = mot.encode('utf-8')
    result = subprocess.run(args, input=mot, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return 0 if result.returncode == 0 else 1

def verif_banque(uglix, cert_path):
    args = ['openssl', 'verify', '-trusted', uglix, cert_path]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return 0 if result.returncode == 0 else 1

def verif_carte(uglix, cert_b_path, cert_c_path):
    args = ['openssl', 'verify', '-trusted', uglix, '-untrusted', cert_b_path, cert_c_path]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return 0 if result.returncode == 0 else 1

liste_valeurs = []

with open('donnees.json', 'r') as file:
    donnee = json.load(file)

    batch_id = donnee.get("batch", {}).get("identifier", "UNKNOWN")
    print(f"\nBatch identifier: {batch_id}\n")

    transactions = donnee["batch"]["transactions"]

    for idx, transaction in enumerate(transactions):
        val = 1
        data = transaction['data']
        data_json = json.loads(data)

        card = transaction['card']
        card_number = card['number']
        certif_c = card['certificate']

        bank = card['bank']
        bank_name = bank['name']
        certif_b = bank['certificate']

        data_card = data_json['card-number']
        data_bname = data_json['bank-name']

        print(f"\nTransaction #{idx}")
        print(data)

        if data_card != card_number:
            print(f"❌ Invalid card number at index {idx}")
            val = 0
        else:
            print("✅ Card number match")

        if data_bname != bank_name:
            print(f"❌ Invalid bank name at index {idx}")
            val = 0
        else:
            print("✅ Bank name match")

        with open('certif_c.pem', "w") as f: f.write(certif_c)
        with open('certif_b.pem', "w") as f: f.write(certif_b)
        with open('pubkey_c.pem', "w") as f: f.write(extract_public_key('certif_c.pem'))
        with open('signature.txt', "wb") as f: f.write(bytes.fromhex(transaction['signature']))

        if verif_banque('uglix.pem', 'certif_b.pem') != 0:
            print(f"❌ Bank cert verification failed at index {idx}")
            val = 0

        if verif_carte('uglix.pem', 'certif_b.pem', 'certif_c.pem') != 0:
            print(f"❌ Card cert chain verification failed at index {idx}")
            val = 0

        if verifysign('signature.txt', 'pubkey_c.pem', data) != 0:
            print(f"❌ Signature invalid at index {idx}")
            val = 0

        liste_valeurs.append(val)

print("\nAnalysis result:", liste_valeurs)
