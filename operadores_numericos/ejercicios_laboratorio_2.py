from math import pi

def pregunta_1(radio: float, angulo: float):
    """
    Realice una funcion que reciba como parametros dos numeros reales: el radio de una circunferencia y un angulo en grados sexagesimales. La funcion debe calcular la longitud
    del arco que corresponde a ese angulo, utilizando la siguiente formula:
    L = r · θ · π/180
    """
    longitud_arco = radio * angulo * (pi /180)

    return round(longitud_arco, 2)


def pregunta_2(coordenada_x : float, coordenada_y: float, coordenada_z: float):
    """
    Implemente una funcion para calcular el modulo de un vector en 3 dimensiones
    Modulo del Vector = Raiz cuadrada de la suma de las coordenadas cada uno elevado al cuadrado.
    """
    modulo_vector = (coordenada_x **2 + coordenada_y **2 + coordenada_z **2)**0.5

    return round(abs(modulo_vector),2)

def pregunta_3(edad: int):
    """
    Crea una funcion que clasifique la edad de una persona segun los siguientes criterios:
    • Si la edad es menor a 13: "Menor"
    • Si la edad es mayor o igual a 13 y menor a 18: "Adolescente"
    • Si la edad es mayor o igual a 18 y menor a 65: "Adulto"
    • Si la edad es mayor o igual a 65: "Adulto Mayor"
    Resuelva la funcion bajo el supuesto que el usuario ingresara siempre una edad valida,
    en el rango de 0 - 120.
    """
    if(edad < 13):
        return "Menor"
    elif(edad < 18):
        return "Adolescente"
    elif(edad < 65):
        return "Adulto"
    else:
        return "Adulto Mayor"   

def pregunta_4(peso: int, altura: float):
    """
    Desarrolle una funcion que calcule el Indice de Masa Corporal (IMC) a partir del peso
    y la altura de una persona, y clasifique el resultado en una de las siguientes categorias
    segun la OMS:
    • Utilizar la formula del IMC: IMC = peso / (altura * altura).
    • Evaluar el IMC con estructuras condicionales:
     Si el IMC es menor a 18.5, retornar "Bajo peso".
     Si el IMC esta desde 18.5 y menos de 25, retornar "Normal".
     Si el IMC esta desde 25 y menos de 30, retornar "Sobrepeso".
     Si el IMC es mayor o igual a 30, retornar "Obesidad".

    """
    imc = peso / (altura ** 2)
    if (imc < 18.5):
        return "Bajo peso"
    elif (imc < 25):
        return "Normal"
    elif (imc < 30):
        return "Sobrepeso"
    else:
        return "Obesidad"
