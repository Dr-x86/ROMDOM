import crawler
import random
import requests

urls = {
    "Playstation 2":["https://archive.org/details/ps2_bob_collection","https://archive.org/details/PS2CollectionPart1ByGhostware","https://archive.org/details/PS2CollectionPart2ByGhostware","https://github.com/Dr-x86/Video-Game-Web-Crawler"],
    "GBA - GB":["https://archive.org/details/2-games-in-1-sonic-advance-sonic-battle-europe-en-ja-fr-de-es-en-ja-fr-de-es-it","https://archive.org/details/unrenamed-consoles-gba"],
    "Nintendo 3DS":["https://archive.org/details/3ds-cia-eshop","https://archive.org/details/wonderswan-cias-3ds"]
}

consolas = ["Playstation 2", "GBA - GB", "Nintendo 3DS"]

# eleccion = random.choice( consolas ) 
eleccion = "GBA - GB"


enlaces_repo = crawler.busquedaRecursiva(urls[eleccion])


lista = list()
for enlace in enlaces_repo:
    lista.append(crawler.enlaceDescarga(enlace,"-"))
    
    


subLista = random.choice(lista)
juego = random.choice(subLista)

extension = juego.split(".")
extension = extension[len(extension)-1]

print(extension)

descarga = requests.get(juego)



with open(f"Juego.{extension}", "wb") as f:
    f.write(descarga.content)


print("Descargado")

from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.getenv("TOKEN")

def enviarJuego():
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    
    data = {
        "chat_id":"6814112276",
        "caption":"Juego aleatorio del dia"
    }
    files = {
        "document": open(f"Juego.{extension}","rb")
    }
        
    try:
        res = requests.post(url,data=data, files=files)
        if res.status_code == 200:
            print(res.json())
    
    except Exception as e:
        print(f"Excepcion: {e}")

enviarJuego()