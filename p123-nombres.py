# Procesa dos listas de cadena (nombre)


def procesa(nombres1, nombres2):
    todos = nombres1 + nombres2
    todos.sort()
    for i in range(len(todos)):
        todos[i] =  todos[i].upper()
    return todos


def entrada():
    dat = []
    while True:
        d = input('Nombre :')
        if d=='': break
    return dat


# PROGRAMA PRINCIPAL
import os; os.system('Clear')

n1 = ['Juan', 'Pedro', 'Luis', 'Jose', 'Maria']
#nombres2 = ['Rocio', 'Teresa', 'Karla']
n2 = entrada()
n3 = procesa(n1, n2)

print(n3)