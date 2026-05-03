import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Sistema Febreo - Bill Lopez", 
    page_icon="??", 
    layout="wide"
)

if "movimientos" not in st.session_state:
    st.session_state.movimientos = []

with st.sidebar:
    st.title("Panel de Control")
    seccion = st.selectbox(
        "Navegaci車n Principal",
        ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
    )
    st.divider()
    st.caption("Developer: Bill Giner Lopez Milla")
    st.caption("Egresado Ingenier赤a de Sistemas - UNI")
    st.caption("Ciclo Acad谷mico 2026")

if seccion == "Home":
    st.title("?? PySistemas Analytics: Plataforma de Gesti車n Febreo")
    st.divider()
    
    col_img, col_info = st.columns([1, 2])
    
    with col_img:
        try:
            st.image("logo_lopez.png", use_container_width=True)
        except:
            st.warning("Archivo logo_lopez.png no hallado en el repositorio")

    with col_info:
        st.subheader("?? Ficha T谷cnica del Developer")
        st.write(f"**Nombre:** Bill Giner Lopez Milla")
        st.write(f"**Especialidad:** Ingenier赤a de Sistemas")
        st.write(f"**Sede:** San Mart赤n de Porres, Lima")
        st.write(f"**M車dulo:** Python Fundamentals & Analytics")
        st.write(f"**A?o:** 2026")

    st.divider()
    
    with st.container():
        st.markdown("#### ?? Descripci車n del Proyecto")
        st.write("""
        Implementaci車n de una infraestructura digital orientada a la optimizaci車n de procesos. 
        El sistema utiliza estructuras de datos din芍micas y l車gica de programaci車n avanzada 
        para la resoluci車n de casos de negocio en entornos de ingenier赤a de sistemas.
        """)

    st.markdown("#### ??? Tecnolog赤as Utilizadas")
    st.info("Core: Python 3.x | Data: Pandas & NumPy | Interface: Streamlit Framework")

elif seccion == "Ejercicio 1":
    st.header("Ejercicio 1 每 Flujo de caja con listas")
    
    st.markdown("""
    Desarrollo de un m車dulo para el registro de movimientos financieros en una lista din芍mica. 
    Permite el monitoreo de ingresos y gastos para determinar el balance neto de liquidez.
    """)

    with st.container(border=True):
        col_c, col_t, col_m = st.columns([2, 1, 1])
        
        with col_c:
            concepto = st.text_input("Concepto")
        with col_t:
            tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
        with col_m:
            valor = st.number_input("Valor", min_value=0.0, step=1.0)

        if st.button("Agregar movimiento", use_container_width=True):
            if concepto and valor > 0:
                st.session_state.movimientos.append({
                    "Concepto": concepto, 
                    "Tipo": tipo, 
                    "Valor": valor
                })
                st.toast("Movimiento registrado satisfactoriamente")
            else:
                st.warning("Se requiere una descripci車n y un valor positivo")

    if st.session_state.movimientos:
        st.divider()
        st.write("##### Tabla de movimientos")
        df_movs = pd.DataFrame(st.session_state.movimientos)
        st.dataframe(df_movs, use_container_width=True, hide_index=True)

        t_ingresos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso")
        t_gastos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto")
        saldo_final = t_ingresos - t_gastos

        st.write("##### Resultado final del flujo de caja")
        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric("Total Ingresos", f"{t_ingresos:,.2f}")
        col_m2.metric("Total Gastos", f"{t_gastos:,.2f}")
        col_m3.metric("Saldo Final", f"{saldo_final:,.2f}")

        if saldo_final > 0:
            st.success(f"El flujo de caja est芍 a favor: {saldo_final:,.2f}")
        elif saldo_final < 0:
            st.error(f"El flujo de caja est芍 en contra: {saldo_final:,.2f}")
        else:
            st.info("El flujo de caja se encuentra en equilibrio operativo")
            
        if st.button("Reiniciar registros"):
            st.session_state.movimientos = []
            st.rerun()
    else:
        st.info("No se han detectado registros en la sesi車n actual")