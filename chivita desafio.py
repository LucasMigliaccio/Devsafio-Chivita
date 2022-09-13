from random import choice

#animales = ["el lobo", "el toro", "la vaca", "el burro", "el raton", "el gato", "el perro", "el pajaro", "la marmota", "la tortuga", "el aguila", "el oso", "la abeja","el cocodrilo", "el leon",
#           "la hiena","el pez", "el tiburón", "la tortuga", "el burro", "el cerdo", "la gallina", "el lemur", "el camaleon", "el tigre", "el escorpión", "el ciervo", "el condor", "el pinguino", "la foca" ] 

animales=["el lobo", "el toro", "la vaca"]
cadena= []
nosaca= []

def HayQueLlamar(self):

    baraja= choice(self)
    cadena.append(baraja)
    return baraja

actual = "la chiva"
z = int(input("¿Cuantos animales queres que aparezcan?: "))

n= 0
for n in range(z):

    print("Sal de ahí chivita chivita, sal de ahí de ese lugar")
    proximo = HayQueLlamar(animales)
    if proximo == actual:
        proximo = HayQueLlamar(animales)
        for proximo in range(cadena):
            if proximo not in cadena:
                proximo = HayQueLlamar(animales)
                

            else:
                print("NO SE PUEDEN REPETIR ANIMALES")
                


    print("vamos a llamar a ", proximo, " para que saque a", actual)
    saca = f'{proximo}, no quiere sacar a {actual}\n'
    nosaca.append(saca)

    for x in range(len(nosaca) -1, -1, -1):

        print (nosaca[x], end="")
    
    print("la chiva no quiere salir de ahi" ) 
    actual = proximo
    n=+1

print()
print(cadena)
print()
