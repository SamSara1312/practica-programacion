"""
Programa que calcula el área de un rectángulo.
"""
def calcular_area():
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    
    area = base * altura
    
    print(f"El área es: {area:.2f}")

if __name__ == "__main__":
    calcular_area()
