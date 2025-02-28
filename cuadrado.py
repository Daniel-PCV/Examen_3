def calcular_cuadrado(lado):
  
    if lado <= 0:
        return "El lado debe ser un número positivo."
    
    area = lado * lado
    perimetro = 4 * lado
    return f"Área: {area}, Perímetro: {perimetro}"

