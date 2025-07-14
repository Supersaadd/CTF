import subprocess

# 🔹 Challenge chiffré donné
challenge_b64 = "U2FsdGVkX18236izA7fOnepeuck28jk1lyFqiubhQMxRURy62J/0TlG+zFFKrVAi"
REPONSE_ATTENDUE = "flabs homey hoots ville ileum"
FICHIER_DICTIONNAIRE = "words.txt"

def bruteforce_openssl():
    try:
        with open(FICHIER_DICTIONNAIRE, "r", encoding="utf-8") as f:
            mots_de_passe = f.read().splitlines()

        for mot in mots_de_passe:
            print(f"🔍 Test du mot de passe : {mot}")

            cmd = f'echo "{challenge_b64}" | openssl enc -d -aes-128-cbc -pbkdf2 -base64 -pass pass:"{mot}"'
            result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Debugging
            print(f"📤 OpenSSL stdout: {result.stdout}")
            print(f"⚠️ OpenSSL stderr: {result.stderr}")

            # Essayer utf-8 puis latin-1
            try:
                decrypted_text = result.stdout.decode("utf-8", errors="ignore").strip()
            except UnicodeDecodeError:
                decrypted_text = result.stdout.decode("latin-1").strip()

            if decrypted_text == REPONSE_ATTENDUE:
                print(f"🎯 Mot de passe trouvé : {mot}")
                return mot

        print("❌ Aucun mot de passe trouvé.")
    except FileNotFoundError:
        print("📂 Fichier dictionnaire introuvable.")

bruteforce_openssl()
