#CONSIGNA 2
#Desarrollá una función en Python que reciba como entrada la edad de 3 personas y devuelva la 
#mayor edad de las tres. Si las 3 son iguales, la función debe devolver un mensaje indicándolo. 

#1 - Identificar el problema
#2 - Identificar los datos (Entradas que va a  recibir el programa)
#3 - En este caso 3 parametros numericos(Enteros)
#4 - Procesar los datos (En este caso usando condicionales)
#5 - Identificar las posibles soluciones
#6 - Retornar el mensaje

# Llego a lo mismo
# if(edad1 == edad2)and(edad1 == edad3) #Forma 1:
# if(edad1==edad2==edad3): #Forma 2

def comparar_edades(edad1,edad2,edad3):
    
    resultado = ""
    
    if(edad1==edad2==edad3): #TRUE/FALSE
        resultado = "Las edades ingresadas son iguales"
    elif(edad1 >= edad2) and (edad1 >= edad3):
        resultado = edad1
    elif(edad2 >= edad1) and (edad2 >= edad3):
        resultado = edad2
    else:
        resultado = edad3
    return resultado

#Test de la funcion
#print(comparar_edades(5,5,6) == "Las edades ingresadas son iguales") Muestra en pantalla True o False
assert(comparar_edades(5,5,5) == "Las edades ingresadas son iguales") #Es True
assert(comparar_edades(6,5,5) == 6) #Es True
assert(comparar_edades(5,7,5) == 7) #Es True
assert(comparar_edades(5,5,8) == 8) #Es True
print("Paso los test de la funcion Comparar_edades")

# Consigna 3: 
# Crea una función que permita simular una partida de "Piedra, Papel o Tijera" entre dos jugadores. 
# La función deberá recibir dos parámetros representando las elecciones de cada jugador: 
# -  Cada jugador debe elegir entre: "piedra", "papel" o "tijera". 
# -  La función debe devolver: 
# -  "Empate" si ambos jugadores eligieron lo mismo. 
# -  "Gana jugador 1" o "Gana jugador 2" según las reglas clásicas: 
# -  Piedra gana a Tijera. 
# -  Tijera gana a Papel. 
# -  Papel gana a Piedra. 

#1 - identificar problema ( simular una partida entre dos jugadores de piedra, papel o tijera)




















