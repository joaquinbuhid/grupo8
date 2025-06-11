import grupo4
import grupo3
import json
charla_total = []
charla_total = []

def preguntar_con_contexto(pregunta):
    with open("data_negocio.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
        prompt = grupo4.preguntar(datos)
        print("Generando respuesta...")
        respuesta = grupo3.conectar_con_ollama(prompt)
        print(respuesta, "\n")
        vector_charla = [pregunta,respuesta]
        charla_total.append(vector_charla)

# for charlas in charla_total:
#     with open("charlas.txt", "a") as ARCHIVO:
#         ARCHIVO.writelines(f"Tú: {charlas[0]} \n")
#         ARCHIVO.writelines(f"Llama3: {charlas[1]} \n")