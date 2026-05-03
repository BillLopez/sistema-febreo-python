import streamlit as st
import pandas as pd

# Configuraci車n de p芍gina con identidad profesional
st.set_page_config(
    page_title="Sistema Febreo - Anal赤tica", 
    page_icon="??", 
    layout="wide"
)

# --- NAVEGACI車N LATERAL ---
with st.sidebar:
    st.title("Panel de Control")
    # Navegaci車n basada en los requisitos de la gu赤a
    seccion = st.selectbox(
        "Navegaci車n Principal",
        ["Inicio", "Flujo de Caja", "Inventario NumPy", "Librer赤a Funciones", "Gesti車n POO"]
    )
    st.divider()
    st.caption("Consultor: Bill Giner Lopez Milla")
    st.caption("Egresado Ingenier赤a de Sistemas - USMP")
    st.caption("Ciclo Acad谷mico 2026")

# --- SECCI車N 1: INICIO (HOME) ---
if seccion == "Inicio":
    st.title("PySistemas Analytics: Plataforma de Gesti車n Febreo")
    st.divider()
    
    col_img, col_info = st.columns([1, 2])
    
    with col_img:
        # Aseg迆rate de subir 'logo_lopez.png' a tu GitHub[cite: 3]
        # Si a迆n no lo subes, puedes comentar la l赤nea de abajo
        st.image("logo_lopez.png", use_container_width=True)

    with col_info:
        st.subheader("Ficha T谷cnica del Proyecto")
        st.write(f"**Estudiante:** Bill Giner Lopez Milla")
        st.write(f"**Especialidad:** Ingenier赤a de Sistemas")
        st.write(f"**Instituci車n:** Universidad de San Mart赤n de Porres (Lima)")
        st.write(f"**M車dulo:** Python Fundamentals & Analytics")
        st.write(f"**Tecnolog赤as:** Streamlit, Pandas, NumPy, Plotly")

    st.divider()
    
    with st.container():
        st.markdown("#### Descripci車n de la Arquitectura")
        st.write("""
        Esta plataforma representa la implementaci車n de soluciones digitales orientadas a la 
        optimizaci車n de procesos. A trav谷s de este sistema, se integran estructuras de datos 
        avanzadas, gesti車n de archivos y programaci車n orientada a objetos para resolver 
        desaf赤os operativos en entornos de ingenier赤a.
        """)

# --- SECCI車N 2: EJERCICIO 1 (FLUJO DE CAJA) ---
elif seccion == "Flujo de Caja":
    st.title("Gesti車n de Flujo de Caja")
    st.write("M車dulo dise?ado para el monitoreo de liquidez mediante estructuras de listas din芍micas.")

    # Inicializaci車n de memoria de sesi車n para la lista[cite: 3, 6]
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    # Interfaz de captura de datos con dise?o de tarjeta (card)
    with st.container(border=True):
        st.write("##### Registro de Movimiento")
        col_c, col_t, col_m = st.columns([2, 1, 1])
        
        with col_c:
            concepto = st.text_input("Concepto Operativo", placeholder="Descripci車n de la transacci車n")
        with col_t:
            tipo = st.selectbox("Categor赤a", ["Ingreso", "Gasto"])
        with col_m:
            valor = st.number_input("Monto en Divisa", min_value=0.0, step=1.0)

        if st.button("Procesar Transacci車n", use_container_width=True):
            if concepto and valor > 0:
                # Almacenamiento en lista seg迆n requerimiento[cite: 3]
                st.session_state.movimientos.append({
                    "Concepto": concepto, 
                    "Tipo": tipo, 
                    "Monto": valor
                })
                st.toast("Transacci車n registrada exitosamente")
            else:
                st.warning("Verifique que el concepto y el monto sean v芍lidos")

    # Visualizaci車n de resultados si existen datos
    if st.session_state.movimientos:
        st.divider()
        df_movs = pd.DataFrame(st.session_state.movimientos)
        
        col_list, col_metrics = st.columns([2, 1])
        
        with col_list:
            st.write("##### Historial Consolidado")
            st.dataframe(df_movs, use_container_width=True, hide_index=True)

        with col_metrics:
            st.write("##### Balance de Situaci車n")
            t_ingresos = sum(m["Monto"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso")
            t_gastos = sum(m["Monto"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto")
            saldo_final = t_ingresos - t_gastos

            # M谷tricas profesionales[cite: 3]
            st.metric("Ingresos Totales", f"{t_ingresos:,.2f}")
            st.metric("Gastos Totales", f"{t_gastos:,.2f}", delta=f"-{t_gastos:,.2f}", delta_color="inverse")
            st.metric("Balance Neto", f"{saldo_final:,.2f}")

            if saldo_final > 0:
                st.success("Estado de Cuenta: Super芍vit")
            elif saldo_final < 0:
                st.error("Estado de Cuenta: D谷ficit")
            else:
                st.info("Estado de Cuenta: Equilibrio")
            
        if st.button("Reiniciar Registros"):
            st.session_state.movimientos = []
            st.rerun()
    else:
        st.info("No se han detectado transacciones registradas en el sistema")

# Los dem芍s ejercicios se a?adir芍n a continuaci車n...