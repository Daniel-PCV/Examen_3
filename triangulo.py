def calcular_triangulo(base, altura, lado1, lado2, lado3):
    
    if base <= 0 or altura <= 0 or lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        return "Todos los lados y la altura deben ser números positivos."

    area = (base * altura) / 2
    perimetro = lado1 + lado2 + lado3
    return f"Área: {area}, Perímetro: {perimetro}"


