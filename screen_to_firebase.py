import time
import os
from PIL import ImageGrab
import requests

# URL d'upload vers Firebase Storage
FIREBASE_UPLOAD_URL = "https://firebasestorage.googleapis.com/v0/b/bot-crypto-472ab.firebasestorage.app/o?uploadType=media&name=last_screenshot.jpg"

def upload_screenshot():
    filename = "last_screenshot.jpg"

    # Prendre une capture d'écran
    screenshot = ImageGrab.grab()
    screenshot.save(filename, "JPEG")

    # Envoyer l'image vers Firebase
    with open(filename, "rb") as f:
        response = requests.post(FIREBASE_UPLOAD_URL, headers={"Content-Type": "image/jpeg"}, data=f)

    if response.status_code == 200:
        print("Capture envoyée : https://firebasestorage.googleapis.com/v0/b/bot-crypto-472ab.firebasestorage.app/o/last_screenshot.jpg?alt=media")
    else:
        print("Erreur d'upload :", response.text)

    # Supprimer le fichier local
    os.remove(filename)

if __name__ == "__main__":
    print("Démarrage des captures d'écran (CTRL + C pour arrêter)...")
    while True:
        upload_screenshot()
        time.sleep(1)

