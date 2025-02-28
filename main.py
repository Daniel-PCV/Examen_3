from cuadrado import calcular_cuadrado
  
from triangulo import calcular_triangulo

lado = float(input("Ingrese el tamaño del lado del cuadrado: "))
resultado = calcular_cuadrado(lado)
print(resultado)

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
lado1 = float(input("Ingrese el primer lado del triángulo: "))
lado2 = float(input("Ingrese el segundo lado del triángulo: "))
lado3 = float(input("Ingrese el tercer lado del triángulo: "))

resultado = calcular_triangulo(base, altura, lado1, lado2, lado3)
print(resultado)
