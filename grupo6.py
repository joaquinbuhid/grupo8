import streamlit as st
import grupo5

# Configuramos el título de la app
st.set_page_config(page_title="Chat Demo", layout="centered")
st.title("💬 Chat con Streamlit")

# Campo de entrada de texto
user_input = st.text_input("Escribí algo y presioná Enter", key="input")

# Si hay algo escrito
if user_input:
    st.write("🤖 Respondiendo...")
    grupo5.preguntar_con_contexto(user_input)