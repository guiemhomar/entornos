A = int(input("Dame el valor"))
B = int(input("Dame el valor"))
C = int(input("Dame el valor"))
if (A > B ) and (A > C):
    print (A, "es mayor")
if (A < B) and (B > C):
    print (B, "es mayor")
if (C > A) and (C > B):
    print (C, "es mayor")
if (A == B) and (A == C):
    print ("A, B y C son iguales")
    
