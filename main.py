import requests
from bs4 import BeautifulSoup

# URL der Website, die gecrawlt werden soll
url = input("gib die Seite ein, die du crawlen willst ")

# HTTP-Anfrage an die Website senden
response = requests.get(url)

# Überprüfen, ob die Anfrage erfolgreich war
if response.status_code == 200:
    # HTML-Inhalt der Seite analysieren
    soup = BeautifulSoup(response.text, "html.parser")

    # Beispiel: Titel der Seite extrahieren und anzeigen
    page_title = soup.title.text
    print("Seitentitel:", page_title)

    # Beispiel: Alle Links auf der Seite extrahieren und anzeigen
    links = soup.find_all("a")
    print("Gefundene Links:")
    for link in links:
        print(link.get("href"))

    # Beispiel: Alle Bilder auf der Seite extrahieren und anzeigen
    images = soup.find_all("img")
    print("Gefundene Bilder:")
    for img in images:
        print(img.get("src"))
else:
    print("Fehler beim Abrufen der Seite")
