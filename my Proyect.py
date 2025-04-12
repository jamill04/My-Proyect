class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}"


class SistemaLibros:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros en el sistema.")
        else:
            print("Lista de libros:")
            for libro in self.libros:
                print(libro)

    def buscar_libro(self, consulta):
        resultados = []
        for libro in self.libros:
            if consulta.lower() in libro.titulo.lower() or consulta.lower() in libro.autor.lower():
                resultados.append(libro)
        return resultados


def menu():
    sistema = SistemaLibros()

    while True:
        print("\n--- Sistema de Gestión de Libros ---")
        print("1. Agregar libro")
        print("2. Mostrar libros")
        print("3. Buscar libro")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, isbn)
            sistema.agregar_libro(libro)
            print("Libro agregado correctamente.")

        elif opcion == "2":
            sistema.mostrar_libros()

        elif opcion == "3":
            consulta = input("Ingrese el título o autor a buscar: ")
            resultados = sistema.buscar_libro(consulta)
            if resultados:
                print("Resultados de la búsqueda:")
                for libro in resultados:
                    print(libro)
            else:
                print("No se encontraron libros con esa consulta.")

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
