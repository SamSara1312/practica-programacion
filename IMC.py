"""
Programa que calcula el Índice de Masa Corporal (IMC).
"""
def calcular_imc():
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    
    imc = peso / (altura ** 2)
    
    print(f"Tu IMC es: {imc:.2f}")

if __name__ == "__main__":
    calcular_imc()
