from modulos import funciones_adivina_computadora as fac

conjunto_numeros = [1,2,3,4,5,6,7,8,9]


combinaciones = fac.crear_combinaciones(conjunto_numeros)
print(f"Combinaciones Iniciales: {combinaciones}")
adivinar = False
while adivinar == False:
    print("Combinación propuesta por la computadora = " + combinaciones[0])
    coincidencias = int(input("Cuántas coincidencias en valor y posición existen? [Elige entre los números 0 - 1 - 2 - 3]: "))

    if coincidencias == len(combinaciones[0]):
        adivinar = True
    else:
        combinaciones = fac.hallar_combinaciones_posibles(combinaciones,combinaciones[0],coincidencias)
        print(f"Filtrado {combinaciones}")      
        print(f"Lenght = {len(combinaciones)}")
                        