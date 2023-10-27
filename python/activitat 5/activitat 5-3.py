mes = int(input("Introduce un mes"))
dia = int(input("Introduce un día"))
if (mes > 0) and (mes < 13):
    print (mes)
elif (mes < 0) and (mes > 13):
    print ("Error")
if (mes==1) or (mes ==3) or (mes==5) or (mes==7) or (mes==8) or (mes==10) or (mes==12):
    print (dia < 32) and (dia > 0) 
    print ("día"+ dia) ("del"+ mes)
if (mes==4) or (mes==6) or (mes==9) or (mes==11):
    print (dia<31) and (dia > 0)
    print ("día"+ dia) and ("del"+ mes)
if (mes==2):
    print (dia < 29) and (dia > 0)
    print ("día"+ dia) and ("del"+ mes)
