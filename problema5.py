# problema 5 - Horas trabajadas por recurso
# estudiante: Diego Alejandro Rivero
# ingenieria de sistemas - UNAD

recursos = []

print("REGISTRO DE HORAS TRABAJADAS")
for i in range(4) :
    nombre = input("ingrese el nombre del recurso: ")
    lunes = float(input("horas del lunes: "))
    martes = float(input("horas del martes: "))
    miercoles = float(input("horas del miércoles: "))
    jueves = float(input("horas del jueves: "))
    viernes = float(input("horas del viernes: "))
    recursos.append([nombre, lunes, martes, miercoles, jueves, viernes ])

def calcular_jornada(matriz) :
    for recurso in matriz:
        total = sum(recurso[1 :])
        if total > 40:
            clasificación = "Sobretiempo"
        else:
            clasificación = "Horario estándar"

        print("Recurso:", recurso[0])
        print("Total de horas:", total)
        print("Clasificación:", clasificación)

calcular_jornada(recursos)



