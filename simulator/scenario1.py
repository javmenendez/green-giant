import pandas as pd

def simular_escenario_1(
    años=30,
    precio_piso_inicial=115000,
    cashflow_inicial=2750,
    coste_inversion=50000,
    ahorro_inicial=20000,
    ahorro_anual=25000 * 2,  # dos titulares
    porcentaje_financiacion=0.7,
    interes_hipoteca=0.03,
    duracion_hipoteca=30,
    revalorizacion_anual=0.02,
    incremento_cashflow=0.02,
    incremento_ahorro=0.02,
    saldo_minimo=20000,
):
    """
    Simulación del Escenario 1: compra continua de pisos con ahorro y reinversión
    """

    # Estado inicial
    pisos_comprados = 3
    deuda_total = (precio_piso_inicial * porcentaje_financiacion - coste_inversion) * pisos_comprados
    ahorro = ahorro_inicial
    patrimonio = precio_piso_inicial * pisos_comprados - deuda_total + ahorro
    cashflow_anual = cashflow_inicial * pisos_comprados
    flujo_de_caja = 0

    # Data para resultados
    datos = []

    resultados.append({
         "Año": 0,
            "Pisos": pisos_comprados,
            "Precio Piso (€/ud)": round(precio_piso_inicial, 2),
            "Cashflow Anual (€)": round(cashflow_anual, 2),
            "Ahorro (€)": round(ahorro, 2),
            "Deuda Hipotecaria (€)": round(deuda_total, 2),
            "Patrimonio Neto (€)": round(patrimonio, 2),
            "Pago Hipoteca Anual (€)": round(calcular_pago_hipoteca(precio_piso_actual, porcentaje_financiacion, interes_hipoteca, duracion_hipoteca) * pisos_comprados, 2),
            "Flujo de Caja (€)": round(flujo_de_caja, 2)
    })


    for año in range(1, años + 1):
        # Revalorización precios y cashflow
        precio_piso_actual = precio_piso_inicial * ((1 + revalorizacion_anual) ** año)
        cashflow_actual = cashflow_inicial * ((1 + incremento_cashflow) ** año) * pisos_comprados
        ahorro_anual_actual = ahorro_anual * ((1 + incremento_ahorro) ** año)

        # Flujo de caja: sumamos cashflow y ahorro anual, restamos pagos hipoteca (simplificado)
        # Aquí se puede detallar el pago anual de hipoteca con fórmula financiera
        pago_hipoteca_anual = calcular_pago_hipoteca(precio_piso_actual, porcentaje_financiacion, interes_hipoteca, duracion_hipoteca) * pisos_comprados

        flujo_de_caja = cashflow_actual + ahorro_anual_actual - pago_hipoteca_anual

        # Actualizamos ahorro (dejando saldo mínimo)
        ahorro += flujo_de_caja
        if ahorro > saldo_minimo:
            # Se compra nuevo piso y se descuenta coste inversión y financiación
            pisos_comprados += 1
            deuda_total += precio_piso_actual * porcentaje_financiacion - coste_inversion
            ahorro -= (precio_piso_actual * porcentaje_financiacion - coste_inversion)

        # Actualizamos patrimonio neto
        patrimonio = precio_piso_actual * pisos_comprados - deuda_total + ahorro

        datos.append({
            "Año": año,
            "Pisos": pisos_comprados,
            "Precio Piso (€/ud)": round(precio_piso_actual, 2),
            "Cashflow Anual (€)": round(cashflow_actual, 2),
            "Ahorro (€)": round(ahorro, 2),
            "Deuda Hipotecaria (€)": round(deuda_total, 2),
            "Patrimonio Neto (€)": round(patrimonio, 2),
            "Pago Hipoteca Anual (€)": round(pago_hipoteca_anual, 2),
            "Flujo de Caja (€)": round(flujo_de_caja, 2)
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

