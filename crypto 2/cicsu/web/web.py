import json
import subprocess

# en cas de problème, cette exception est déclenchée
class OpensslError(Exception):
    pass

def extract_public_key(cert_path):
    
    args = ['openssl', 'x509', '-pubkey', '-noout', '-in', cert_path]
    result = subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return result.stdout.decode()
# attention on retourne un \n a la fin

# openssl dgst -sha256 -verify public_key.pem -signature signature.txt -keyform PEM -binary txt.txt
def verifysign(signature, pubkey_key, mot, cipher='aes-128-cbc'):

    with open(pubkey_key, 'r') as fichier:
    # Lire le contenu du fichier
        contenu = fichier.read()
    
    # prépare les arguments à envoyer à openssl
    args = ['openssl', 'dgst', '-sha256', '-verify', pubkey_key, '-signature', signature]
    
    # si plaintext est de stype str, on est obligé de l'encoder en bytes pour
    # pouvoir l'envoyer dans le pipeline vers openssl
    if isinstance(mot, str):
        mot = mot.encode('utf-8')
        # plaintext = base64.b64encode(plaintext)
    result = subprocess.run(args, input=mot, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # si un message d'erreur est présent sur stderr, on arrête tout
    # attention, sur stderr on récupère des bytes(), donc on convertit
    if result.returncode == 0:
        return 0
    else:
        return 1

def verif_banque(uglix,cert_path):
    
    args = ['openssl', 'verify', '-trusted',uglix, cert_path]
    result = subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if (result.stderr == b'') :
        return 0
    else :
        return 1

def verif_carte(uglix,cert_b_path,cert_c_path):
    
    args = ['openssl', 'verify', '-trusted',uglix,'-untrusted', cert_b_path,cert_c_path ]
    result = subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if (result.stderr == b'') :
        return 0
    else :
        return 1

liste_valeurs = []
# Ouvrir et lire le fichier JSON
with open('donnees.json', 'r') as file:
    donnee = json.load(file)
    for i in range(0,40):
        val = 1
        transaction = donnee['batch']['transactions'][i]
        data = transaction['data']
        print(data)
        data_json = json.loads(data)
        data_card = data_json['card-number']
        data_bname = data_json['bank-name']
        card = transaction['card']
        card_number = card['number']
        bank = card['bank']
        bank_name = bank['name']
        if(data_card != card_number) :
            print('pas le bon numero de carte')
            print(data_card)
            print(card_number)
            val = 0
        else :
            print ("bon numéro de carte")

        if(data_bname != bank_name) :
            print('pas le bon nom de banque')
            print(data_bname)
            print(bank_name)
            val = 0
        else :
            print ("bon nom de banque")

        with open('certif_c.pem', "w") as file:
            file.write(card['certificate'])
        with open('certif_b.pem', "w") as file:
            file.write(bank['certificate'])
        with open('pubkey_c.pem', "w") as file:
            file.write(extract_public_key('certif_c.pem'))
        with open('signature.txt', "wb") as file:
            file.write(bytes.fromhex(transaction['signature']))
        if(verif_banque('UGLIX.pem','certif_b.pem')!=0) :
            val = 0
        if(verif_carte('UGLIX.pem','certif_b.pem','certif_c.pem')!=0) :
            val = 0
        if(verifysign('signature.txt','pubkey_c.pem',data)!=0) :
            val = 0
        
        liste_valeurs.append(val)


print(liste_valeurs)

