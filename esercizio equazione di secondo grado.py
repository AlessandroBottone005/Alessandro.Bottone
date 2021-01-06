a = int (input("inserisci il coefficiente a:"))
b = int (input("inserisci il coefficiente b:"))
c = int (input("inserisci il termine noto c:"))

import math
delta = pow(b,2) -4*a*c
if delta < 0:
    print ("l'equazione non ammette soluzioni")
    elif delta > 0:
        print ("l'equazione ammette due soluzioni reali e distinte")
        print ("x1 = x2 =", -b/2*a)
        else:
            print ("x1 = ",(-b-math.sqrt(delta))/2*a)
            print ("x2 = ",(-b+math.sqrt(delta))/2*a)
