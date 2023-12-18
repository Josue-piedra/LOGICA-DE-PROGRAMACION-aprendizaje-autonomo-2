#Actividad 1
a = int(input("Ingrese un número: "))
b = int(input("Ingrese un número: "))
c = int(input("Ingrese un número: "))

if a >= b and a >= c:
    mayor = a
elif b >= a and b >= c:
    mayor = b
else:
    mayor = c

print(f"El número mayor es: {mayor}")



