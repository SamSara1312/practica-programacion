"""
Programa que calcula el promedio de 3 calificaciones.
"""
def calcular_promedio():
    n1 = float(input("Calificación 1: "))
    n2 = float(input("Calificación 2: "))
    n3 = float(input("Calificación 3: "))
    
    promedio = (n1 + n2 + n3) / 3
    
    print(f"El promedio es: {promedio:.2f}")

if __name__ == "__main__":
    calcular_promedio()
