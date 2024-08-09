def generar_meses_validos(anio):
    meses_validos = {}
    for mes in range(1, 13):
        mes_str = str(mes).zfill(2)
        base_periodo = int(f"{anio}{mes_str}")
        # Generar las 5 planillas válidas para cada mes
        meses_validos[base_periodo] = [base_periodo + i * 20 for i in range(5)]
    return meses_validos

# Ejemplo de uso para el año 2024
meses_validos_2024 = generar_meses_validos(2025)
for mes, periodos in meses_validos_2024.items():
    print(f"{mes}: {periodos}")
