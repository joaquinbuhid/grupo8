import os
os.system("python grupo1.py")

import grupo5
charla_total = []
vector_charla = []
# user_input =""
# # Configuramos el título de la app
# st.set_page_config(page_title="Chat Demo", layout="centered")
# st.title("💬 Chat con Streamlit")

# # Campo de entrada de texto
# user_input = st.text_input("Escribí algo y presioná Enter", key="input")

# # Si hay algo escrito


import streamlit as st

# Simulación del sistema de respuestas (reemplazá por tu lógica real)
def responder_usuario(prompt):
    return f"Respuesta a: {prompt}"

st.set_page_config(page_title="Chatbot", layout="centered")
st.title("💬 Chatbot Inteligente")

# Inicializar historial si no existe
if "chat_historial" not in st.session_state:
    st.session_state.chat_historial = []

# Mostrar historial de chat (de arriba hacia abajo)
for remitente, mensaje in st.session_state.chat_historial:
    with st.chat_message(remitente.lower() if remitente == "Bot" else "user"):
        st.markdown(f"**{remitente}:** {mensaje}")


# Formulario de entrada de texto
with st.form(key="chat_form"):
    user_input = st.text_input("Escribí tu mensaje", value="")
    submit_button = st.form_submit_button(label="Enviar")

# Procesar entrada
if submit_button and user_input.strip() != "":

    if user_input:
        try:
            for charla in charla_total:
                st.write(f"Joaquin: {charla[0]}")
                st.write(f"Llama3: {charla[1]}")
        except Exception as e:
            print(f"Error; {e}")
        respuesta = grupo5.preguntar_con_contexto(user_input)
        st.write(respuesta)
        vector_charla = [user_input,respuesta]
        charla_total.append(vector_charla)

    # Guardar en el historial (cada entrada es una tupla: (usuario, bot))
    st.session_state.chat_historial.append(("Tú", user_input))
    st.session_state.chat_historial.append(("Bot", respuesta))
    st.session_state.user_input = ""

