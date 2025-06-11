import requests

def conectar_con_ollama(prompt, modelo="llama3"):
    url = "http://localhost:11434/api/chat"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "model": modelo,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False  # True si querés recibir el texto en streaming
    }

    try:
        respuesta = requests.post(url, headers=headers, json=payload)
        respuesta.raise_for_status()
        contenido = respuesta.json()
        return contenido["message"]["content"]
    except Exception as e:
        return f"Error al conectar con Ollama: {e}"

# while True:
#     usuario = input("Hazme una pregunta: ")
#     prompt = usuario
#     if usuario.upper() == "EXIT":
#         break
#     print("Generando respuesta...\n")
#     respuesta = conectar_con_ollama(prompt)
#     print(respuesta, "\n")