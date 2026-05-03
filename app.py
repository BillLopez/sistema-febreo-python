import streamlit as st
import pandas as pd
import numpy as np

# CONFIGURACION DE LA SUITE
st.set_page_config(
    page_title="Nexus Systems - Bill Lopez", 
    page_icon="???", 
    layout="wide"
)

# PERSISTENCIA DE DATOS (SESSION STATE)
if "movimientos" not in st.session_state:
    st.session_state.movimientos = []
if "db_inventario" not in st.session_state:
    st.session_state.db_inventario = []
if "historial_metricas" not in st.session_state:
    st.session_state.historial_metricas = []
if "db_actividades" not in st.session_state:
    st.session_state.db_actividades = []

# NAVEGACION Y BRANDING
with st.sidebar:
    st.title("Nexus Control")
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
    st.title("Systems: Advanced Management Suite")
    st.divider()
    
    col_img, col_info = st.columns([1, 2])
    with col_img:
        try:
            st.image("logo_lopez.png", use_container_width=True)
        except:
            st.warning("Logo institucional no hallado")

    with col_info:
        st.header("Ficha Tecnica del Developer")
        st.write(f"**Identidad:** Bill Giner Lopez Milla")
        st.write(f"**Formacion:** Ingenieria de Sistemas - UNI")
        st.write(f"**Ubicacion:** San Martin de Porres, Lima")
        st.write(f"**Especialidad:** Python Fundamentals and Analytics")
        st.write(f"**Version:** 2.0 (Stable)")

    st.divider()
    with st.container(border=True):
        st.subheader("Arquitectura del Proyecto")
        st.write("""
        Plataforma integral de gestion dise?ada para la optimizacion de recursos y analisis de datos. 
        Este sistema despliega estructuras de datos avanzadas y programacion orientada a objetos (POO) 
        para resolver problemas complejos de ingenieria mediante una interfaz de usuario minimalista.
        """)
    st.success("Framework: Streamlit | Engine: Python 3.x | Logic: POO and Functional Programming")

# SECCION: EJERCICIO 1
elif seccion == "Ejercicio 1":
    st.title("Ejercicio 1: Analisis de Flujo de Caja")
    st.info("Monitoreo financiero basado en listas dinamicas para el control de liquidez.")[cite: 3]

    with st.container(border=True):
        st.header("Registro de Transacciones")
        c1, c2, c3 = st.columns([2, 1, 1])
        with c1: concepto = st.text_input("Concepto Operativo")[cite: 3]
        with c2: tipo = st.selectbox("Tipo", ["Ingreso", "Gasto"])[cite: 3]
        with c3: valor = st.number_input("Monto", min_value=0.0, step=1.0)[cite: 3]

        if st.button("Procesar Movimiento", use_container_width=True):[cite: 3]
            if concepto and valor > 0:
                st.session_state.movimientos.append({"Concepto": concepto, "Tipo": tipo, "Valor": valor})[cite: 3]
                st.toast("Transaccion registrada")
            else: st.warning("Datos incompletos")

    if st.session_state.movimientos:
        st.divider()
        st.subheader("Historial Consolidado")
        df_movs = pd.DataFrame(st.session_state.movimientos)[cite: 3]
        st.dataframe(df_movs, use_container_width=True, hide_index=True)[cite: 3]

        t_ing = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso")[cite: 3]
        t_gas = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto")[cite: 3]
        saldo = t_ing - t_gas[cite: 3]

        st.header("Balance General")
        m1, m2, m3 = st.columns(3)
        m1.metric("Ingresos", f"{t_ing:,.2f}")[cite: 3]
        m2.metric("Egresos", f"{t_gas:,.2f}")[cite: 3]
        m3.metric("Saldo Neto", f"{saldo:,.2f}")[cite: 3]

        if saldo > 0: st.success(f"Estado de Caja: Superavit ({saldo:,.2f})")[cite: 3]
        elif saldo < 0: st.error(f"Estado de Caja: Deficit ({saldo:,.2f})")[cite: 3]
        if st.button("Limpiar Sesion"):
            st.session_state.movimientos = []
            st.rerun()

# SECCION: EJERCICIO 2
elif seccion == "Ejercicio 2":
    st.title("Ejercicio 2: Control de Activos (NumPy)")
    st.info("Gestion de inventario tecnico procesado mediante arreglos multidimensionales.")[cite: 3]

    with st.container(border=True):
        st.header("Captura de Registros")
        n1, n2 = st.columns(2)
        with n1: nom_p = st.text_input("Descripcion del Activo")[cite: 3]
        with n2: cat_p = st.selectbox("Categoria", ["Hardware", "Software", "Redes", "Otros"])[cite: 3]
        
        p1, p2 = st.columns(2)
        with p1: pre_p = st.number_input("Costo Unitario", min_value=0.0)[cite: 3]
        with p2: can_p = st.number_input("Stock", min_value=0, step=1)[cite: 3]
            
        if st.button("Confirmar Registro", use_container_width=True):[cite: 3]
            if nom_p:
                reg_np = np.array([nom_p, cat_p, pre_p, can_p, pre_p * can_p])[cite: 3]
                st.session_state.db_inventario.append(reg_np)[cite: 3]
                st.toast("Matriz actualizada")
            else: st.error("Nombre requerido")

    if st.session_state.db_inventario:
        st.divider()
        st.subheader("Matriz de Inventario")
        df_inv = pd.DataFrame(st.session_state.db_inventario, columns=["Producto", "Categoria", "Precio", "Cantidad", "Total"])[cite: 3]
        df_inv[["Precio", "Cantidad", "Total"]] = df_inv[["Precio", "Cantidad", "Total"]].apply(pd.to_numeric)[cite: 3]
        st.dataframe(df_inv, use_container_width=True, hide_index=True)[cite: 3]
        st.success(f"Valuacion Total del Inventario: {np.sum(df_inv['Total'].values):,.2f}")
        if st.button("Reiniciar Matriz"):
            st.session_state.db_inventario = []
            st.rerun()

# SECCION: EJERCICIO 3
elif seccion == "Ejercicio 3":
    st.title("Ejercicio 3: Analitica de Sistemas")
    st.info("Ejecucion de funciones externas para la medicion de eficiencia y disponibilidad.")[cite: 3]

    metrica = st.selectbox("Seleccione Proceso de Calculo", ["Clasificacion (F1-Score)", "Disponibilidad de Red"])[cite: 3]

    with st.container(border=True):
        if "Clasificacion" in metrica:
            st.header("Metricas de Clasificacion")
            c1, c2, c3 = st.columns(3)
            with c1: tp = st.number_input("TP", min_value=0)[cite: 3]
            with c2: fp = st.number_input("FP", min_value=0)[cite: 3]
            with c3: fn = st.number_input("FN", min_value=0)[cite: 3]
            if st.button("Calcular F1", use_container_width=True):[cite: 3]
                p = tp/(tp+fp) if (tp+fp)>0 else 0
                r = tp/(tp+fn) if (tp+fn)>0 else 0
                f1 = (2*p*r/(p+r)) if (p+r)>0 else 0
                st.session_state.historial_metricas.append({"Metrica": "F1", "Valor": round(f1, 4)})[cite: 3]
                st.success(f"Analisis Finalizado: {f1:.4f}")

        else:
            st.header("Calculo de Disponibilidad")
            t1, t2 = st.columns(2)
            with t1: tt = st.number_input("Horas Totales", min_value=1.0)[cite: 3]
            with t2: tc = st.number_input("Horas Caida", min_value=0.0)[cite: 3]
            if st.button("Calcular Uptime", use_container_width=True):[cite: 3]
                disp = ((tt-tc)/tt)*100 if tt>tc else 0
                st.session_state.historial_metricas.append({"Metrica": "Uptime", "Valor": round(disp, 2)})[cite: 3]
                st.success(f"Disponibilidad de Red: {disp:.2f}%")

    if st.session_state.historial_metricas:
        st.divider()
        st.subheader("Historico de Operaciones")
        st.dataframe(pd.DataFrame(st.session_state.historial_metricas), use_container_width=True)[cite: 3]

# SECCION: EJERCICIO 4
elif seccion == "Ejercicio 4":
    st.title("Ejercicio 4: Gestion CRUD POO")
    st.info("Administracion de actividades mediante Programacion Orientada a Objetos.")[cite: 3]

    class Actividad:[cite: 4]
        def __init__(self, nom, tip, pre, gas):[cite: 4]
            self.nom, self.tip, self.pre, self.gas = nom, tip, pre, gas[cite: 4]
        def estado(self): return "OK" if self.gas <= self.pre else "Excedido"[cite: 4]

    t_add, t_view, t_mod, t_del = st.tabs(["A?adir", "Consultar", "Modificar", "Remover"])[cite: 3]

    with t_add:
        st.header("Registro de Nueva Actividad")
        with st.container(border=True):
            a1, a2 = st.columns(2)
            with a1: n = st.text_input("Actividad"); t = st.selectbox("Categoria Recurso", ["TI", "Personal", "Logistica"])[cite: 3]
            with a2: p = st.number_input("Presupuesto"); g = st.number_input("Ejecucion")[cite: 3]
            if st.button("Guardar Actividad"):[cite: 3]
                if n: st.session_state.db_actividades.append(Actividad(n, t, p, g)); st.toast("Guardado")[cite: 3, 4]
                else: st.error("Error")

    with t_view:
        st.header("Visualizacion de Datos")
        if st.session_state.db_actividades:
            d = [{"Actividad": x.nom, "Tipo": x.tip, "Presupuesto": x.pre, "Gasto": x.gas, "Estado": x.estado()} for x in st.session_state.db_actividades][cite: 4]
            st.dataframe(pd.DataFrame(d), use_container_width=True, hide_index=True)[cite: 3]
        else: st.info("Sin registros")

    with t_mod:
        st.header("Actualizacion de Gasto")
        if st.session_state.db_actividades:
            sel = st.selectbox("Seleccionar Actividad", [x.nom for x in st.session_state.db_actividades])[cite: 3]
            val = st.number_input("Nuevo Gasto Real")[cite: 3]
            if st.button("Actualizar"):[cite: 3]
                for x in st.session_state.db_actividades:
                    if x.nom == sel: x.gas = val; st.rerun()[cite: 3]
        else: st.warning("Vacio")

    with t_del:
        st.header("Remover Registro")
        if st.session_state.db_actividades:
            sel_d = st.selectbox("Seleccionar para eliminar", [x.nom for x in st.session_state.db_actividades])[cite: 3]
            if st.button("Confirmar"):[cite: 3]
                st.session_state.db_actividades = [x for x in st.session_state.db_actividades if x.nom != sel_d]; st.rerun()[cite: 3]
        else: st.warning("Vacio")