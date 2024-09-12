# Funciones

""" 


def function_name(params...):
    codigo



variable_name = lambda params : return


"""

def sumar(a, b):
    return a + b

restar = lambda a, b: a - b

result = sumar(1, 2)
print(result) # 3

result = restar(10, 5)
print(result) # 5



""" 
Parametros Posicionales
"""

def imprimir_nombre_completo(nombre, apellido):
    return f"{nombre} {apellido}"

print(imprimir_nombre_completo("Luis", "Rodriguez")) # Luis Rodriguez

""" 
Parametros con valores por defecto
"""

def saludar(nombre="Luis"):
    return f"Hola, {nombre}"


""" 
Parametros keywords
"""
def nombre_completo(nombre, apellido, ciudad):
    return f"Mi nombre es: {nombre} {apellido} y vivo en: {ciudad}"

result = nombre_completo("John", "Doe", "Paris")
print(result)

result = nombre_completo(ciudad="Caracas", apellido="Rodriguez", nombre="Javier")
print(result)

""" 
Empaquetamiento de Argumentos
"""

def totalizar(*args):
    return sum(args)

print(totalizar(1, 2, 3, 4, 5, 6))

""" 
Empaquetamiento de Argumentos Keywords
"""

def datos_personales(**kwargs):
    return f"Nombre: {kwargs["nombre"]}, Edad: {kwargs["edad"]}, Ciudad: {kwargs["ciudad"]}"


print(datos_personales(edad=42, nombre="Luis", ciudad="Santiago"))