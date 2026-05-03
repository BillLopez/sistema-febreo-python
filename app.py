import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Sistema Febreo - Analítica", 
    page_icon="📊", 
    layout="wide"
)

with st.sidebar:
    st.title("Panel de Control")
    seccion = st.selectbox(
        "Navegación Principal",
        ["Inicio", "Flujo de Caja", "Inventario NumPy", "Librería Funciones", "Gestión POO"]
    )
    st.divider()
    st.caption("Consultor: Bill Giner Lopez Milla")
    st.caption("Egresado Ingeniería de Sistemas - USMP")
    st.caption("Ciclo Académico 2026")

# HOME
if seccion == "Inicio":
    st.title("PySistemas Analytics: Plataforma de Gestión Febreo")
    st.divider()
    
    col_img, col_info = st.columns([1, 2])
    
    with col_img:
        st.image("logo_lopez.png", use_container_width=True)

    with col_info:
        st.subheader("Ficha Técnica del Proyecto")
        st.write(f"**Estudiante:** Bill Giner Lopez Milla")
        st.write(f"**Especialidad:** Ingeniería de Sistemas")
        st.write(f"**Institución:** Universidad Nacional de Ingeniería (Lima)")
        st.write(f"**Módulo:** Python Fundamentals & Analytics")
        st.write(f"**Tecnologías:** Streamlit, Pandas, NumPy, Plotly")

    st.divider()
    
    with st.container():
        st.markdown("#### Descripción de la Arquitectura")
        st.write("""
        Esta plataforma representa la implementación de soluciones digitales orientadas a la 
        optimización de procesos. A través de este sistema, se integran estructuras de datos 
        avanzadas, gestión de archivos y programación orientada a objetos para resolver 
        desafíos operativos en entornos de ingeniería.
        """)

# EJERCICIO 1:
elif seccion == "Flujo de Caja":
    st.title("Gestión de Flujo de Caja")
    st.write("Módulo diseñado para el monitoreo de liquidez mediante estructuras de listas dinámicas.")

    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    with st.container(border=True):
        st.write("##### Registro de Movimiento")
        col_c, col_t, col_m = st.columns([2, 1, 1])
        
        with col_c:
            concepto = st.text_input("Concepto Operativo", placeholder="Descripción de la transacción")
        with col_t:
            tipo = st.selectbox("Categoría", ["Ingreso", "Gasto"])
        with col_m:
            valor = st.number_input("Monto en Divisa", min_value=0.0, step=1.0)

        if st.button("Procesar Transacción", use_container_width=True):
            if concepto and valor > 0:
                st.session_state.movimientos.append({
                    "Concepto": concepto, 
                    "Tipo": tipo, 
                    "Monto": valor
                })
                st.toast("Transacción registrada exitosamente")
            else:
                st.warning("Verifique que el concepto y el monto sean válidos")

    if st.session_state.movimientos:
        st.divider()
        df_movs = pd.DataFrame(st.session_state.movimientos)
        
        col_list, col_metrics = st.columns([2, 1])
        
        with col_list:
            st.write("##### Historial Consolidado")
            st.dataframe(df_movs, use_container_width=True, hide_index=True)

        with col_metrics:
            st.write("##### Balance de Situación")
            t_ingresos = sum(m["Monto"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso")
            t_gastos = sum(m["Monto"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto")
            saldo_final = t_ingresos - t_gastos

            # Métricas profesionales[cite: 3]
            st.metric("Ingresos Totales", f"{t_ingresos:,.2f}")
            st.metric("Gastos Totales", f"{t_gastos:,.2f}", delta=f"-{t_gastos:,.2f}", delta_color="inverse")
            st.metric("Balance Neto", f"{saldo_final:,.2f}")

            if saldo_final > 0:
                st.success("Estado de Cuenta: Superávit")
            elif saldo_final < 0:
                st.error("Estado de Cuenta: Déficit")
            else:
                st.info("Estado de Cuenta: Equilibrio")
            
        if st.button("Reiniciar Registros"):
            st.session_state.movimientos = []
            st.rerun()
    else:
        st.info("No se han detectado transacciones registradas en el sistema")

# Los demás ejercicios se añadirán a continuación...