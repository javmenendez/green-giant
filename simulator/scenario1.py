import pandas as pd

def simular_escenario_1(
    años=30,
    precio_piso_inicial=115000,
    gastos_compra_inicial=15000,
    ahorro_anual=25000,  
    porcentaje_financiacion=0.7,
    interes_hipoteca=0.03,
    duracion_hipoteca=25,
    revalorizacion_anual=0.02,
    incremento_ahorro=0.02,
    saldo_minimo=20000,
    alquiler_medio_mes=900,
    gastos_medios_anuales=5000,
    limite_numero_pisos=10
):
    """
    Simulación del Escenario 1: compra continua de pisos con ahorro y reinversión ()
    """

    # Estado inicial
    pisos_comprados = 3
    ahorro = ahorro_anual
    alquiler_anual = alquiler_medio_mes * 12 * pisos_comprados
    gastos_anuales = gastos_medios_anuales * pisos_comprados
    precio_entrada_total = (precio_piso_inicial + gastos_compra_inicial)
    # Data para resultados
    datos = []

    hipotecas = []

    # Añadir hipotecas
    hipotecas.append(Hipoteca("Hipoteca inicial 1", 115000, porcentaje_financiacion, duracion_hipoteca, interes_hipoteca, 0))
    hipotecas.append(Hipoteca("Hipoteca inicial 2", 115000, porcentaje_financiacion, duracion_hipoteca, interes_hipoteca, 0))
    hipotecas.append(Hipoteca("Hipoteca inicial 3", 115000, porcentaje_financiacion, duracion_hipoteca, interes_hipoteca, 0))

    capital, intereses = amortizacion_total_en_anio_base(hipotecas, anio_base=0)
    deuda_total = ((precio_piso_inicial * porcentaje_financiacion) * pisos_comprados) - capital
    total_invertido = ((precio_piso_inicial + gastos_compra_inicial) - (precio_piso_inicial * porcentaje_financiacion)) * pisos_comprados
    valor_pisos = precio_entrada_total * pisos_comprados
    cashflow_acumulado = alquiler_anual - gastos_anuales - intereses - capital;


    patrimonio_sin_invertir = total_invertido
    patrimonio_sin_invertir_beneficio_1 = total_invertido
    patrimonio_sin_invertir_beneficio_2 = total_invertido
    patrimonio_sin_invertir_beneficio_3 = total_invertido
    patrimonio_sin_invertir_beneficio_4 = total_invertido
    
    # print(f"Año base 0: Capital amortizado total: {capital} €, Intereses pagados total: {intereses} €")

    datos.append(crear_diccionario_datos(
        año=0,
        pisos_comprados=pisos_comprados,
        valor_pisos=valor_pisos,
        precio_entrada_total=precio_entrada_total,
        total_invertido=total_invertido,
        ahorro=ahorro,
        deuda_total=deuda_total,
        capital=capital,
        intereses=intereses,
        precio_piso=precio_piso_inicial,
        alquiler_anual=alquiler_anual,
        gastos_anuales=gastos_anuales,
        porcentaje_financiacion=porcentaje_financiacion,
        cashflow_acumulado=cashflow_acumulado,
        patrimonio_sin_invertir=patrimonio_sin_invertir,
        patrimonio_sin_invertir_beneficio_1=patrimonio_sin_invertir,
        patrimonio_sin_invertir_beneficio_2=patrimonio_sin_invertir,
        patrimonio_sin_invertir_beneficio_3=patrimonio_sin_invertir,
        patrimonio_sin_invertir_beneficio_4=patrimonio_sin_invertir,
        limite_numero_pisos=limite_numero_pisos
    ))

    for año in range(1, años + 1):

        precio_piso_actual = precio_piso_inicial * ((1 + revalorizacion_anual) ** año)
        precio_entrada_total_actual = precio_entrada_total * ((1 + revalorizacion_anual) ** año)
        coste_compra_piso = precio_entrada_total_actual - precio_piso_actual * porcentaje_financiacion

        if ahorro > (saldo_minimo + coste_compra_piso) and pisos_comprados < limite_numero_pisos:
            # Se compra nuevo piso y se descuenta coste inversión y financiación
            pisos_comprados += 1
            deuda_total += precio_piso_actual * porcentaje_financiacion
            ahorro -= coste_compra_piso
            total_invertido += precio_entrada_total_actual - (precio_piso_actual * porcentaje_financiacion)
            hipotecas.append(Hipoteca(f"Hipoteca {año}", precio_piso_actual, porcentaje_financiacion, duracion_hipoteca, interes_hipoteca, año))    
        
        # Revalorización precios y cashflow
        ahorro_anual_actual = ahorro_anual * ((1 + incremento_ahorro) ** año)
        gastos_anuales_actuales = gastos_medios_anuales * ((1 + revalorizacion_anual) ** año) * pisos_comprados
        alquiler_anual_actual = alquiler_medio_mes * ((1 + revalorizacion_anual) ** año) * 12 * pisos_comprados  
        valor_pisos = precio_entrada_total_actual * pisos_comprados 
       

        capital, intereses = amortizacion_total_en_anio_base(hipotecas, anio_base=año)
        # print(f"Año {año}: Capital amortizado total: {capital} €, Intereses pagados total: {intereses} €")
        deuda_total = deuda_total - capital
        cashflow_actual = alquiler_anual_actual - gastos_anuales_actuales - intereses - capital
        cashflow_acumulado += cashflow_actual

        # Actualizamos ahorro (dejando saldo mínimo)
        ahorro += cashflow_actual + ahorro_anual_actual

        patrimonio_sin_invertir += ahorro_anual_actual
        patrimonio_sin_invertir_beneficio_1 += ahorro_anual_actual + patrimonio_sin_invertir_beneficio_1 * 0.05
        patrimonio_sin_invertir_beneficio_2 += ahorro_anual_actual + patrimonio_sin_invertir_beneficio_2 * 0.1
        patrimonio_sin_invertir_beneficio_3 += ahorro_anual_actual + patrimonio_sin_invertir_beneficio_3 * 0.15
        patrimonio_sin_invertir_beneficio_4 += ahorro_anual_actual + patrimonio_sin_invertir_beneficio_4 * 0.20

        # print(f"Año {año}: Total invertido: {total_invertido} €")

        datos.append(crear_diccionario_datos(
            año=año,
            pisos_comprados=pisos_comprados,
            valor_pisos=valor_pisos,
            precio_entrada_total=precio_entrada_total_actual,
            total_invertido=total_invertido,
            ahorro=ahorro,
            deuda_total=deuda_total,
            capital=capital,
            intereses=intereses,
            precio_piso=precio_piso_actual,
            alquiler_anual=alquiler_anual_actual,
            gastos_anuales=gastos_anuales_actuales,
            porcentaje_financiacion=porcentaje_financiacion,
            cashflow_acumulado=cashflow_acumulado,
            patrimonio_sin_invertir=patrimonio_sin_invertir,
            patrimonio_sin_invertir_beneficio_1=patrimonio_sin_invertir_beneficio_1,
            patrimonio_sin_invertir_beneficio_2=patrimonio_sin_invertir_beneficio_2,
            patrimonio_sin_invertir_beneficio_3=patrimonio_sin_invertir_beneficio_3,
            patrimonio_sin_invertir_beneficio_4=patrimonio_sin_invertir_beneficio_4,
            limite_numero_pisos=limite_numero_pisos
        
        ))

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

def calcular_amortizacion_hipoteca(precio, porcentaje_financiacion, interes, duracion, año):
    """
    Calcula la cantidad de interés y capital amortizado para un año específico de la hipoteca.
    
    Args:
        precio: precio del piso
        porcentaje_financiacion: 0.7 o 0.8
        interes: tipo de interés anual decimal (0.03)
        duracion: años hipoteca
        año: año específico para el que queremos calcular (1 a duracion)
        
    Returns:
        tuple: (interes_anual, capital_anual) donde:
            - interes_anual: cantidad de interés pagado en el año especificado
            - capital_anual: cantidad de capital amortizado en el año especificado
    """
    if año < 1 or año > duracion:
        raise ValueError(f"El año debe estar entre 1 y {duracion}")
        
    importe_financiado = precio * porcentaje_financiacion
    i = interes
    n = duracion
    
    # Calculamos el pago anual total
    pago_anual = calcular_pago_hipoteca(precio, porcentaje_financiacion, interes, duracion)
    
    # Calculamos el capital pendiente al inicio del año especificado
    # Para el año 1, el capital pendiente es el importe financiado
    if año == 1:
        capital_pendiente = importe_financiado
    else:
        # Para años posteriores, calculamos el capital pendiente
        # usando la fórmula del capital pendiente en un préstamo francés
        capital_pendiente = importe_financiado * ((1 + i) ** n - (1 + i) ** (año - 1)) / ((1 + i) ** n - 1)
    
    # Calculamos el interés y capital para el año especificado
    interes_anual = capital_pendiente * i
    capital_anual = pago_anual - interes_anual
    
    return (interes_anual, capital_anual)

def formatear_precio(cantidad):
    """
    Formatea un número como precio sin decimales y con puntos para separar los miles.
    Ejemplo: 1234567.89 -> "1.234.568"
    """
    return f"{int(round(cantidad, 0)):_.0f}".replace("_", ".")

def amortizacion_total_en_anio_base(hipotecas, anio_base):
    total_capital = 0.0
    total_intereses = 0.0

    for h in hipotecas:
        datos = h.obtener_amortizacion_en_anio_base(anio_base)
        total_capital += datos["capital"]
        total_intereses += datos["intereses"]

    return round(total_capital, 2), round(total_intereses, 2)

def crear_diccionario_datos(
    año,
    pisos_comprados,
    valor_pisos,
    precio_entrada_total,
    total_invertido,
    ahorro,
    deuda_total,
    capital,
    intereses,
    precio_piso,
    alquiler_anual,
    gastos_anuales,
    porcentaje_financiacion,
    cashflow_acumulado,
    patrimonio_sin_invertir,
    patrimonio_sin_invertir_beneficio_1,
    patrimonio_sin_invertir_beneficio_2,
    patrimonio_sin_invertir_beneficio_3,
    patrimonio_sin_invertir_beneficio_4,
    limite_numero_pisos
):
    """
    Crea un diccionario con los datos formateados para un año específico de la simulación.
    Todos los valores monetarios deben ser números (no formateados).
    """
    # Calcular el porcentaje de retorno del cashflow
    cashflow_anual = alquiler_anual - gastos_anuales - intereses - capital
    cashflow_return_pct = (cashflow_anual / total_invertido * 100) if total_invertido > 0 else 0

    patrimonio_neto = valor_pisos - deuda_total

    if pisos_comprados >= limite_numero_pisos:
        patrimonio_neto += ahorro
        ahorro = 0;

    return {
        "Año": año,
        "Pisos": pisos_comprados,
        "Total Invertido (€)": formatear_precio(total_invertido),
        "Valor Pisos (€)": formatear_precio(valor_pisos),
        "Deuda Hipotecaria (€)": formatear_precio(deuda_total),
        "Patrimonio Neto (€)": formatear_precio(patrimonio_neto),
        "Alquiler Anual (€)": formatear_precio(alquiler_anual),
        "Gastos Anuales (€)": formatear_precio(gastos_anuales),
        "Hipoteca Intereses (€)": formatear_precio(intereses),
        "Hipoteca Capital Amortizado (€)": formatear_precio(capital),
        "Cashflow Anual (€)": formatear_precio(cashflow_anual),
        "Cashflow Return (%)": f"{cashflow_return_pct:.2f}%",
        "Cashflow Acumulado (€)": formatear_precio(cashflow_acumulado),
        "Precio Compra (€/ud)": formatear_precio(precio_piso),
        "Precio Compra + Gastos (€/ud)": formatear_precio(precio_entrada_total),
        "Ahorro para compra (€/ud)": formatear_precio(precio_entrada_total - precio_piso * porcentaje_financiacion),
        "Ahorro (€)": formatear_precio(ahorro),
        "Patrimonio sin invertir (€)": formatear_precio(patrimonio_sin_invertir),
        "+5% anual (€)": formatear_precio(patrimonio_sin_invertir_beneficio_1),
        "+10% anual (€)": formatear_precio(patrimonio_sin_invertir_beneficio_2),
        "+15% anual (€)": formatear_precio(patrimonio_sin_invertir_beneficio_3),
        "+20% anual (€)": formatear_precio(patrimonio_sin_invertir_beneficio_4)
    }

class Hipoteca:
    def __init__(self, nombre, monto_total, porcentaje_financiado, plazo_anios, interes_anual, anio_inicio):
        self.nombre = nombre
        self.monto_total = monto_total
        self.porcentaje_financiado = porcentaje_financiado
        self.plazo_anios = plazo_anios
        self.interes_anual = interes_anual
        self.anio_inicio = anio_inicio

        self.capital_prestado = monto_total * porcentaje_financiado
        self.interes_mensual = interes_anual / 12
        self.total_meses = plazo_anios * 12

        self.cuota_mensual = round(
            self.capital_prestado * self.interes_mensual / (1 - (1 + self.interes_mensual) ** -self.total_meses), 2
        )

        self.cuadro_anual = self._generar_cuadro_anual()

    def _generar_cuadro_anual(self):
        saldo_pendiente = self.capital_prestado
        cuadro = {}
        for mes in range(1, self.total_meses + 1):
            interes_mes = round(saldo_pendiente * self.interes_mensual, 10)
            amortizacion_mes = self.cuota_mensual - interes_mes
            saldo_pendiente -= amortizacion_mes

            anio = (mes - 1) // 12 + 1
            if anio not in cuadro:
                cuadro[anio] = {"capital": 0.0, "intereses": 0.0}
            cuadro[anio]["capital"] += amortizacion_mes
            cuadro[anio]["intereses"] += interes_mes

        # Redondear resultado por año
        for anio in cuadro:
            cuadro[anio]["capital"] = round(cuadro[anio]["capital"], 2)
            cuadro[anio]["intereses"] = round(cuadro[anio]["intereses"], 2)

        return cuadro

    def obtener_amortizacion_en_anio_base(self, anio_base):
        anio_relativo = anio_base - self.anio_inicio + 1
        if 1 <= anio_relativo <= self.plazo_anios:
            return self.cuadro_anual.get(anio_relativo, {"capital": 0.0, "intereses": 0.0})
        else:
            return {"capital": 0.0, "intereses": 0.0}
