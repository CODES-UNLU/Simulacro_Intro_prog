def clasificar_entrada(texto):
    cartel = ""
    if texto.isdigit():
        cartel = "La entrada contiene solo dígitos."
    elif texto.isalpha():
        cartel = "La entrada contiene solo letras."
    elif texto.isalnum():
        cartel = "La entrada contiene letras y/o números, pero sin símbolos."
    return cartel

