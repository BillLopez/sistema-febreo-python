import streamlit as st
import pandas as pd
import numpy as np

# CONFIGURACION DE LA SUITE
st.set_page_config(
    page_title="Nexus Systems - Bill Lopez", 
    page_icon="???", 
    layout="wide"
)

# PERSISTENCIA DE DATOS
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
    st.title("Panel de Control")
    seccion = st.selectbox(
        "Navegacion Principal",
        ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
    )
    st.divider()
    st.caption("Developer: Bill Giner Lopez Milla")
    st.caption("Egresado Ingenieria de Sistemas - UNI")
    st.caption("Lima, 2026")

# HOME
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

    st.divider()
    with st.container(border=True):
        st.subheader("Arquitectura del Proyecto")
        st.write("""
        Plataforma integral de gestion para la optimizacion de recursos y analisis de datos. 
        Este sistema despliega estructuras de datos avanzadas y programacion orientada a objetos (POO) 
        para resolver problemas complejos de ingenieria mediante una interfaz de usuario minimalista.
        """)
    st.success("Framework: Streamlit | Engine: Python 3.x | Logic: POO and Functional Programming")

# EJERCICIO 1
elif seccion == "Ejercicio 1":
    st.title("Ejercicio 1: Analisis de Flujo de Caja")
    st.info("Monitoreo financiero basado en listas dinamicas para el control de liquidez.")

    with st.container(border=True):
        st.header("Registro de Transacciones")
        c1, c2, c3 = st.columns([2, 1, 1])
        with c1: concepto = st.text_input("Concepto Operativo")
        with c2: tipo = st.selectbox("Tipo", ["Ingreso", "Gasto"])
        with c3: valor = st.number_input("Monto", min_value=0.0, step=1.0)

        if st.button("Procesar Movimiento", use_container_width=True):
            if concepto and valor > 0:
                st.session_state.movimientos.append({"Concepto": concepto, "Tipo": tipo, "Valor": valor})
                st.toast("Transaccion registrada")
            else: st.warning("Datos incompletos")

    if st.session_state.movimientos:
        st.divider()
        st.subheader("Historial Consolidado")
        df_movs = pd.DataFrame(st.session_state.movimientos)
        st.dataframe(df_movs, use_container_width=True, hide_index=True)

        t_ing = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso")
        t_gas = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto")
        saldo = t_ing - t_gas

        st.header("Balance General")
        m1, m2, m3 = st.columns(3)
        m1.metric("Ingresos", f"{t_ing:,.2f}")
        m2.metric("Egresos", f"{t_gas:,.2f}")
        m3.metric("Saldo Neto", f"{saldo:,.2f}")

        if saldo > 0: st.success(f"Estado de Caja: Superavit ({saldo:,.2f})")
        elif saldo < 0: st.error(f"Estado de Caja: Deficit ({saldo:,.2f})")
        
        if st.button("Limpiar Sesion"):
            st.session_state.movimientos = []
            st.rerun()

# EJERCICIO 2
elif seccion == "Ejercicio 2":
    st.title("Ejercicio 2: Control de Activos (NumPy)")
    st.info("Gestion de inventario tecnico procesado mediante arreglos multidimensionales.")

    with st.container(border=True):
        st.header("Captura de Registros")
        n1, n2 = st.columns(2)
        with n1: nom_p = st.text_input("Descripcion del Activo")
        with n2: cat_p = st.selectbox("Categoria", ["Hardware", "Software", "Redes", "Otros"])
        
        p1, p2 = st.columns(2)
        with p1: pre_p = st.number_input("Costo Unitario", min_value=0.0)
        with p2: can_p = st.number_input("Stock", min_value=0, step=1)
            
        if st.button("Confirmar Registro", use_container_width=True):
            if nom_p:
                reg_np = np.array([nom_p, cat_p, pre_p, can_p, pre_p * can_p])
                st.session_state.db_inventario.append(reg_np)
                st.toast("Matriz actualizada")
            else: st.error("Nombre requerido")

    if st.session_state.db_inventario:
        st.divider()
        st.subheader("Matriz de Inventario")
        df_inv = pd.DataFrame(st.session_state.db_inventario, columns=["Producto", "Categoria", "Precio", "Cantidad", "Total"])
        df_inv[["Precio", "Cantidad", "Total"]] = df_inv[["Precio", "Cantidad", "Total"]].apply(pd.to_numeric)
        st.dataframe(df_inv, use_container_width=True, hide_index=True)
        st.success(f"Valuacion Total del Inventario: {np.sum(df_inv['Total'].values):,.2f}")
        
        if st.button("Reiniciar Matriz"):
            st.session_state.db_inventario = []
            st.rerun()

# EJERCICIO 3
elif seccion == "Ejercicio 3":
    st.title("Ejercicio 3: Analitica de Sistemas")
    st.info("Ejecucion de funciones externas para la medicion de eficiencia y disponibilidad.")

    metrica = st.selectbox("Seleccione Proceso de Calculo", ["Clasificacion (F1-Score)", "Disponibilidad de Red"])

    with st.container(border=True):
        if "Clasificacion" in metrica:
            st.header("Metricas de Clasificacion")
            c1, c2, c3 = st.columns(3)
            with c1: tp = st.number_input("TP", min_value=0)
            with c2: fp = st.number_input("FP", min_value=0)
            with c3: fn = st.number_input("FN", min_value=0)
            if st.button("Calcular F1", use_container_width=True):
                p = tp/(tp+fp) if (tp+fp)>0 else 0
                r = tp/(tp+fn) if (tp+fn)>0 else 0
                f1 = (2*p*r/(p+r)) if (p+r)>0 else 0
                st.session_state.historial_metricas.append({"Metrica": "F1", "Valor": round(f1, 4)})
                st.success(f"Analisis Finalizado: {f1:.4f}")
        else:
            st.header("Calculo de Disponibilidad")
            t1, t2 = st.columns(2)
            with t1: tt = st.number_input("Horas Totales", min_value=1.0)
            with t2: tc = st.number_input("Horas Caida", min_value=0.0)
            if st.button("Calcular Uptime", use_container_width=True):
                disp = ((tt-tc)/tt)*100 if tt>tc else 0
                st.session_state.historial_metricas.append({"Metrica": "Uptime", "Valor": round(disp, 2)})
                st.success(f"Disponibilidad de Red: {disp:.2f}%")

    if st.session_state.historial_metricas:
        st.divider()
        st.subheader("Historico de Operaciones")
        st.dataframe(pd.DataFrame(st.session_state.historial_metricas), use_container_width=True)

# SECCION: EJERCICIO 4
elif seccion == "Ejercicio 4":
    st.title("Ejercicio 4: Gestion CRUD POO")
    st.info("Administracion de actividades mediante Programacion Orientada a Objetos.")

    class Actividad:
        def __init__(self, nom, tip, pre, gas):
            self.nom, self.tip, self.pre, self.gas = nom, tip, pre, gas
        def estado(self): return "OK" if self.gas <= self.pre else "Excedido"

    t_add, t_view, t_mod, t_del = st.tabs(["Anadir", "Consultar", "Modificar", "Remover"])

    with t_add:
        st.header("Registro de Nueva Actividad")
        with st.container(border=True):
            a1, a2 = st.columns(2)
            with a1: 
                n = st.text_input("Actividad")
                t = st.selectbox("Categoria Recurso", ["TI", "Personal", "Logistica"])
            with a2: 
                p = st.number_input("Presupuesto")
                g = st.number_input("Ejecucion")
            if st.button("Guardar Actividad"):
                if n: 
                    st.session_state.db_actividades.append(Actividad(n, t, p, g))
                    st.toast("Guardado")
                else: st.error("Error")

    with t_view:
        st.header("Visualizacion de Datos")
        if st.session_state.db_actividades:
            d = [{"Actividad": x.nom, "Tipo": x.tip, "Presupuesto": x.pre, "Gasto": x.gas, "Estado": x.estado()} for x in st.session_state.db_actividades]
            st.dataframe(pd.DataFrame(d), use_container_width=True, hide_index=True)
        else: st.info("Sin registros")

    with t_mod:
        st.header("Actualizacion de Gasto")
        if st.session_state.db_actividades:
            sel = st.selectbox("Seleccionar Actividad", [x.nom for x in st.session_state.db_actividades])
            val = st.number_input("Nuevo Gasto Real")
            if st.button("Actualizar"):
                for x in st.session_state.db_actividades:
                    if x.nom == sel: 
                        x.gas = val
                        st.rerun()
        else: st.warning("Vacio")

    with t_del:
        st.header("Remover Registro")
        if st.session_state.db_actividades:
            sel_d = st.selectbox("Seleccionar para eliminar", [x.nom for x in st.session_state.db_actividades])
            if st.button("Confirmar"):
                st.session_state.db_actividades = [x for x in st.session_state.db_actividades if x.nom != sel_d]
                st.rerun()
        else: st.warning("Vacio")