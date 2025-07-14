import subprocess
import base64

# ce script suppose qu'il a affaire à OpenSSL v1.1.1
# vérifier avec "openssl version" en cas de doute.
# attention à MacOS, qui fournit à la place LibreSSL.

# en cas de problème, cette exception est déclenchée
class OpensslError(Exception):
    pass

# Il vaut mieux être conscient de la différence entre str() et bytes()

def encrypt(plaintext, passphrase, cipher='aes-128-cbc'):
    """invoke the OpenSSL library (though the openssl executable which must be
       present on your system) to encrypt content using a symmetric cipher.

       The passphrase is an str object (a unicode string)
       The plaintext is str() or bytes()
       The output is bytes()

       # encryption use
       >>> message = "texte avec caractères accentués"
       >>> c = encrypt(message, 'foobar')       
    """
    # prépare les arguments à envoyer à openssl
    pass_arg = 'pass:{}'.format(passphrase)
    args = ['openssl', 'enc', '-' + cipher, '-base64', '-pass', pass_arg, '-pbkdf2']
    
    # si plaintext est de stype str, on est obligé de l'encoder en bytes pour
    # pouvoir l'envoyer dans le pipeline vers openssl
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')
    
    # ouvre le pipeline vers openssl. envoie plaintext sur le stdin de openssl, récupère stdout et stderr
    #    affiche la commande invoquée
    #    print('debug : {0}'.format(' '.join(args)))
    result = subprocess.run(args, input=plaintext, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # si un message d'erreur est présent sur stderr, on arrête tout
    # attention, sur stderr on récupère des bytes(), donc on convertit
    error_message = result.stderr.decode()
    if error_message != '':
        raise OpensslError(error_message)

    # OK, openssl a envoyé le chiffré sur stdout, en base64.
    # On récupère des bytes, donc on en fait une chaine unicode
    return result.stdout.decode()

def decrypt(plaintext, passphrase, cipher='aes-128-cbc'):

        # Ouvrir le fichier en mode lecture
    
        # print(ligne)
        # prépare les arguments à envoyer à openssl
        pass_arg = 'pass:{}'.format(passphrase)
        args = ['openssl', 'enc','-d','-A', '-' + cipher, '-base64', '-pass', pass_arg, '-pbkdf2']
        
        # si plaintext est de stype str, on est obligé de l'encoder en bytes pour
        # pouvoir l'envoyer dans le pipeline vers openssl
        if isinstance(plaintext, str):
            plaintext = plaintext.encode('utf-8')
        
        # ouvre le pipeline vers openssl. envoie plaintext sur le stdin de openssl, récupère stdout et stderr
        #    affiche la commande invoquée
        #    print('debug : {0}'.format(' '.join(args)))
        result = subprocess.run(args, input=plaintext, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # si un message d'erreur est présent sur stderr, on arrête tout
        # attention, sur stderr on récupère des bytes(), donc on convertit
        # error_message = result.stderr.decode()
        # if error_message != '':
        #     raise OpensslError(error_message)

        # OK, openssl a envoyé le chiffré sur stdout, en base64.
        # On récupère des bytes, donc on en fait une chaine unicode
        return result.stdout.decode()

def encryptclepub(plaintext, clepub, cipher='aes-128-cbc'):
    """invoke the OpenSSL library (though the openssl executable which must be
       present on your system) to encrypt content using a symmetric cipher.

       The passphrase is an str object (a unicode string)
       The plaintext is str() or bytes()
       The output is bytes()

       # encryption use
       >>> message = "texte avec caractères accentués"
       >>> c = encrypt(message, 'foobar')       
    """
    # prépare les arguments à envoyer à openssl
    args = ['openssl', 'pkeyutl', '-encrypt', '-pubin', '-inkey', clepub]
    
    # si plaintext est de stype str, on est obligé de l'encoder en bytes pour
    # pouvoir l'envoyer dans le pipeline vers openssl
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')
        # plaintext = base64.b64encode(plaintext)

    
    # ouvre le pipeline vers openssl. envoie plaintext sur le stdin de openssl, récupère stdout et stderr
    #    affiche la commande invoquée
    #    print('debug : {0}'.format(' '.join(args)))
    result = subprocess.run(args, input=plaintext, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # si un message d'erreur est présent sur stderr, on arrête tout
    # attention, sur stderr on récupère des bytes(), donc on convertit
    error_message = result.stderr.decode()
    if error_message != '':
        raise OpensslError(error_message)

    # OK, openssl a envoyé le chiffré sur stdout, en base64.
    # On récupère des bytes, donc on en fait une chaine unicode
    return result.stdout.hex()

# openssl dgst -sha256 -sign private_key.pem -out signature.txt -keyform PEM txt.txt
def sign(sortie, secret_key, text_signature, cipher='aes-128-cbc'):
    
    # prépare les arguments à envoyer à openssl
    args = ['openssl', 'dgst', '-sha256', '-sign', secret_key, '-out', text_signature]
    
    # si plaintext est de stype str, on est obligé de l'encoder en bytes pour
    # pouvoir l'envoyer dans le pipeline vers openssl
    if isinstance(sortie, str):
        sortie = sortie.encode('utf-8')
        # plaintext = base64.b64encode(plaintext)

    
    # ouvre le pipeline vers openssl. envoie plaintext sur le stdin de openssl, récupère stdout et stderr
    #    affiche la commande invoquée
    #    print('debug : {0}'.format(' '.join(args)))
    result = subprocess.run(args, input=sortie, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # si un message d'erreur est présent sur stderr, on arrête tout
    # attention, sur stderr on récupère des bytes(), donc on convertit
    error_message = result.stderr.decode()
    if error_message != '':
        raise OpensslError(error_message)

    # ici il suffit d'executer le resultat sans le -out text_signature pour avoir le resultat affichable en .hex
    return result.stdout.hex()

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

    
    # ouvre le pipeline vers openssl. envoie plaintext sur le stdin de openssl, récupère stdout et stderr
    #    affiche la commande invoquée
    #    print('debug : {0}'.format(' '.join(args)))
    result = subprocess.run(args, input=mot, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # si un message d'erreur est présent sur stderr, on arrête tout
    # attention, sur stderr on récupère des bytes(), donc on convertit
    error_message = result.stderr.decode()
    if error_message != '':
        raise OpensslError(error_message)

    
    return result.stdout.decode()


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
        if ( result.stdout.decode('utf_8','ignore') == 'ayins luaus belie harks oxbow') :return result.stdout.decode('utf_8','ignore')




# TODO :
# - implement the decrypt() method
# - write a KeyPair class
# - write a PublicKey class
# - etc.

# print(encrypt("ayins luaus belie harks oxbow","abdomen"))
# print(decryptmorepass(encrypt("ayins luaus belie harks oxbow\n","abdomen"),"words.txt"))
# print("U2FsdGVkX1+LluMHhQkmWD8K/gY6XBDqjczeHbUgEWCXgvGLCbwc3ejZ6SEmeVNq")
# print(base64.b64encode(base64.b64decode("U2FsdGVkX1+LluMHhQkmWD8K/gY6XBDqjczeHbUgEWCXgvGLCbwc3ejZ6SEmeVNq")).decode())
# print(decryptmorepass("U2FsdGVkX1+LluMHhQkmWD8K/gY6XBDqjczeHbUgEWCXgvGLCbwc3ejZ6SEmeVNq","words.txt"))
# res = sign("bonjour","private_key.pem","signature.txt")
# print (res)
# print(verifysign("signature.txt","public_key.pem","bonjour"))
# print("I, the lab director, hereby grant quentin.de_magalhaes permission to take the BiblioDrone-NG.".encode('utf-8').hex())
# res = bytes.fromhex("627b315b69e7b3bceaa0442397c5ac3285a794f6229a0bacd8da1bc9dbf879622ff3942f7fa58890fd239e7d4d51ba9fb82438387512c6fd8a016c3c9d3bfc634ffcfecc52933b1fa38b1761a8ab93ffb97116f4aa0ce069f648d9acdff6b5507061d7c88a5779553593df0c623e6daccf7acc07f7c39c3e56f5a9da1269c4792b41662e55a681ddc07bc65b796ecb968587be609afae7aaee4f715eaf5040f9f5841543c53af9999dcbdac399d8c7fdd3c9301ffb6563b727d655f94c46ab7617d3a0fb59d79dea0acc11b1e7e5484fc573bceeeeef8aa94198d36addfc0c3ad751119e3e81eb5acc521ba884a6fd16bc0ee27a02cd2ebb75f12c092dce58a1")
# with open('txt.txt', 'wb') as fichier:
#     fichier.write(res)
# print(base64.b64encode('8c4c89f9f3389b9ea0190390db0d834b9d84f84fc3ba559a523a28f1fbe01f264b5c904330ad496d8fc3f18d591d7a10d1eac14bc62720f5baf0ac126ed99d5cad96b6a43557bb3ffd56a4f34fb66046370ddb3f0b0eef77d3c2b5e62312c3ea036bf6890d455ce681208acfb9a4e1cc2837683fa1e2dd952383fca74bc36c1e92eedb296432224c03cf1be9f4e2430fba369017cafd530ba8194473987441e9b69674fa1024e824d19ad6f694eaf63e611963910f8a87717a1138bb8d9a8add25aba62edf54a9d83e3b68cab2bfbfc294c0341ccdfd367780387ef0d8f573afbafcbfc49c028c48411f3b13b5a10aef316dc188124b9a8fe774764f3db20a41'.encode('utf-8')).decode())
print(decrypt("U2FsdGVkX1/1hVFFUWnLWFnwfS+84f0equrHt0tslzMgK2F0CnieZyclKIGdyCa1","6ARkNJu7&F"))

