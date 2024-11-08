
#La Academia de futbol Santos Laguna, desea llevar el control de los jugadores en cada categoría.
# Las categorías se conforman de acuerdo con la edad y pueden tener varios jugadores. 
# Diseña una aplicación con programación orientada a objetos.

class Jugador:
    def __init__(self, nombre, añonac, sexo, becado):
        self.nombre = nombre
        self.añonac = añonac
        self.sexo = sexo
        self.becado = becado
        self.total = 1

    def __str__(self):
        estado_beca = "Becado" if self.becado.lower() == "becado" else "Sin Beca"
        return f"Nombre: {self.nombre:<20} AñoNacimiento: {self.añonac:<4} Sexo: {self.sexo:<6} Becado: {estado_beca}"


class Categoria:
    def __init__(self, nombre, rango, costo):
        self.nombre = nombre
        self.rango = rango
        self.costo = costo
        self.jugadores = list()
    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
    def total_jugadores(self):
        return len(self.jugadores)
    def contar_por_genero(self):
        hombres = sum(1 for jugador in self.jugadores if jugador.sexo == "Hombre")
        mujeres = sum(1 for jugador in self.jugadores if jugador.sexo == "Mujer")
        return hombres, mujeres
    def subtotal_categoria(self):
        return sum(self.costo for jugador in self.jugadores if jugador.becado.lower() != "becado")
    def __str__(self):
        return f"{self.nombre} - {self.rango} - ({self.total_jugadores()})"


class Academia:
    def __init__(self, nombre, propietario, domicilio):
        self.nombre = nombre
        self.propietario = propietario
        self.domicilio = domicilio
        self.categorias = list()

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def total_generos(self):
        total_hombres = sum(categoria.contar_por_genero()[0] for categoria in self.categorias)
        total_mujeres = sum(categoria.contar_por_genero()[1] for categoria in self.categorias)
        return total_hombres, total_mujeres

    def total_ingresos(self):
        return sum(categoria.subtotal_categoria() for categoria in self.categorias)

    def __str__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Propietario: {self.propietario}\n"
                f"Domicilio: {self.domicilio}\n")


def main():
    import os; os.system("clear")
    miacademia = Academia("Academia Santos Laguna", "Francisco Nava", "Aguanaval 123, Hidráulica")
    # JUGADORES POR CATEGORIA 
    cat1 = Categoria("Junior A", "2006-2007-2008", 1250)
    cat1.agregar_jugador(Jugador("Alexander Lopez", 2006, "Hombre", "Sin Beca"))
    cat1.agregar_jugador(Jugador("Uriel Puga", 2007, "Hombre", "Becado"))
    cat1.agregar_jugador(Jugador("Alejandra Escalona", 2008, "Mujer", "Sin Beca"))

    cat2 = Categoria("Junior B", "2009-2010-2011", 850)
    cat2.agregar_jugador(Jugador("Armando Santana", 2009, "Hombre", "Sin Beca"))
    cat2.agregar_jugador(Jugador("Daniel Mijares", 2010, "Hombre", "Sin Beca"))
    cat2.agregar_jugador(Jugador("Antonio Hernandez", 2011, "Mujer", "Becado"))

    cat3 = Categoria("Pony A", "2012-2013-2014", 700)
    cat3.agregar_jugador(Jugador("Andrea Solis", 2012, "Mujer", "Becado"))
    cat3.agregar_jugador(Jugador("Marissa Hernandez", 2013, "Mujer", "Becado"))
    cat3.agregar_jugador(Jugador("Diana Soto", 2014, "Mujer", "Sin Beca"))

    # CATEGORIAS
    miacademia.agregar_categoria(cat1)
    miacademia.agregar_categoria(cat2)
    miacademia.agregar_categoria(cat3)
    total_hombres, total_mujeres = miacademia.total_generos()

    # REPORTE COMPLETO DE EL CLUB
    print("REPORTE DEL CLUB DEPORTIVO")
    print(miacademia)
    print("Total de Categorías:", len(miacademia.categorias))
    print("Total de Hombres:", total_hombres)
    print("Total de Mujeres:", total_mujeres)

    print("\nDatos generales de las Categorías:")
    for categoria in miacademia.categorias:
        print(f"Nombre: {categoria.nombre:<10} Rango: {categoria.rango} Costo: ${categoria.costo:,.2f}")

    print("\nJugadores por Categoría:")
    for categoria in miacademia.categorias:
        print(f"\n{categoria}")
        for jugador in categoria.jugadores:
            print(jugador)
        print(f"Subtotal: ${categoria.subtotal_categoria():,.2f}")

    print(f"\nTotal Ingresos: ${miacademia.total_ingresos():,.2f}")

if __name__ == "__main__":
    main()
