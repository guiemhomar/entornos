contadorint=0
sumaint=0
mediaint=0
A=int(input("Introduce numeros enteros (que acaben en -1)"))
while A != -1:
    sumaint=sumaint+A
    contadorint = contadorint + 1

if (contadorint > 0):
    mediaint=sumaint/contadorint
    print ("La media de los numeros es", mediaint)
elif (contadorint < 0):
    print("No se acpetan numeros negativos mas pequeños que (-1)")
