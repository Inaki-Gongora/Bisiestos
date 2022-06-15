#año=int(input("ingrese un año: "))
#if año%4==0 and año%100!=0:print("El año es bisiesto")
#elif año%400==0:print("El año es bisiesto")
#else:print("El año no es bisiesto")
#añoB=2020
#años=2022
#while años <=2100:
#    añoB=añoB+4
#    print (añoB)
#    años=años+4
años=[]
for i in range (2020,2100,4):
    años.append(i)
años.pop(0)
print(años)
