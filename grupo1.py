import requests
from bs4 import BeautifulSoup
import json
import re

datos = {}

def extraer_titulo(URL = "https://rotariaweb.net/ucasal/"):
    # Título
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    for h1 in soup.find_all("h1"):
        texto = h1.get_text(strip=True)
        if texto:
            datos["nombre_empresa"] = texto
            break

def extraer_subtitulo(URL = "https://rotariaweb.net/ucasal/"):
    # Subtitulo
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    for p in soup.find_all("p",id="subtitulo"):
        texto = p.get_text(strip=True)
        if texto:
            datos["descripcion"] = texto
            break

def extraer_horario(URL = "https://rotariaweb.net/ucasal/"):
    # Subtitulo
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    for p in soup.find_all("p",id="horario_normal"):
        texto = p.get_text(strip=True)
        if texto:
            datos["horario_normal"] = texto
            break

def extraer_servicios(URL = "https://rotariaweb.net/ucasal/"):
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    # Servicios listados
    servicios = []
    for h3 in soup.find_all("h3"):
        texto = h3.get_text(strip=True)
        if texto and texto.lower()!="horarios de atencion":
            servicios.append(texto)
    datos["servicios"] = servicios

def extraer_contacto(URL = "https://rotariaweb.net/ucasal/"):
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    # Contacto
    contacto = {}

    for a in soup.find_all("a", href=True):
        href = a["href"]

        # WhatsApp (extraer número)
        if "wa.me" in href:
            match = re.search(r'wa\.me/(\d+)', href)
            if match:
                contacto["whatsapp o numero de telefono"] = match.group(1)

        # Instagram
        if "instagram.com" in href:
            contacto["instagram o ig"] = href

    datos["contacto"] = contacto

def guardar_datos(OUTPUT_FILE = "data_negocio.json"):
    # Guardar como JSON
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)

    print(f"Datos extraídos y guardados en {OUTPUT_FILE}")

try:
    extraer_titulo()
    extraer_subtitulo()
    extraer_servicios()
    extraer_contacto()
    extraer_horario()
    guardar_datos()
except Exception as e:
    print(e)