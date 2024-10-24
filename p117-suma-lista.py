# Suma un lista de numeros, usanado una funcion

def suama_lista(lista):
    s = 0
    for n in lista:
        s += n
    return s


nums = [10, 20, 30, 40, 50]

res = suama_lista(nums)

print(f'La suma de la lista es : {res}')