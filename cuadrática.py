from math import sqrt

print("ax^2 + bx + c")

a=int(input("DAME EL NUMERO -A-"))
b=int(input("DAME EL NUMERO -B-"))
c=int(input("DAME EL NUMERO -C-"))

x1=0
x2=0

if ((b**2)-4*a*c) < 0:
    print("Tus resultados seran numeros complejos")
else:
    x1 = (-b + (sqrt(b**2)-4*a*c))/(2*a)
    x2 = (-b - (sqrt(b**2)-4*a*c))/(2*a)
    print('Las soluciones a tu ecuacion son: ')
    print (x1)
    print (x2)