import json
matriz = []
vector_sub_titulo = []
vector_servicios = []
vector_contacto = []
vector_horario = []
servicios = ""
def abrir_archivo(ARCHIVO):
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        datos = json.load(f)
    return datos

def procesar_sub_titulo(vector_sub_titulo):
    datos = abrir_archivo("data_negocio.json")
    for elemento in datos:
        if elemento == "nombre_empresa":
            vector_sub_titulo.append(datos[elemento])
        elif elemento == "descripcion":
            vector_sub_titulo.append(datos[elemento])

def procesar_servicios(vector_servicios):
    datos = abrir_archivo("data_negocio.json")
    for elemento in datos:
        if elemento == "servicios":
            for servicio in datos[elemento]:
                vector_servicios.append(servicio)

def procesar_contacto(vector_contacto):
    datos = abrir_archivo("data_negocio.json")
    for elemento in datos:  
        if elemento == "contacto":
            for key, value in datos[elemento].items():
                print(f"{key}: {value}")
                vector_contacto.append(value)

def procesar_horario(vector_horario):
    datos = abrir_archivo("data_negocio.json")
    for elemento in datos:
        if elemento == "horario_normal":
            vector_horario.append(datos[elemento])

def procesar_todo(vector1, vector2, vector3, vector4):
    matriz.append(vector1)
    matriz.append(vector2)
    matriz.append(vector3)
    matriz.append(vector4)
    print(matriz)

procesar_horario(vector_horario)
procesar_sub_titulo(vector_sub_titulo)
procesar_servicios(vector_servicios)
procesar_contacto(vector_contacto)
# print(f"vector_servicios= {vector_servicios}")
# print(f"vector_sub_titulo= {vector_sub_titulo}")
# print(f"vector_contacto= {vector_contacto}")
# print(f"vector_horario= {vector_horario}")
procesar_todo(vector_sub_titulo, vector_servicios, vector_contacto, vector_horario)
for servicio in vector_servicios:
    servicios = servicio + ", " + servicios
    texto_formateado = f"{vector_sub_titulo[0]} es una emepresa dedicada a {vector_sub_titulo[1]} que ofrece estos servicios: {servicios}. Para contactarse usar: {vector_contacto[0]} o {vector_contacto[1]}. nuestros horarios de atencion son: {vector_horario[0]}"