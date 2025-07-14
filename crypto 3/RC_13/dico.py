import subprocess

chiffre = "U2FsdGVkX19D7MkxxA4TtGYH6nWAlLKqB2/zenTAfCDhjCKaqNhL575cZZJLxPfq\n"
objectif = "pubis porch brave dungy toped"
file = open("/home/lucie/crypto/Livres/words.txt","r")

def find_pass(chiffre,passphrase,file):
    lignes=file.readlines()
    for ligne in lignes:
        ligne=ligne.replace("\n","")
        #print(ligne)
        if decrypt(chiffre,ligne) == objectif:
            print("ok")
            print(ligne)
            result = ligne
            return result

def decrypt(plaintext, passphrase, cipher='aes-128-cbc'):
    pass_arg = 'pass:{}'.format(passphrase)
    args = ['openssl', 'enc','-d', '-' + cipher, '-base64', '-pass', pass_arg, '-pbkdf2']
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')
    result = subprocess.run(args, input=plaintext, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    error_message = result.stderr.decode()
    try :
        test = result.stdout.decode()
        return(test)
    except:
        return("")
    
result = find_pass(chiffre,objectif,file)
print(result)