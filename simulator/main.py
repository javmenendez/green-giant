from scenario1 import simular_escenario_1
import streamlit as st
import pdb  # Python debugger

# Enable debug mode
DEBUG = True

def debug_breakpoint():
    if DEBUG:
        pdb.set_trace()

st.sidebar.header("Parámetros Generales")
años = st.sidebar.slider("Años a simular", min_value=10, max_value=40, value=30)
interes_hipoteca = st.sidebar.selectbox("Interés hipotecario (%)", [2.5, 3.0], index=1) / 100
porcentaje_financiacion = st.sidebar.selectbox("Porcentaje financiado (%)", [70, 80], index=0)
duracion_hipoteca = st.sidebar.selectbox("Duración hipoteca (años)", [20, 25, 30], index=2)

st.sidebar.header("Parámetros específicos Escenario 1")
precio_piso_inicial = st.sidebar.number_input("Precio inicial por piso (€)", value=115000)
gastos_compra_inicial = st.sidebar.number_input("Gastos compra inicial por piso (€)", value=15000)
ahorro_anual = st.sidebar.number_input("Ahorro anual total (€)", value=15000)
revalorizacion_anual = st.sidebar.slider("Revalorización anual (%)", min_value=0.0, max_value=10.0, value=2.0) / 100
incremento_ahorro = st.sidebar.slider("Incremento anual ahorro (%)", min_value=0.0, max_value=10.0, value=2.0) / 100
saldo_minimo = st.sidebar.number_input("Saldo mínimo en cuenta (€)", value=20000)
alquiler_medio_mes = st.sidebar.number_input("Alquiler medio al mes (€)", value=900)
gastos_medios_anuales = st.sidebar.number_input("Gastos medios al año (€)", value=5000)
limite_numero_pisos = st.sidebar.slider("Límite número pisos (€)", min_value=3, max_value=30,value=10)


if st.sidebar.button("Simular Escenario 1"):
    
    try:
        
        df_resultados = simular_escenario_1(
            años=años,
            precio_piso_inicial=precio_piso_inicial,
            gastos_compra_inicial=gastos_compra_inicial,
            ahorro_anual=ahorro_anual,
            porcentaje_financiacion=porcentaje_financiacion / 100,
            interes_hipoteca=interes_hipoteca,
            duracion_hipoteca=duracion_hipoteca,
            revalorizacion_anual=revalorizacion_anual,
            incremento_ahorro=incremento_ahorro,
            saldo_minimo=saldo_minimo,
            alquiler_medio_mes=alquiler_medio_mes,
            gastos_medios_anuales=gastos_medios_anuales,
            limite_numero_pisos=limite_numero_pisos
        )
        
        st.subheader("Resultados Simulación Escenario 1")
        st.dataframe(df_resultados)
        
        # Convert all monetary columns from formatted strings to numbers
        df_chart = df_resultados.copy()
        columns_to_plot = [
            "Patrimonio Neto (€)",
            "Patrimonio sin invertir (€)",
            "+5% anual (€)",
            "+10% anual (€)",
            "+15% anual (€)",
            "+20% anual (€)"
        ]
        
        for col in columns_to_plot:
            df_chart[col] = df_chart[col].str.replace(".", "").astype(float)
        
        # Create the multi-line chart
        st.line_chart(
            df_chart.set_index("Año")[columns_to_plot],
            use_container_width=True
        )
        
    except Exception as e:
        
        st.error(f"Error en la simulación: {str(e)}")
        raise  # Re-raise the exception to see the full traceback
