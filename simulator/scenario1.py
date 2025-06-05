import pandas as pd

def simular_escenario_1(
    años=30,
    precio_piso_inicial=115000,
    cashflow_inicial=2750,
    coste_inversion=50000,
    ahorro_inicial=20000,
    ahorro_anual=25000,  
    porcentaje_financiacion=0.7,
    interes_hipoteca=0.03,
    duracion_hipoteca=30,
    revalorizacion_anual=0.02,
    incremento_cashflow=0.02,
    incremento_ahorro=0.02,
    saldo_minimo=20000,
    alquiler_medio_mes=900,
    gastos_medios_mes=450,
):
    """
    Simulación del Escenario 1: compra continua de pisos con ahorro y reinversión
    """

    # Estado inicial
    pisos_comprados = 3
    deuda_total = (precio_piso_inicial * porcentaje_financiacion) * pisos_comprados
    ahorro = ahorro_inicial
    patrimonio = precio_piso_inicial * pisos_comprados - deuda_total + ahorro
    cashflow_anual = cashflow_inicial * pisos_comprados
    flujo_de_caja = 0
    total_invertido = coste_inversion * pisos_comprados 
    alquiler_anual = alquiler_medio_mes * 12 * pisos_comprados
    gastos_anuales = gastos_medios_mes * 12 * pisos_comprados
    beneficio_anual = alquiler_anual - gastos_anuales

    # Data para resultados
    datos = []

    datos.append({
            "Año": 0,
            "Pisos": pisos_comprados,
            "Total Invertido (€)": formatear_precio(total_invertido),
            "Cashflow Anual (€)": formatear_precio(cashflow_anual),
            "Ahorro (€)": formatear_precio(ahorro),
            "Deuda Hipotecaria (€)": formatear_precio(deuda_total),
            "Patrimonio Neto (€)": formatear_precio(patrimonio),
            "Pago Hipoteca Anual (€)": formatear_precio(calcular_pago_hipoteca(precio_piso_inicial, porcentaje_financiacion, interes_hipoteca, duracion_hipoteca) * pisos_comprados),
            # "Flujo de Caja (€)": formatear_precio(flujo_de_caja)
            "Precio Piso (€/ud)": formatear_precio(precio_piso_inicial),
            "Alquiler Anual (€)": formatear_precio(alquiler_anual),
            "Gastos Anuales (€)": formatear_precio(gastos_anuales),
            "Beneficio Anual (€)": formatear_precio(beneficio_anual),
           
    })


    for año in range(1, años + 1):
        # Revalorización precios y cashflow
        precio_piso_actual = precio_piso_inicial * ((1 + revalorizacion_anual) ** año)
        coste_inversion_actual = coste_inversion * ((1 + revalorizacion_anual) ** año)
        cashflow_actual = cashflow_inicial * ((1 + incremento_cashflow) ** año) * pisos_comprados
        ahorro_anual_actual = ahorro_anual * ((1 + incremento_ahorro) ** año)

        # Flujo de caja: sumamos cashflow y ahorro anual, restamos pagos hipoteca (simplificado)
        # Aquí se puede detallar el pago anual de hipoteca con fórmula financiera
        pago_hipoteca_anual = calcular_pago_hipoteca(precio_piso_actual, porcentaje_financiacion, interes_hipoteca, duracion_hipoteca) * pisos_comprados

        flujo_de_caja = cashflow_actual + ahorro_anual_actual - pago_hipoteca_anual

        # Actualizamos ahorro (dejando saldo mínimo)
        ahorro += flujo_de_caja
        if ahorro > saldo_minimo + coste_inversion_actual:
            # Se compra nuevo piso y se descuenta coste inversión y financiación
            pisos_comprados += 1
            deuda_total += precio_piso_actual * porcentaje_financiacion - coste_inversion_actual
            ahorro -= (precio_piso_actual * porcentaje_financiacion - coste_inversion_actual)

        # Actualizamos patrimonio neto
        patrimonio = precio_piso_actual * pisos_comprados - deuda_total + ahorro

        datos.append({           
            "Año": año,
            "Pisos": pisos_comprados,
            "Total Invertido (€)": formatear_precio(total_invertido),
            "Cashflow Anual (€)": formatear_precio(cashflow_anual),
            "Ahorro (€)": formatear_precio(ahorro),
            "Deuda Hipotecaria (€)": formatear_precio(deuda_total),
            "Patrimonio Neto (€)": formatear_precio(patrimonio),
            "Pago Hipoteca Anual (€)": formatear_precio(calcular_pago_hipoteca(precio_piso_inicial, porcentaje_financiacion, interes_hipoteca, duracion_hipoteca) * pisos_comprados),
            # "Flujo de Caja (€)": formatear_precio(flujo_de_caja)
            "Precio Piso (€/ud)": formatear_precio(precio_piso_inicial),
            "Alquiler Anual (€)": formatear_precio(alquiler_anual),
            "Gastos Anuales (€)": formatear_precio(gastos_anuales),
            "Beneficio Anual (€)": formatear_precio(beneficio_anual),
        })

    return pd.DataFrame(datos)

def calcular_pago_hipoteca(precio, porcentaje_financiacion, interes, duracion):
    """
    Calcula el pago anual fijo de la hipoteca usando fórmula de amortización francesa
    precio: precio del piso
    porcentaje_financiacion: 0.7 o 0.8
    interes: tipo de interés anual decimal (0.03)
    duracion: años hipoteca
    """
    importe_financiado = precio * porcentaje_financiacion
    i = interes
    n = duracion

    pago_anual = importe_financiado * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
    return pago_anual

def formatear_precio(cantidad):
    """
    Formatea un número como precio sin decimales y con puntos para separar los miles.
    Ejemplo: 1234567.89 -> "1.234.568"
    """
    return f"{int(round(cantidad, 0)):_.0f}".replace("_", ".")

