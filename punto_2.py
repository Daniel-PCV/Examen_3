
# Parte 2: Funciones Lambda (15 min)

# Crear una lista de números máximo 15 y usar map() y lambda para elevar al cuadrado cada número de la lista.

# Desafío extra: Filtrar los números mayores a 50 utilizando filter().


pregunta = []  
while len(pregunta) < 15:  
    try:
        num = int(input(f"Digite un número ({len(pregunta) + 1}/15): "))  
        pregunta.append(num) 
        print(f"Número agregado: {num}, Total ingresados: {len(pregunta)}")
    except ValueError:
        print("Error: Ingrese un número válido.")

cuadrado = lambda x: x**2
cuadrados = [cuadrado(num) for num in pregunta]
print("Cuadrados de los números ingresados:")
for i, cuadrado in enumerate(cuadrados):
    print(f"{pregunta[i]}^2 = {cuadrado}")



filtro = filter(lambda x: x > 50, pregunta)

for num in filtro:
  
    print(f"Numeros mayores a 50 {num}")