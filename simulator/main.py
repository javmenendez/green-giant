from scenario1 import simular_escenario_1
import streamlit as st

st.sidebar.header("Parámetros Generales")
años = st.sidebar.slider("Años a simular", min_value=10, max_value=40, value=30)
interes_hipoteca = st.sidebar.selectbox("Interés hipotecario (%)", [2.5, 3.0], index=1) / 100
porcentaje_financiacion = st.sidebar.selectbox("Porcentaje financiado (%)", [70, 80], index=0)
duracion_hipoteca = st.sidebar.selectbox("Duración hipoteca (años)", [20, 25, 30], index=2)

st.sidebar.header("Parámetros específicos Escenario 1")
precio_piso_inicial = st.sidebar.number_input("Precio inicial por piso (€)", value=115000)
cashflow_inicial = st.sidebar.number_input("Cashflow neto anual por piso (€)", value=2750)
coste_inversion = st.sidebar.number_input("Coste total inversión por piso (€)", value=50000)
ahorro_inicial = st.sidebar.number_input("Ahorro inicial (€)", value=20000)
ahorro_anual = st.sidebar.number_input("Ahorro anual total (€)", value=50000)
revalorizacion_anual = st.sidebar.slider("Revalorización anual (%)", min_value=0.0, max_value=10.0, value=2.0) / 100
incremento_cashflow = st.sidebar.slider("Incremento anual cashflow (%)", min_value=0.0, max_value=10.0, value=2.0) / 100
incremento_ahorro = st.sidebar.slider("Incremento anual ahorro (%)", min_value=0.0, max_value=10.0, value=2.0) / 100
saldo_minimo = st.sidebar.number_input("Saldo mínimo en cuenta (€)", value=20000)

alquiler_medio_mes = st.sidebar.number_input("Alquiler medio al mes (€)", value=900)
gastos_medios_mes = st.sidebar.number_input("Gastos medios al mes (€)", value=400)

if st.sidebar.button("Simular Escenario 1"):
    df_resultados = simular_escenario_1(
        años=años,
        precio_piso_inicial=precio_piso_inicial,
        cashflow_inicial=cashflow_inicial,
        coste_inversion=coste_inversion,
        ahorro_inicial=ahorro_inicial,
        ahorro_anual=ahorro_anual,
        porcentaje_financiacion=porcentaje_financiacion / 100,
        interes_hipoteca=interes_hipoteca,
        duracion_hipoteca=duracion_hipoteca,
        revalorizacion_anual=revalorizacion_anual,
        incremento_cashflow=incremento_cashflow,
        incremento_ahorro=incremento_ahorro,
        saldo_minimo=saldo_minimo,
        alquier_medio_mes=alquiler_medio_mes,
        gastos_medios_mes=gastos_medios_mes
    )

    st.subheader("Resultados Simulación Escenario 1")
    st.dataframe(df_resultados)
    st.line_chart(df_resultados.set_index("Año")["Patrimonio Neto (€)"])
