# Consigna 1:
# Explica brevemente qué es un algoritmo y cómo se relaciona con la programación.

#Son pasos finitos, resolver una tarea especifica. 



# Consigna 2:
# Desarrollá una función en Python que reciba como entrada el año de nacimiento de una persona y devuelva su edad actual 
# (considerando que estamos en 2025). Si la edad calculada es menor a 0, debe devolver un mensaje de error.

def anioNacimiento(anio):
    anio_actual = 2025
    edad = anio_actual - anio
    mensaje = ""
    
    if(edad >= 0):
        mensaje = edad
    else:
        mensaje = "Error"
    return mensaje
    
#Funcion Test años

assert(anioNacimiento(1990) == 35)
assert(anioNacimiento(2025) == 0)
assert(anioNacimiento(2027) == "Error")
print("Paso todos los test")
    
def naci(anio):
    calculo= 2025 - anio
    if calculo >= 0:
        resultado= f"tenes {calculo} años"
    else:
        resultado= "error"
    return resultado


assert(naci(1990) == f"tenes 35 años")
assert(naci(2025) == f"tenes 0 años")
assert(naci(2027) == "error")
print("Paso todos los test!!!!!!!")

# Consigna 3:
# Creá una función que reciba como parámetro el nombre de una persona y la hora actual (número entero del 0 al 23).
# La función debe devolver un saludo personalizado según la hora:

# De 6 a 12: “Buen día, [nombre]”

# De 13 a 19: “Buenas tardes, [nombre]”

# De 20 a 5: “Buenas noches, [nombre]”

# Si la hora no está en el rango 0–23, debe devolver “Hora inválida”.

def saludo(nombre, hora):
    respuesta=""
    if(hora >=6 and hora <=12):
        respuesta = f"Buen dia, {nombre}"
    elif(hora >= 13 and hora <=19):
        respuesta = f"Buenas tardes, {nombre}"
    elif((hora >= 20 and hora <=23) or (hora >=0 and hora <=5)):
        respuesta = f"Buenas noches, {nombre}"
    else:
        respuesta = "Hora inválida"
    return respuesta

assert(saludo("Juan",5)== "Buenas noches, Juan")
assert(saludo("Pedro", 8)== "Buen dia, Pedro")
assert(saludo("Maria",17)== "Buenas tardes, Maria")
assert(saludo("Marta", 25)== "Hora inválida")    
print("Paso el saludo!!")

#Consigna 4
# Creá una función que reciba un nombre y un número entero.
# La función debe imprimir ese nombre la cantidad de veces indicada por el número recibido.

# Consigna 5
# Escribí una función que reciba una cadena de texto y devuelva cuántas letras tiene, sin contar espacios.

# Consigna 6
# Desarrollá una función que reciba dos números y devuelva el resultado de su división.
# Si el segundo número es cero, debe devolver un mensaje que diga “No se puede dividir por cero”.



def comparar(numero1, numero2):
    cartel =""
    if (numero1 == numero2):
        cartel = "Iguales"
    elif(numero1 != numero2):
        cartel = "Distintos"
    elif(numero1 > numero2):
        cartel = "Numero 1 mayor a Numero 2"
    elif(numero1 < numero2):
        cartel = "Numero 1 menor a Numero 2"
    return cartel

assert(comparar(1,1)=="Iguales")
assert(comparar(1,2)=="Distintos")
assert(comparar(8,1)=="Numero 1 mayor a Numero 2")
assert(comparar(1,7)=="Numero 1 menor a Numero 2")
print("Pasamos los test de comparar")

