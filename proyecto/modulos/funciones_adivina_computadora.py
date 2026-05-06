def crear_combinaciones(conjunto_numeros:list[int]):

    #Recibo como pámetros el conjunto de números que puede tomar cada dígito.
    #Recibo 3 listas: Una para cada dígito

    """
    Mi función realizará todas las combinaciones de 3 digitos, en donde ninguno de los dígitos de la combinación pueden coincidir entre sí.
    La lógica aplicada es:
        Por cada dígito del conjunto de número del primer digito, concateno los  otros dos dígitos diferentes, los cuales obtendré (cada uno) recorriendo el conjunto nuevamente por cada dígito. Para realizar la combinación creo una condicional que solo se cumple cuando los digitos son diferentes entre sí.
        Al final, retorno todas las combinaciones posibles en una lista.
    """

    combinaciones = [] # Creo mi lista para guardar las combinaciones de dígitos posibles
    for digito1 in conjunto_numeros:
        for digito2 in conjunto_numeros:
            for digito3 in conjunto_numeros:
                if digito1 != digito2 and digito1 != digito3 and digito2 != digito3: # Valido que los dígitos de la combinación no coincidan
                    combinaciones.append(f"{digito1}{digito2}{digito3}") # Concateno la combinación de tres dígitos
    return combinaciones # Retorno mi lista de combinaciones



def hallar_combinaciones_posibles(combinaciones:list[int], intento_combinacion_computadora:int, coincidencias:int):

    """
    Recibo como parámetros:
    - La lista de combinaciones: Será mis combinaciones iniciales
    - El intento de combinación que realiza la computadora
    - El número de coincidencias en valor y posición que nos da como información el usuario en cada intento.
    """

    """
    Mi función recorrerá cada combinación de la lista de combinaciones iniciales y luego evaluará, con mi función contar_coincidencias, si la combinación tiene la misma cantidad de coincidencias que me dice el usuario.
    """

    posibilidades_coincistentes = []

    for combinacion in combinaciones:
        if contar_coincidencias(combinacion, intento_combinacion_computadora) == coincidencias:
            posibilidades_coincistentes.append(combinacion)
    
    return posibilidades_coincistentes


def contar_coincidencias(combinacion: int, intento_combinacion_computadora:int):

    """
    Recibo como parámetros:
    - Una combinación hecha con 3 número del cojunto.
    - El intento de combinación que trata de adivinar la computadora
    """

    """
    Mi función verificará cuántas coincidencias existen entre una combinación y la combinación propuesta por la computadora.
    La lógica aplicada es:
        Recorrer n vueltas donde n es igual a la cantidad de dígitos que tiene la combinación, en este caso por los 3 digitos realiizará 3 vueltas. Además, si encuentro una coincidencia entre el digito de la combinación y el digito del intento de la computadora, en la posición evaluada de la vuelta del bucle, entonces registro que tengo una coincidencia.
        Al final, habiendo recorrida cada posición de la combinación, retorno el total de coincidencias encontradas en valor y posición de las combinaciones evaluadas.
    """

    total_coincidencias = 0 #Variable para almacenar las coincidencias encontradas

    for i in range(len(combinacion)): # Recorro n vueltas donde n es igual a la longitud de caracteres de combinacion
        if intento_combinacion_computadora[i] == combinacion[i]:
            total_coincidencias += 1
    return total_coincidencias
