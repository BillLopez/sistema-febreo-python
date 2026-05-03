import streamlit as st
import pandas as pd
import numpy as np

# CONFIGURACION
st.set_page_config(
    page_title="Sistema Febreo - Bill Lopez", 
    page_icon="??", 
    layout="wide"
)

if "movimientos" not in st.session_state:
    st.session_state.movimientos = []
if "db_inventario" not in st.session_state:
    st.session_state.db_inventario = []

with st.sidebar:
    st.title("Panel de Control")
    seccion = st.selectbox(
        "Navegacion Principal",
        ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
    )
    st.divider()
    st.caption("Developer: Bill Giner Lopez Milla")
    st.caption("Egresado Ingenieria de Sistemas - UNI")
    st.caption("Ciclo Academico 2026")

# HOME
if seccion == "Home":
    st.title("?? PySistemas Analytics: Plataforma de Gestion Febreo")
    st.divider()
    
    col_img, col_info = st.columns([1, 2])
    
    with col_img:
        try:
            st.image("logo_lopez.png", use_container_width=True)
        except:
            st.warning("Archivo logo_lopez.png no hallado en el repositorio")

    with col_info:
        st.subheader("?? Ficha Tecnica del Developer")
        st.write(f"**Nombre:** Bill Giner Lopez Milla")
        st.write(f"**Especialidad:** Ingenieria de Sistemas")
        st.write(f"**Residencia:** San Martin de Porres, Lima")
        st.write(f"**Modulo:** Python Fundamentals and Analytics")
        st.write(f"**Anio:** 2026")

    st.divider()
    
    with st.container():
        st.markdown("#### ?? Descripcion del Proyecto")
        st.write("""
        Implementacion de una infraestructura digital orientada a la optimizacion de procesos. 
        El sistema utiliza estructuras de datos dinamicas y logica de calculo avanzada 
        para la resolucion de casos de negocio en entornos de ingenieria de sistemas.
        """)

    st.markdown("#### ??? Tecnologias Utilizadas")
    st.info("Core: Python 3.x | Data: Pandas and NumPy | Interface: Streamlit Framework")

# EJERCICIO 1
elif seccion == "Ejercicio 1":
    st.header("Ejercicio 1 - Flujo de caja con listas")
    
    st.markdown("""
    Desarrollo de un modulo para el registro de movimientos financieros en una lista dinamica. 
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
                st.toast("Movimiento registrado")
            else:
                st.warning("Se requiere una descripcion y un valor positivo")

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
            st.success(f"El flujo de caja esta a favor: {saldo_final:,.2f}")
        elif saldo_final < 0:
            st.error(f"El flujo de caja esta en contra: {saldo_final:,.2f}")
        else:
            st.info("El flujo de caja se encuentra en equilibrio")
            
        if st.button("Reiniciar registros"):
            st.session_state.movimientos = []
            st.rerun()
    else:
        st.info("No se han detectado registros en la sesion actual")

# EJERCICIO 2
elif seccion == "Ejercicio 2":
    st.header("Ejercicio 2 - Registro con NumPy, arrays y DataFrame")
    
    st.markdown("""
    Formulario para registrar informacion utilizando arreglos de NumPy para el procesamiento de datos 
    antes de su conversion a un DataFrame actualizado.
    """)

    with st.container(border=True):
        col_n, col_cat = st.columns(2)
        with col_n:
            nombre_p = st.text_input("Nombre del producto")
        with col_cat:
            categoria_p = st.selectbox("Categoria", ["Electronica", "Mobiliario", "Suministros", "Otros"])
        
        col_pre, col_can = st.columns(2)
        with col_pre:
            precio_p = st.number_input("Precio", min_value=0.0, step=0.1)
        with col_can:
            cantidad_p = st.number_input("Cantidad", min_value=0, step=1)
            
        if st.button("Agregar nuevo registro", use_container_width=True):
            if nombre_p:
                total_p = precio_p * cantidad_p
                nuevo_registro = np.array([nombre_p, categoria_p, precio_p, cantidad_p, total_p])
                st.session_state.db_inventario.append(nuevo_registro)
                st.toast("Registro agregado exitosamente")
            else:
                st.error("El nombre del producto es obligatorio")

    if st.session_state.db_inventario:
        st.divider()
        columnas = ["Producto", "Categoria", "Precio", "Cantidad", "Total"]
        df_inventario = pd.DataFrame(st.session_state.db_inventario, columns=columnas)
        
        df_inventario["Precio"] = pd.to_numeric(df_inventario["Precio"])
        df_inventario["Cantidad"] = pd.to_numeric(df_inventario["Cantidad"])
        df_inventario["Total"] = pd.to_numeric(df_inventario["Total"])
        
        st.write("##### Tabla de inventario actualizada")
        st.dataframe(df_inventario, use_container_width=True, hide_index=True)
        
        valor_total_stock = np.sum(df_inventario["Total"].values)
        st.info(f"Valorizacion total del inventario: {valor_total_stock:,.2f}")
        
        if st.button("Limpiar inventario"):
            st.session_state.db_inventario = []
            st.rerun()
    else:
        st.info("No hay registros en el inventario")