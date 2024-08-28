
# Calcular una catiedad de horas a: Dias, Minutos y Segundos

print("Calcular una catiedad de horas a: Dias, Minutos y Segundos\n")

horas = int(input("Dame la catidad en horas: "))

dias = horas // 24
horas_restantes = horas % 24
minutos = horas * 60
segundos = horas * 3600


print(f"{horas} horas equivalen a:")
print(f"{dias} días y {horas_restantes} horas")
print(f"{minutos} minutos")
print(f"{segundos} segundos")