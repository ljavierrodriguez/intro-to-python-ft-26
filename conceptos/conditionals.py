# Condicionales
""" 

if condition:
    codigo

if condition:
    condigo
else:
    condigo


if condition:
    pass
elif condition:
    pass
elif condition:
    pass
else:
    pass


variable = value if condition else value2



"""

a = 5 
b = 10
c = 8

if a > b:
    print("A > B")


if a > c:
    print("A > C")
else:
    print("A < C")


if a > b and a > c:
    print("A > B y C")
elif b > c:
    print("B > A y C")
else:
    print("C > A y B")


mayor = True if a > 18 else False

if mayor:
    print("Puedes Pasar")