import subprocess
import base64

# ce script suppose qu'il a affaire à OpenSSL v1.1.1
# vérifier avec "openssl version" en cas de doute.
# attention à MacOS, qui fournit à la place LibreSSL.

# en cas de problème, cette exception est déclenchée
class OpensslError(Exception):
    pass

# Il vaut mieux être conscient de la différence entre str() et bytes()

def decryptmorepass(plaintext, passphrase, cipher='aes-128-cbc'):

        # Ouvrir le fichier en mode lecture
    with open(passphrase, 'r') as fichier:
    # Lire le contenu du fichier
        contenu = fichier.read()
    # Diviser le texte en lignes
    lignes = contenu.splitlines()

    # Boucle pour sélectionner chaque mot pour chaque ligne
    for ligne in lignes:
        
        
        ligne=ligne.strip()
        print(ligne)
            # prépare les arguments à envoyer à openssl
        pass_arg = 'pass:{}'.format(ligne)
        args = ['openssl', 'enc','-d','-A', '-' + cipher, '-base64', '-pass', pass_arg, '-pbkdf2']
            # print(args)
            # si plaintext est de stype str, on est obligé de l'encoder en bytes pour
            # pouvoir l'envoyer dans le pipeline vers openssl
            
        if isinstance(plaintext, str):
            plaintext = plaintext.encode('utf-8')
            # plaintext.hex()
            # plaintext = base64.b64decode(plaintext)
            
            # ouvre le pipeline vers openssl. envoie plaintext sur le stdin de openssl, récupère stdout et stderr
            #    affiche la commande invoquée
            #    print('debug : {0}'.format(' '.join(args)))
        result = subprocess.run(args, input=plaintext, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # print(result)
            # si un message d'erreur est présent sur stderr, on arrête tout
            # attention, sur stderr on récupère des bytes(), donc on convertit
            # error_message = result.stderr.decode()
            # if error_message != '':
            #     raise OpensslError(error_message)
        print(result.stderr.decode())
            # OK, openssl a envoyé le chiffré sur stdout, en base64.
            # On récupère des bytes, donc on en fait une chaine unicode
        # if ( result.stderr.decode() == '') :return base64.b64encode(result.stdout).decode()
        if ( result.stdout.decode('utf_8','ignore') == 'grime manna parka flaky femme') :return result.stdout.decode('utf_8','ignore')




# TODO :
# - implement the decrypt() method
# - write a KeyPair class
# - write a PublicKey class
# - etc.

# print(encrypt("ayins luaus belie harks oxbow","abdomen"))
# print(decryptmorepass(encrypt("ayins luaus belie harks oxbow\n","abdomen"),"words.txt"))
# print("U2FsdGVkX1+LluMHhQkmWD8K/gY6XBDqjczeHbUgEWCXgvGLCbwc3ejZ6SEmeVNq")
# print(base64.b64encode(base64.b64decode("U2FsdGVkX1+LluMHhQkmWD8K/gY6XBDqjczeHbUgEWCXgvGLCbwc3ejZ6SEmeVNq")).decode())
print(decryptmorepass("U2FsdGVkX1+ob3G2hk4ioOY0PHKV1gxfsFuFHyWRh1irZZh1B3n+3iyDmdrPTx3M","words.txt"))