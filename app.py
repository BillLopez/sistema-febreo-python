import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sistema Febreo - Bill Lopez", page_icon="🚀", layout="wide")

with st.sidebar:
    st.markdown("## Menú de Navegación")
    seccion = st.selectbox(
        "Ir a:",
        ["🏠 Home", "📉 Ejercicio 1", "📦 Ejercicio 2", "🧪 Ejercicio 3", "🛠️ Ejercicio 4"]
    )
    st.info(f"Usuario: Bill G. Lopez Milla\nEgresado Ing. de Sistemas")

# --- SECCIÓN HOME ---
if seccion == "🏠 Home":
    st.title("PySistemas Analytics: Plataforma de Gestión Inteligente Febreo")
    st.markdown("---")
    
    col_img, col_info = st.columns([1, 2])
    
    with col_img:
        st.image("https://cdn-icons-png.flaticon.com/512/5968/5968350.png", width=150)
        st.caption("Fusión Python-Lopez Milla v1.0")

    with col_info:
        st.subheader("Información del Estudiante")
        st.write(f"**Nombre:** Bill Giner Lopez Milla")
        st.write(f"**Especialidad:** Egresado Ingeniería de Sistemas - USMP")
        st.write(f"**Sede:** Lima, Perú")
        st.write(f"**Módulo:** Python Fundamentals & Data Structures")
        st.write(f"**Año:** 2026")

    st.markdown("---")
    st.markdown("### 📝 Breve descripción del proyecto")
    st.write("""
    Este proyecto es una solución integral que demuestra el dominio de los fundamentos de Python 
    aplicados a la analítica de datos. A través de cuatro módulos prácticos, la aplicación permite 
    gestionar flujos de caja, administrar inventarios con NumPy y ejecutar procesos CRUD avanzados 
    utilizando Programación Orientada a Objetos (POO).
    """)

    st.markdown("### 🛠️ Tecnologías utilizadas")
    st.code("Streamlit | Python | NumPy | Pandas | Openpyxl | Plotly", language="text")

# --- LOS DEMÁS EJERCICIOS (Se irán llenando) ---
elif seccion == "📉 Ejercicio 1":
    st.header("Ejercicio 1 - Flujo de Caja")
    st.write("Configurando listas dinámicas...")

# Repetir para Ejercicio 2, 3 y 4 con st.write("En construcción")