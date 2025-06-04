import streamlit as st

st.set_page_config(page_title="Simulador Inversión Inmobiliaria", layout="wide")

st.title("📊 Simulador de Inversión Inmobiliaria a Largo Plazo")
st.markdown("""
Este simulador te permite analizar distintos **escenarios de inversión** en vivienda para alquiler y evolución del patrimonio durante 30 años.
Puedes ajustar los parámetros en la barra lateral y comparar el rendimiento neto acumulado.
""")

# Barra lateral con parámetros básicos
st.sidebar.header("Parámetros Generales")
años = st.sidebar.slider("Años a simular", min_value=10, max_value=40, value=30)
interes_hipoteca = st.sidebar.selectbox("Interés hipotecario (%)", [2.5, 3.0], index=1)
porcentaje_financiacion = st.sidebar.selectbox("Porcentaje financiado (%)", [70, 80], index=0)
duracion_hipoteca = st.sidebar.selectbox("Duración hipoteca (años)", [20, 25, 30], index=2)

# Mensajes informativos
st.info("🔧 Funcionalidades avanzadas en desarrollo: escenarios múltiples, reinversión, estrategia óptima, revalorización, impuestos...")
st.success("✅ Esta es una versión inicial del simulador. El análisis detallado se irá completando.")
