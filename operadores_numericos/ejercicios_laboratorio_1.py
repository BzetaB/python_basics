def pregunta_1(arista:float):
    
    volumen = 1/4 * (15 + 7 * (5 ** 0.5)) * arista ** 3

    return round(volumen, 3)

def pregunta_2(lado1: float, lado2: float, lado3: float, lado4: float):
    
    semiperimetro = (lado1 + lado2 + lado3 + lado4) / 2
    area = ((semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3) * (semiperimetro - lado4)) ** 0.5
    
    return round(area, 3)


def pregunta_3(numero:int):
    
    primer_digito = numero // 100
    segundo_digito = (numero % 100) // 10
    tercer_digito = numero % 10

    if(primer_digito == segundo_digito and segundo_digito == tercer_digito):
        return ("Tiene tres digitos iguales")
    elif(primer_digito != segundo_digito and segundo_digito != tercer_digito and primer_digito != tercer_digito):
        return ("Tiene tres digitos diferentes")
    else:
        return ("Tiene solo dos digitos iguales")


def pregunta_4(rango:int):
    if(rango <= 69):
        return "Deficiente"
    elif(rango <=79):
        return "Inferior"
    elif(rango <=89):
        return "Abajo del Promedio"
    elif(rango <= 109):
        return "Promedio"
    elif(rango <=119):
        return "Arriba del Promedio"
    elif(rango <=129):
        return "Superior"
    else:
        return "Muy Superior"
