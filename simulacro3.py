# Ejercicio 1 – Clasificación de edad:
# Escribí una función que reciba la edad de una persona (número entero) y devuelva una clasificación según el siguiente criterio:

# Si es menor de 18:

    # Si tiene menos de 13: “Niño/a”

    # Si tiene entre 13 y 17: “Adolescente”

# Si tiene 18 o más:

    # Si tiene menos de 60: “Adulto/a”

    # Si tiene 60 o más: “Adulto/a mayor”
    
def edadPersona(edad):
    
    cartel =""
    if edad.isdigit():
        edad = int(edad)
        if edad >=0 and edad < 18:
            if edad < 13:
                cartel = "ninio/a"
            elif edad >=13 or edad <= 17:
                cartel = "Adolescente"
        elif edad > 18 and edad <=120:
            if edad >= 18 and edad < 60:
                cartel = "Adulto/a"
            elif edad >= 60:
                cartel = "Adulto Mayor"
        else:
            cartel = "Edad Invalidad"
    else:
        cartel = "El dato ingresado no es numerico"
    return cartel
print(edadPersona("2"))    

            
#######################################################################################################
# Ejercicio 2 – Evaluación de inscripción a curso
# Escribí una función que reciba nombre, edad y nivel de una persona, y evalúe si puede inscribirse a un curso.

# Las reglas son:

    # Si el nivel es "básico":

        # Puede inscribirse si tiene 10 años o más.

    # Si el nivel es "intermedio":

        # Puede inscribirse si tiene 15 años o más.

    # Si el nivel es "avanzado":

        # Puede inscribirse si tiene 18 años o más.

# Si no cumple los requisitos, la función debe devolver un mensaje que diga:
# "[nombre] no puede inscribirse al nivel [nivel]"
# En caso contrario:
# "[nombre] puede inscribirse al nivel [nivel]"

#######################################################################################################
# Ejercicio 3 – Cálculo de precio final con descuentos
# Escribí una función que reciba tres parámetros:

# producto (str): nombre del producto,

# precio_unitario (float): precio por unidad,

# cantidad (int): cantidad de unidades a comprar.

# La función debe calcular el precio total y aplicar el siguiente descuento:

# Si compra 3 o más unidades, se aplica un 10% de descuento.

# Si compra 5 o más, el descuento es del 20%.

# Finalmente, debe devolver un único mensaje indicando:

# "El total a pagar por [cantidad] [producto](s) es: $[importe]"

# Si el precio o la cantidad es menor o igual a cero, devolver: "Datos inválidos".

#######################################################################################################
#######################
#       DESAFIO
#######################
# Clasificación múltiple de números
# Escribí una función que reciba tres números enteros distintos y devuelva un mensaje indicando:

# Cuál es el mayor, el menor, y cuál quedó en el medio.

# Además, indicar si el mayor es par y si el menor es negativo.

#Salida esperada: "Mayor: 20 (par), Medio: 5, Menor: -3 (negativo)"
