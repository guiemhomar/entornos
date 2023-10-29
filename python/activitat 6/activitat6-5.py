contadormaxint=-9999999
contminint=99999999
contint=0
sumaint=0
mediaint=0
A=float(input("Introduce numeros enteros (que el ultimo sea el 0)"))
while A != 0:
    if (A>contadormaxint):
        contadormaxint=A
    sumaint=sumaint + A
    contint=contint + 1
if (contint>0):
    mediaint = sumaint / contint
    print("El maximo es", contadormaxint)
    print("El minimo es 0")
    print("La media es", mediaint)
elif (contint<0):
    print("Error")