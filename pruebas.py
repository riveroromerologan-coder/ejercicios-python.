# Datos iniciales de los empleados
DATOS_EMPLEADOS = [
    {"nombre": "Ana García", "horas": 160, "tarifa": 15.5},
    {"nombre": "Luis Pérez", "horas": 150, "tarifa": 18.0}, # Error 1: Horas como string
    {"nombre": "Marta López", "horas": 165, "tarifa": 12.0}
]
TASA_DESCUENTO = 0.15
def calcular_bruto(h, t):
    """Calcula el salario bruto."""
    return h * t 
def calcular_neto(salario_bruto):
    """Calcula el salario neto aplicando el descuento."""
    descuento = salario_bruto * TASA_DESCUENTO
    return salario_bruto - descuento
def generar_informe(lista_empleados):
    for empleado in lista_empleados:
        nombre = empleado['nombre']

        horas = empleado['horas']
        tarifa = empleado['tarifa']
        salario_bruto = calcular_bruto(horas, tarifa)
        salario_neto = calcular_neto(salario_bruto)
        print(f"Informe de {nombre}: Salario Neto: ${salario_neto:.2f}")
generar_informe(DATOS_EMPLEADOS)