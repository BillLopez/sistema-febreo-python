import streamlit as st
import pandas as pd
import numpy as np

# CONFIGURACION DE LA INTERFAZ
st.set_page_config(
    page_title="Sistema Febreo - Bill Lopez", 
    page_icon="??", 
    layout="wide"
)

# INICIALIZACION DE ESTADOS DE SESION
if "movimientos" not in st.session_state:
    st.session_state.movimientos = []
if "db_inventario" not in st.session_state:
    st.session_state.db_inventario = []
if "historial_metricas" not in st.session_state:
    st.session_state.historial_metricas = []
if "db_actividades" not in st.session_state:
    st.session_state.db_actividades = []

# NAVEGACION LATERAL
with st.sidebar:
    st.title("Panel de Control")
    seccion = st.selectbox(
        "Navegacion Principal",
        ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
    )
    st.divider()
    st.caption("Developer: Bill Giner Lopez Milla")
    st.caption("Egresado Ingenieria de Sistemas - UNI")
    st.caption("Lima, 2026")

# SECCION: HOME
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
        st.header("Ficha Tecnica del Developer")
        st.write(f"**Nombre:** Bill Giner Lopez Milla")
        st.write(f"**Especialidad:** Ingenieria de Sistemas")
        st.write(f"**Residencia:** San Martin de Porres, Lima")
        st.write(f"**Modulo:** Python Fundamentals and Analytics")
        st.write(f"**Anio:** 2026")

    st.divider()
    
    with st.container():
        st.subheader("Descripcion del Proyecto")
        st.write("""
        Implementacion de una infraestructura digital orientada a la optimizacion de procesos. 
        El sistema utiliza estructuras de datos dinamicas y logica de calculo avanzada 
        para la resolucion de casos de negocio en entornos de ingenieria de sistemas.
        """)

    st.success("Core: Python 3.x | Data: Pandas and NumPy | Interface: Streamlit Framework")

# SECCION: EJERCICIO 1
elif seccion == "Ejercicio 1":
    st.title("?? Ejercicio 1 - Flujo de caja con listas")
    
    st.info("""
    Desarrollo de un modulo para el registro de movimientos financieros en una lista dinamica. 
    Permite el monitoreo de ingresos y gastos para determinar el balance neto de liquidez.
    """)

    with st.container(border=True):
        st.header("Entrada de Datos Financieros")
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
        st.subheader("Tabla de movimientos")
        df_movs = pd.DataFrame(st.session_state.movimientos)
        st.dataframe(df_movs, use_container_width=True, hide_index=True)

        t_ingresos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso")
        t_gastos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto")
        saldo_final = t_ingresos - t_gastos

        st.header("Resultado final del flujo de caja")
        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric("Total Ingresos", f"{t_ingresos:,.2f}")
        col_m2.metric("Total Gastos", f"{t_gastos:,.2f}")
        col_m3.metric("Saldo Final", f"{saldo_final:,.2f}")

        if saldo_final > 0:
            st.success(f"El flujo de caja esta a favor: {saldo_final:,.2f}")
        elif saldo_final < 0:
            st.error(f"El flujo de caja esta en contra: {saldo_final:,.2f}")
        else:
            st.warning("El flujo de caja se encuentra en equilibrio")
            
        if st.button("Reiniciar registros"):
            st.session_state.movimientos = []
            st.rerun()

# SECCION: EJERCICIO 2
elif seccion == "Ejercicio 2":
    st.title("?? Ejercicio 2 - Registro con NumPy y DataFrame")
    
    st.info("""
    Formulario para registrar informacion utilizando arreglos de NumPy para el procesamiento de datos 
    antes de su conversion a un DataFrame actualizado.
    """)

    with st.container(border=True):
        st.header("Captura de Activos")
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
        st.subheader("Tabla de inventario actualizada")
        columnas = ["Producto", "Categoria", "Precio", "Cantidad", "Total"]
        df_inventario = pd.DataFrame(st.session_state.db_inventario, columns=columnas)
        
        df_inventario["Precio"] = pd.to_numeric(df_inventario["Precio"])
        df_inventario["Cantidad"] = pd.to_numeric(df_inventario["Cantidad"])
        df_inventario["Total"] = pd.to_numeric(df_inventario["Total"])
        
        st.dataframe(df_inventario, use_container_width=True, hide_index=True)
        
        valor_total_stock = np.sum(df_inventario["Total"].values)
        st.success(f"Valorizacion total del inventario: {valor_total_stock:,.2f}")
        
        if st.button("Limpiar inventario"):
            st.session_state.db_inventario = []
            st.rerun()

# SECCION: EJERCICIO 3
elif seccion == "Ejercicio 3":
    st.title("?? Ejercicio 3 - Funciones Externas")
    
    st.info("""
    Implementacion de funciones para el calculo de metricas de rendimiento en sistemas de clasificacion 
    y evaluacion de disponibilidad de sistemas de informacion.
    """)

    st.header("Selector de Funciones de Analitica")
    opcion_metrica = st.selectbox(
        "Seleccione la metrica a evaluar",
        ["Metricas de Clasificacion (Precision, Recall, F1)", "Disponibilidad de Sistema"]
    )

    with st.container(border=True):
        if opcion_metrica == "Metricas de Clasificacion (Precision, Recall, F1)":
            st.subheader("Parametros de Matriz de Confusion")
            col_tp, col_fp, col_fn = st.columns(3)
            with col_tp: tp = st.number_input("Verdaderos Positivos (TP)", min_value=0, step=1)
            with col_fp: fp = st.number_input("Falsos Positivos (FP)", min_value=0, step=1)
            with col_fn: fn = st.number_input("Falsos Negativos (FN)", min_value=0, step=1)

            if st.button("Ejecutar Evaluacion", use_container_width=True):
                precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
                recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
                f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0.0
                
                st.session_state.historial_metricas.append({
                    "Metrica": "Clasificacion", "Resultado": f"F1: {f1:.4f}",
                    "Timestamp": pd.Timestamp.now().strftime("%H:%M:%S")
                })
                st.success(f"Analisis completado: F1 Score de {f1:.4f}")

        elif opcion_metrica == "Disponibilidad de Sistema":
            st.subheader("Parametros de Tiempo de Actividad")
            col_tt, col_tc = st.columns(2)
            with col_tt: t_total = st.number_input("Tiempo Total (horas)", min_value=1.0, step=1.0)
            with col_tc: t_caida = st.number_input("Tiempo de Caida (horas)", min_value=0.0, step=0.1)

            if st.button("Calcular Disponibilidad", use_container_width=True):
                if t_caida <= t_total:
                    disp = ((t_total - t_caida) / t_total) * 100
                    st.session_state.historial_metricas.append({
                        "Metrica": "Disponibilidad", "Resultado": f"{disp:.2f}%",
                        "Timestamp": pd.Timestamp.now().strftime("%H:%M:%S")
                    })
                    st.success(f"Calculo finalizado: {disp:.2f}%")
                else:
                    st.error("Error: El tiempo de caida excede el tiempo total")

    if st.session_state.historial_metricas:
        st.divider()
        st.subheader("Tabla historica de resultados")
        st.dataframe(pd.DataFrame(st.session_state.historial_metricas), use_container_width=True, hide_index=True)
        if st.button("Limpiar historico"):
            st.session_state.historial_metricas = []
            st.rerun()

# SECCION: EJERCICIO 4
elif seccion == "Ejercicio 4":
    st.title("??? Ejercicio 4 - Gestion de Actividades POO")
    
    st.info("""
    Sistema de gestion de proyectos basado en Programacion Orientada a Objetos. 
    Permite administrar el ciclo de vida completo de actividades mediante operaciones CRUD.
    """)

    class Actividad:
        def __init__(self, nombre, tipo, presupuesto, gasto_real):
            self.nombre, self.tipo, self.presupuesto, self.gasto_real = nombre, tipo, presupuesto, gasto_real
        def esta_en_presupuesto(self): return self.gasto_real <= self.presupuesto

    tab_crear, tab_leer, tab_update, tab_delete = st.tabs(["Crear", "Visualizar", "Actualizar", "Eliminar"])

    with tab_crear:
        st.header("Registro de Nueva Actividad")
        with st.container(border=True):
            c1, c2 = st.columns(2)
            with c1:
                nom = st.text_input("Nombre de la actividad")
                tip = st.selectbox("Tipo de recurso", ["Personal", "Equipos", "Materiales", "Logistica"])
            with c2:
                pre = st.number_input("Presupuesto asignado", min_value=0.0)
                gas = st.number_input("Gasto ejecutado", min_value=0.0)
            if st.button("Guardar Actividad", use_container_width=True):
                if nom:
                    st.session_state.db_actividades.append(Actividad(nom, tip, pre, gas))
                    st.toast("Actividad guardada")
                else: st.error("Nombre obligatorio")

    with tab_leer:
        st.header("Listado Maestro")
        if st.session_state.db_actividades:
            data = [{"Actividad": a.nombre, "Tipo": a.tipo, "Presupuesto": a.presupuesto, "Gasto": a.gasto_real, "Estado": "OK" if a.esta_en_presupuesto() else "Excedido"} for a in st.session_state.db_actividades]
            st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
        else: st.info("Sin registros")

    with tab_update:
        st.header("Edicion de Gastos")
        if st.session_state.db_actividades:
            seleccion = st.selectbox("Seleccione actividad", [a.nombre for a in st.session_state.db_actividades])
            nuevo_valor = st.number_input("Actualizar Gasto Real", min_value=0.0)
            if st.button("Aplicar Cambios", use_container_width=True):
                for a in st.session_state.db_actividades:
                    if a.nombre == seleccion:
                        a.gasto_real = nuevo_valor
                        st.rerun()
        else: st.warning("Sin datos")

    with tab_delete:
        st.header("Remover Actividad")
        if st.session_state.db_actividades:
            seleccion_del = st.selectbox("Seleccione actividad para borrar", [a.nombre for a in st.session_state.db_actividades])
            if st.button("Confirmar Eliminacion", use_container_width=True):
                st.session_state.db_actividades = [a for a in st.session_state.db_actividades if a.nombre != seleccion_del]
                st.rerun()
        else: st.warning("Sin datos")