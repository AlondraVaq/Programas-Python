# Dado el año de nacimiento, la suma de sus dígitos individuales es el número de la suerte.

print("Dado el año de nacimiento, la suma de sus dígitos individuales es el número de la suerte\n")


AñoDeNacimiento = int(input("Dame el año: "))

digitos = [int(d) for d in str(AñoDeNacimiento)]

NumeroSuerte = sum(digitos)


print(f"Los dígitos individuales del año {AñoDeNacimiento} son: {digitos}")
print(f"El número de la suerte es: {NumeroSuerte}")