# ===========================================
# CONVERSOR DE MONEDAS - VERSIÓN 4
# Autor(a): SEBASTIAN VILCA
# ===========================================

soles = float(input("Ingrese la cantidad en soles: "))

print("1. dolares")
print("2. euros")
print("3. libras esterlinas")
print("4. yenes")

opcion = input("seleccione una opcion: ")

if opcion == "1":
  dolares = soles / 3.80
  print("equivale a", dolares,"dolares.")

elif opcion == "2":
     euros = soles/ 4.20
     print("equivale a", euros, "euros.")

elif opcion == "3":
  libras  = soles / 4.80
  print("equivale a", libras, "libras".)
  
        elif opcion == "4":
  yenes = soles * 41.5
  print("equivales a" , yenes , "yenes".)
  
else:
print("opcion no valida.")
