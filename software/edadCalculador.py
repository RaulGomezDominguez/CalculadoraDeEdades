# Obtener el año actual
from datetime import date

# Pedir al usuario su año de nacimiento
try:
    año_nacimiento = int(input("Por favor, ingresa tu año de nacimiento: "))
except ValueError:
    print("Por favor, ingresa un año válido.")
    exit()

# Calcular la edad
año_actual = date.today().year
edad = año_actual - año_nacimiento

# Imprimir la edad
print(f"Tienes {edad} años.")