# Loops

""" 

for valor in range o coleccion:
    codigo


while condition:
    codigo




"""

nombres = ["Hugo", "Paco", "Luis"]

for i in range(1, 11): # start=0, stop, step=1 
    print(i)


for i in range(len(nombres)):
    print(nombres[i])

for valor in nombres:
    print(valor)

indice = 0
while indice < len(nombres):
    print(nombres[indice])
    indice += 1 # indice = indice + 1