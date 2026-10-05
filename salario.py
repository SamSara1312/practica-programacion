"""
Programa que calcula el salario neto con descuento.
"""
TASA_DESCUENTO = 0.10

def calcular_salario():
    salario = float(input("Salario bruto: $"))
    
    descuento = salario * TASA_DESCUENTO
    salario_neto = salario - descuento
    
    print(f"Descuento: ${descuento:.2f}")
    print(f"Salario neto: ${salario_neto:.2f}")

if __name__ == "__main__":
    calcular_salario()
