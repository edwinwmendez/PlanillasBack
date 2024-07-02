import random

def generar_insert(contrato_id, transaccion_id, monto_min, monto_max, periodo_inicial, periodo_final, estado):
    monto = round(random.uniform(monto_min, monto_max), 2)
    return f"({contrato_id}, {transaccion_id}, {monto}, '{periodo_inicial}', '{periodo_final}', {estado})"

def generar_sql_inserts():
    contratos_ids = range(1, 126)
    transacciones_ids = {
        "haberes": 1,
        "bonificaciones": 2,
        "descuentos": 5,
        "aportes": 4
    }

    sql_haberes = "INSERT INTO transacciones_trabajadores (contrato_id, transaccion_id, monto, periodo_inicial, periodo_final, estado)\nVALUES\n"
    sql_bonificaciones = "INSERT INTO transacciones_trabajadores (contrato_id, transaccion_id, monto, periodo_inicial, periodo_final, estado)\nVALUES\n"
    sql_descuentos = "INSERT INTO transacciones_trabajadores (contrato_id, transaccion_id, monto, periodo_inicial, periodo_final, estado)\nVALUES\n"
    sql_aportes = "INSERT INTO transacciones_trabajadores (contrato_id, transaccion_id, monto, periodo_inicial, periodo_final, estado)\nVALUES\n"

    haberes_values = []
    bonificaciones_values = []
    descuentos_values = []
    aportes_values = []

    for contrato_id in contratos_ids:
        haberes_values.append(generar_insert(contrato_id, transacciones_ids["haberes"], 1400, 1700, "202406", "202412", 1))
        bonificaciones_values.append(generar_insert(contrato_id, transacciones_ids["bonificaciones"], 200, 300, "202406", "202412", 1))
        descuentos_values.append(generar_insert(contrato_id, transacciones_ids["descuentos"], 100, 200, "202406", "202412", 1))
        aportes_values.append(generar_insert(contrato_id, transacciones_ids["aportes"], 300, 400, "202406", "202412", 1))

    sql_haberes += ",\n".join(haberes_values) + ";\n"
    sql_bonificaciones += ",\n".join(bonificaciones_values) + ";\n"
    sql_descuentos += ",\n".join(descuentos_values) + ";\n"
    sql_aportes += ",\n".join(aportes_values) + ";\n"

    return sql_haberes, sql_bonificaciones, sql_descuentos, sql_aportes

if __name__ == "__main__":
    sql_haberes, sql_bonificaciones, sql_descuentos, sql_aportes = generar_sql_inserts()
    with open("insert_transacciones.sql", "w") as file:
        file.write("-- Insertar haberes\n")
        file.write(sql_haberes)
        file.write("\n-- Insertar bonificaciones\n")
        file.write(sql_bonificaciones)
        file.write("\n-- Insertar descuentos\n")
        file.write(sql_descuentos)
        file.write("\n-- Insertar aportes\n")
        file.write(sql_aportes)

    print("Archivo SQL generado con éxito.")
