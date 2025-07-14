import subprocess
import json

with open('/home/lucie/crypto/CISCU/EMV/transaction.json', 'r') as jsonfile:
    
    data_json = json.load(jsonfile)

# Initialisation des données 
taille = len(data_json["batch"]["transactions"])
list_finale = []
tmp = 1

# sort clé publique de la carte
def card_public_key(certif_path,pk_path):
    args = ['openssl', 'x509', '-pubkey', '-noout', '-in', certif_path, '-out', pk_path]
    res = subprocess.run(args,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("** La clé de la carte a été crée **\n")
    

# verif signature
def verif_sign(sign_path, pk_path, d_verif):
    args = ["openssl", "dgst", "-sha256", "-verify", pk_path, "-signature", sign_path]
    d = d_verif.encode('utf-8')
    res = subprocess.run(args, input=d, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if res.returncode == 0:
        print("La signature est valide.\n")
        return 1
    else:
        print("La signature n'est pas valide.")
        print(res.stderr.decode(),"\n")
        return 0
    

# verif certificat banque
def verif_certif_bank(bank_path,autorite_path):
    args = ["openssl", "verify", "-trusted", autorite_path, bank_path]
    res = subprocess.run(args,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if "OK" in res.stdout.decode():
        print("Le certificat est valide.\n")
        return 1
    else:
        print("Le certificat n'est pas valide.")
        print(res.stderr.decode(),"\n")
        return 0

def verif_certif_card(card_path,bank_path,autorite_path):
    args = ["openssl", "verify", "-trusted", autorite_path, "-untrusted", bank_path, card_path]
    res = subprocess.run(args,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if "OK" in res.stdout.decode():
        print("Le certificat est valide.\n")
        return 1
    else:
        print("Le certificat n'est pas valide.")
        print(res.stderr.decode(),"\n")
        return 0

for i in range(0,40):

    transaction = data_json["batch"]["transactions"][i]
    data = transaction["data"]

    card_number = transaction["card"]["number"]
    card_certif = transaction["card"]["certificate"]

    bank_name = transaction["card"]["bank"]["name"]
    bank_certif = transaction["card"]["bank"]["certificate"]

    signature = transaction["signature"]
    sign_bytes = bytes.fromhex(signature)

    ind_card = data.find("card-number")+15
    ind_bank = data.find("bank-name")+13
    data_bank = data[ind_bank:]

    # test nom banque
    print(data[ind_bank:ind_bank + data_bank.find("\",")])
    if not(bank_name == data[ind_bank:ind_bank + data_bank.find("\",")]):
        tmp = 0

    # test num carte
    print(data[ind_card:ind_card+19])
    if not(card_number==data[ind_card:ind_card+19]):
        tmp = 0

    bank_file = open("/home/lucie/crypto/CISCU/EMV/certif_banque.pem","w")
    bank_file.write(bank_certif)
    bank_file.close()

    card_file = open("/home/lucie/crypto/CISCU/EMV/certif_carte.pem","w")
    card_file.write(card_certif)
    card_file.close()

    f = open("/home/lucie/crypto/CISCU/EMV/signature.txt","wb")
    f.write(sign_bytes)
    f.close()


    card_public_key("/home/lucie/crypto/CISCU/EMV/certif_carte.pem","/home/lucie/crypto/CISCU/EMV/pk_carte.pem")

    v_sign = verif_sign("/home/lucie/crypto/CISCU/EMV/signature.txt","/home/lucie/crypto/CISCU/EMV/pk_carte.pem",data)
    if v_sign == 0:
        tmp = 0

    v_bank = verif_certif_bank("/home/lucie/crypto/CISCU/EMV/certif_banque.pem","/home/lucie/crypto/CISCU/EMV/certif_autorite.pem")
    if v_bank == 0:
        tmp = 0
    
    v_card = verif_certif_card("/home/lucie/crypto/CISCU/EMV/certif_carte.pem","/home/lucie/crypto/CISCU/EMV/certif_banque.pem","/home/lucie/crypto/CISCU/EMV/certif_autorite.pem")
    if v_card == 0:
        tmp = 0

    list_finale.append(tmp)
    tmp = 1


print(list_finale)