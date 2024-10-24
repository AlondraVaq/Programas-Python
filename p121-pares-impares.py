# Dada un lista de numeros, devolver los pares, devolver los impares 

def pares_impres(nums):
    p = []
    i=[]
    for n in nums:
        if n%2==0:
            p.append(n)
        else:
            i.append(n)
    return p, i 

# PROGRAMA PRINCIPAL
import os; os.system('Clear')
nums = [9, 8, 60, 6, 90, 7, 10, 6, 7]
pares, inmpares = pares_impres(nums)

print('Numeros ', nums, len(nums))
print('Los pares son :', )