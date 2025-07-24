import os
import subprocess
import textwrap
import time

def run_cmd(cmd):
    print(f"\n>>> {cmd}")
    result = subprocess.run(cmd, shell=True, text=True)
    if result.returncode != 0:
        print("⚠️  Échec ou commande avec erreur.")

def install_requirements():
    print("📦 Installation des dépendances Python...")
    run_cmd("py -m pip install --upgrade pip")
    run_cmd("py -m pip install python-dotenv python-binance")

def setup_git():
    print("🔧 Configuration de Git...")
    run_cmd('git config --global user.name "francoismanka"')
    run_cmd('git config --global user.email "francoism4340@gmail.com"')

def create_gitignore():
    print("📁 Création de .gitignore...")
    with open(".gitignore", "w") as f:
        f.write("*.json\n.env\n*.key\n*.pem\n")
    print("✅ .gitignore créé.")

def create_env():
    if not os.path.exists(".env"):
        print("📄 Création du fichier .env...")
        with open(".env", "w") as f:
            f.write("BINANCE_API_KEY=\nBINANCE_API_SECRET=\nFIREBASE_KEY_PATH=bot-crypto-472ab-firebase-adminsdk-fbsvc-237ce20cb0.json\n")
        print("✅ Fichier .env créé. Remplis-le avec tes clés.")
    else:
        print("✅ .env déjà existant.")

def create_test_script():
    print("📄 Création de test_binance.py...")
    script = textwrap.dedent("""\
        from dotenv import load_dotenv
        import os
        from binance.client import Client

        load_dotenv()
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        client = Client(api_key, api_secret)

        try:
            account = client.get_account()
            print("Connexion réussie ! Solde disponible :")
            for balance in account['balances']:
                if float(balance['free']) > 0:
                    print(balance)
        except Exception as e:
            print("Erreur de connexion :", e)
    """)
    with open("test_binance.py", "w", encoding="utf-8") as f:
        f.write(script)
    print("✅ test_binance.py créé.")

def git_push():
    print("⬆️  Ajout et push des fichiers Git...")
    run_cmd("git add .")
    run_cmd('git commit -m "Mise à jour par assistant automatique"')
    run_cmd("git push")

def test_binance():
    print("🧪 Test de connexion Binance...")
    run_cmd("py test_binance.py")

def menu():
    while True:
        print("\n=== ASSISTANT GPT AVANCÉ ===")
        print("1. Installer les dépendances")
        print("2. Configurer Git")
        print("3. Créer .gitignore")
        print("4. Créer .env")
        print("5. Créer test_binance.py")
        print("6. Lancer test Binance")
        print("7. Git add/commit/push")
        print("0. Quitter")
        choix = input("\n➡ Choisis une option : ")
        if choix == "1":
            install_requirements()
        elif choix == "2":
            setup_git()
        elif choix == "3":
            create_gitignore()
        elif choix == "4":
            create_env()
        elif choix == "5":
            create_test_script()
        elif choix == "6":
            test_binance()
        elif choix == "7":
            git_push()
        elif choix == "0":
            print("👋 Fin de l'assistant.")
            break
        else:
            print("❌ Option invalide. Réessaye.")

if __name__ == "__main__":
    menu()
