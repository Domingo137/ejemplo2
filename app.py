import streamlit as st
import random

# Generar ecuación aleatoria de la forma ax + b = 0
def generar_ecuacion():
    a = random.randint(1, 10)
    b = random.randint(-10, 10)
    return a, b

# Resolver la ecuación
def resolver_ecuacion(a, b):
    return round(-b / a, 2)

# Título
st.title("🧮 Resuelve la ecuación de primer grado")

# Guardar en sesión para que no cambie con cada ejecución
if "a" not in st.session_state:
    st.session_state.a, st.session_state.b = generar_ecuacion()
    st.session_state.intentos = 0
    st.session_state.resuelto = False

a = st.session_state.a
b = st.session_state.b

# Mostrar la ecuación
st.latex(f"{a}x + ({b}) = 0")

# Campo de entrada
respuesta_usuario = st.text_input("Escribe el valor de x:", key="respuesta")

# Botón para verificar
if st.button("Verificar respuesta"):
    try:
        respuesta_usuario = float(respuesta_usuario)
        resultado_correcto = resolver_ecuacion(a, b)

        if round(respuesta_usuario, 2) == resultado_correcto:
            st.success("✅ ¡Correcto! 🎉")
            st.balloons()
            st.session_state.resuelto = True
        else:
            st.error(f"❌ Inc
