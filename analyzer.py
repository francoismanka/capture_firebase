import time
import requests
from PIL import Image
from io import BytesIO
import pytesseract

IMAGE_URL = "https://firebasestorage.googleapis.com/v0/b/bot-crypto-472ab.firebasestorage.app/o/last_screenshot.jpg?alt=media"

def analyze_image():
    try:
        response = requests.get(IMAGE_URL)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            text = pytesseract.image_to_string(image, lang="eng+fra")
            print("=== TEXTE DETECTÉ SUR L'ÉCRAN ===")
            print(text)
            print("==============================")
        else:
            print("Erreur téléchargement:", response.status_code)
    except Exception as e:
        print("Erreur d'analyse:", e)

if __name__ == "__main__":
    print("Démarrage de l'analyse en direct (CTRL + C pour arrêter)...")
    while True:
        analyze_image()
        time.sleep(1)
