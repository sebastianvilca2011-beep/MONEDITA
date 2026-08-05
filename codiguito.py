# ===========================================
# CONVERSOR DE MONEDAS - VERSIÓN 2
# Autor(a): SEBASTIAN VILCA
# ===========================================

soles = float(input("Ingrese la cantidad en soles: "))

print("1. dolares")
print("2. euros")

opcion = input("seleccione una opcion: ")

if opcion == "1":
  dolares = soles / 3.80
  print("equivale a", dolares,"dolares.")

elif opcion == "2":
     euros = soles/ 4.20
     print("equivale a", euros, "euros.")
else:
print("opcion no valida.")
