import numpy as np
from Home import *

#r2 = int(input("Enter value of r2 : "))
#r3 = int(input("Enter value of r3 : "))
#r4 = int(input("Enter value of r4 : "))
#r5 = int(input("Enter value of r5 : "))
#r6 = int(input("Enter value of r6 : "))
#r7 = int(input("Enter value of r7 : "))
#vSource = int(input("Enter the value of voltage source: "))

#Node2Data:
constn2=(r2*r3*vSource)
Vn2=-(-(r2*r3)-(r1*r3)-(r1*r2))
Vn3=-(r1*r3)
Vn4=-(r1*r2)
Vn5=0
CoffOfNode2=[Vn2, Vn3, Vn4, Vn5,constn2]
print(CoffOfNode2)
    

#Node3Data:
Vn2=(r4*r5)
Vn3=(-(r2*r4)-(r4*r5)-(r2*r5))
Vn4=(r2*r5)
Vn5=(r2*r4)
constn3=0

CoffOfNode3=[Vn2, Vn3, Vn4, Vn5,constn3]
print(CoffOfNode3)

#Node4Data:
Vn2=(r4*r6)
Vn3=(r3*r6)
Vn4=-((r3*r6)+(r4*r6)+(r3*r4))
Vn5=(r3*r4)
constn4=0
CoffOfNode4=[Vn2, Vn3, Vn4, Vn5,constn4]
print(CoffOfNode4)

#Node5Data:
Vn2=0
Vn3=(r6*r7)
Vn4=(r5*r7)
Vn5=-(r6*r7)-(r5*r7)-(r5*r6)
constn5=0
CoffOfNode5=[Vn2, Vn3, Vn4, Vn5,constn5]
print(CoffOfNode5)


print(CoffOfNode2[0], "Vn2", CoffOfNode2[1], "Vn3", CoffOfNode2[2], "Vn4", CoffOfNode2[3], "Vn5", "=", constn2)
print(CoffOfNode3[0], "Vn2", CoffOfNode3[1], "Vn3", CoffOfNode3[2], "Vn4", CoffOfNode3[3], "Vn5", "=", constn3)
print(CoffOfNode4[0], "Vn2", CoffOfNode4[1], "Vn3", CoffOfNode4[2], "Vn4", CoffOfNode4[3], "Vn5", "=", constn4)
print(CoffOfNode5[0], "Vn2", CoffOfNode5[1], "Vn3", CoffOfNode5[2], "Vn4", CoffOfNode5[3], "Vn5", "=", constn5)

c = np.array([CoffOfNode2, CoffOfNode3, CoffOfNode4, CoffOfNode5])
#Seidel
x = np.zeros(len(c))
for k in range(0, 20):
    for i in range(0, len(c)):
        y = 0
        for j in range(0, len(c)):
            if i != j:
                y = y + (c[i][j] * x[j])
        y = c[i][len(c)] - y
        x[i] = y / c[i][i]

print(x)

Vn = x
Vn2 = Vn[0]
Vn3 = Vn[1]
Vn4 = Vn[2]
Vn5 = Vn[3]


v1 = vSource-Vn2
v2 = Vn2-Vn3
v3 = Vn2-Vn4
v4 = Vn4-Vn3
v5 = Vn3-Vn5
v6 = Vn4-Vn5
v7 = Vn5



print("The Voltage Of r1 is ", v1, "and current is ", round((v1/r1), 4) )
print("The Voltage Of r2 is ", v2, "and current is ", round((v2/r2), 4))
print("The Voltage Of r3 is ", v3, "and current is ", round((v3/r3), 4))
print("The Voltage Of r4 is ", v4, "and current is ", (v4/r4))
print("The Voltage Of r5 is ", v5, "and current is ", (v5/r5))
print("The Voltage Of r6 is ", v6, "and current is ", (v6/r6))
print("The Voltage Of r7 is ", v7, "and current is ", (v7/r7))




