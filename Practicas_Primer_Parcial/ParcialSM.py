# El club de pesaca " El Engorde" de la ciudad de San Miguel, desea que relicemos
# un programa que les permita llevar el control de datos de los concursos de pesca. 
# Cada concursante debe ingresar:
#     Numero, edad, Medida del pescado(Cm), Peso del pescado(Gr).
# Teniendo en cuenta las siguientes reglas: 
#     a- Si la edad del pescador es menor a 12 años y el pescado pesa menos de 800 gramos
#        al peso se le debe agregar 300 gramos.
#        Tambien si el largo es menor a 20 centimetros, se le debe agregar 5 cm.
#        Pero si el pescado cumple con ambas condiciones
#        (Pesa menos de 800 gr y mide menos de 20 cm). Entonces al peso se le debe agregar 500 gms y al
#        largo se le debe agregar 15 cm.
#     b- Si la edad del pescador es mayor a 40 años y el pescado pesa mas 1800g al peso se le deben restar
#     500g y ademas si el largo es mayor a 200 cm se le deben sacar 50 cm.
#     Pero si el pescado cumple con ambas condiciones(Pesa mas de 1800g y mide mas de 200 cm) entonces al peso 
#     se le quitan 800 g y al largo se deben sacar 80 cm.
    
# Realizar una funcion que reciba: numero y edad del concursante, peso del pescado en gramos y largo del pescado en cm.
# y retorne el que corresponde en ese concursante

def concurso(numero,edad,peso,largo):
    
    if edad < 12: #Concursante
        if peso < 800 and largo < 20: #Pescado
            peso += 500
            largo += 15
        elif peso < 800:
            peso += 300
        elif largo < 20:
            largo += 5

    elif edad > 40:
        if peso > 1800 and largo > 200:
            peso -= 800
            largo -= 80
        elif peso > 1800:
            peso -= 500
        elif largo > 200:
            largo -=50
    if (edad >=12 and edad <=40):
        return False 
        
    return f"Concursante N°:{numero} - Edad {edad} Peso final:{peso}g, Largo: {largo}cm"

print(concurso(15,41,2000,201))
            


############################################################################################################################
# Desarrolle una función llamada comparar_resto_con_longitud que reciba dos parámetros:
# un número entero n1, ENTERO
# un texto (string) cadena.
# La función debe retornar True si la cantidad de caracteres del string es igual al resto de dividir n1 entre la longitud de la cadena, y False en caso contrario.
# Condiciones:
# Si la cadena es vacía, la función debe retornar False para evitar división por cero.

def comparar_resto_con_longitud(n1,texto):
    auxiliar = len(texto) #cantidad de caracteres
    auxiliar2 = n1/auxiliar # division
    
    cartel = ""
    if auxiliar2 %2 == 0:
        cartel = True
    else: 
        cartel = False
    return cartel 


def comparar_resto_con_longitud(n1, texto):
    if not texto:  # Verifica si el texto está vacía para evitar errores de división
        return False
    
    longitud_texto = len(texto)  # Guarda la longitud en una variable
    resto_division = n1 % longitud_texto  # Calcula el resto de la división
    
    if resto_division == longitud_texto:  # Compara el resto con la longitud
        resultado = True
    else:
        resultado = False
    
    return resultado


