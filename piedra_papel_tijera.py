# Piedra, papel o tijera

import random

print("--------------------------------------------")
print("-----------Piedra_papel o tijera-----------")
print("--------------------------------------------")

print("1 es piedra")
print("2 es papel")
print("3 es tijera")

# input

j1 = int(input("Elija: "))
    
# processing

cpu = random.randint(1,3)

if (j1 == 1):
    if (cpu == 1):
        print("Empate")
        print("Sacaste " + str (j1) + " la cpu saco " + str (cpu))
    elif (cpu == 2):
        print("Perdiste")
        print("Sacaste " + str (j1) + " la cpu saco " + str (cpu))
    else:
        print("Ganaste")
        print("Sacaste " + str (j1) + " la cpu saco " + str (cpu))

if (j1 == 2):
    if (cpu == 1):
        print("Ganaste")
        print("Sacaste " + str (j1) + " la cpu saco " + str (cpu))
    elif (cpu == 2):
        print("Empate")
        print("Sacaste " + str (j1) + " la cpu saco " + str (cpu))
    else:
        print ("Empate")
        print("Sacaste " + str (j1) + " la cpu saco " + str (cpu))
    
if (j1 == 3):
    if (cpu == 1):
        print ("Perdiste")
        print("Sacaste " + str (j1) + " la cpu saco " + str (cpu))
    elif (cpu == 2):
        print("Ganaste")
        print("Sacaste " + str (j1) + " la cpu saco " + str (cpu))
    else:
        print("Empate")
        print("Sacaste " + str (j1) + " la cpu saco " + str (cpu))
if (j1 > 3):
    print("Ingresaste algo mayor que 3 o una letra no válida,vuelve a intentar otra vez")