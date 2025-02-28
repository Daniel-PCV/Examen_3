pregunta = []  

while len(pregunta) < 10:  
    try:
        num = int(input(f"Digite un número ({len(pregunta) + 1}/10): "))  
        pregunta.append(num) 
        print(f"Número agregado: {num}, Total ingresados: {len(pregunta)}")
    except ValueError:
        print("Error: Ingrese un número válido.")

suma = sum(pregunta)  
promedio = suma / len(pregunta)  
mayor = max(pregunta)  
menor = min(pregunta)  


print("\nResultados:")
print(f"Suma de los números: {suma}")
print(f"Promedio de los números: {promedio:.2f}")
print(f"Número más grande: {mayor}")
print(f"Número más pequeño: {menor}")
