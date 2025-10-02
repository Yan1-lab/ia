import streamlit as st
import openai
import os

st.set_page_config(page_title="Asistente Médico KB", page_icon="💊", layout="centered")

st.title("💊 Asistente Médico Inteligente KB")
st.write("Estuve trabajando mucho en esto, espero te guste 🥰.")

# OpenAI API Key (usa variable de entorno)
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    st.warning("⚠️ Configura tu OpenAI API Key en las variables de entorno.")
    st.stop()

# Historial
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 Hola, soy tu asistente virtual Yan el Panda 🐼. ¿En qué te puedo ayudar?"}
    ]

# Mostrar historial
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# Input
if prompt := st.chat_input("Describe tus síntomas..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("💭 Revisando la base de datos médica..."):
            try:
                response = openai.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": 
                         "Eres un asistente médico virtual. Analiza síntomas y da posibles causas. Siempre aclara que no reemplazas a un médico real."},
                        *st.session_state.messages
                    ],
                    max_tokens=400,
                    temperature=0.5
                )
                reply = response.choices[0].message.content
            except Exception as e:
                reply = f"⚠️ Error al conectar con OpenAI: {e}"

        st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})



