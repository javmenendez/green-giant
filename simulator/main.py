import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Simulador Inversión Inmobiliaria", layout="wide")

def simular_inversion(años, interes, porcentaje_financiacion, duracion_hipoteca):
    # Aquí va la lógica real, pero para mostrar el ejemplo hacemos un DataFrame ficticio
    data = {
        "Año": list(range(1, años + 1)),
        "Patrimonio (€)": np.cumsum(np.random.normal(5000, 1000, años)).round(2),
        "Cashflow (€)": np.linspace(2750, 2750 * 1.05 ** años, años).round(2),
    }
    return pd.DataFrame(data)

st.title("📊 Simulador de Inversión Inmobiliaria a Largo Plazo")

# Barra lateral con parámetros básicos
st.sidebar.header("Parámetros Generales")
años = st.sidebar.slider("Años a simular", min_value=10, max_value=40, value=30)
interes_hipoteca = st.sidebar.selectbox("Interés hipotecario (%)", [2.5, 3.0], index=1)
porcentaje_financiacion = st.sidebar.selectbox("Porcentaje financiado (%)", [70, 80], index=0)
duracion_hipoteca = st.sidebar.selectbox("Duración hipoteca (años)", [20, 25, 30], index=2)

if st.button("Simular"):
    resultados = simular_inversion(años, interes, porcentaje_financiacion, duracion_hipoteca)
    st.write("### Resultados de la simulación")
    st.dataframe(resultados)
    st.line_chart(resultados.set_index("Año")[["Patrimonio (€)", "Cashflow (€)"]])

