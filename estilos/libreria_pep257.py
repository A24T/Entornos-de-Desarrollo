import json


class Libreria:
    """
    Esta clase representa una biblioteca virtual para gestionar libros.

    Atributos:
        libros (list): Una lista de diccionarios que representan los libros de la biblioteca.
            Cada diccionario contiene las claves 'titulo', 'autor', 'genero' y 'anio'.
    """

    def __init__(self):
        """
        Inicializa la biblioteca con una lista vacía de libros.
        """
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        """
        Añade un nuevo libro a la biblioteca.

        Args:
            titulo (str): El título del libro.
            autor (str): El autor del libro.
            genero (str): El género del libro.
            anio (int): El año de publicación del libro.

        Returns:
            str: Un mensaje de confirmación que indica si el libro se ha añadido correctamente.
        """
        self.libros.append({
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "anio": anio
        })
        return "Libro añadido"

    def buscar_libro(self, titulo):
        """
        Busca un libro en la biblioteca por su título.

        Args:
            titulo (str): El título del libro a buscar.

        Returns:
            list: Una lista de diccionarios que representan los libros que coinciden con el título buscado.
        """
        return [
            libro for libro in self.libros
            if libro["titulo"].lower() == titulo.lower()
        ]

    def buscar_por_autor(self, autor):
        """
        Busca libros en la biblioteca por el nombre del autor.

        Args:
            autor (str): El nombre del autor a buscar.

        Returns:
            list: Una lista de diccionarios que representan los libros escritos por el autor especificado.
        """
        return [
            libro for libro in self.libros
            if autor.lower() in libro["autor"].lower()
        ]

    def eliminar_libro(self, titulo):
        """
        Elimina un libro de la biblioteca por su título.

        Args:
            titulo (str): El título del libro a eliminar.

        Returns:
            str: Un mensaje que indica si el libro se ha eliminado correctamente o no.
        """
        original_count = len(self.libros)
        self.libros = [
            libro for libro in self.libros
            if libro["titulo"].lower() != titulo.lower()
        ]
        if len(self.libros) < original_count:
            return "Libro eliminado"
        else:
            return "Libro no encontrado"

    def guardar_libros(self, archivo):
        """
        Guarda la lista de libros en un archivo JSON.

        Args:
            archivo (str): La ruta del archivo JSON donde se guardarán los libros.

        Returns:
            str: Un mensaje de confirmación que indica si los libros se han guardado correctamente.
        """
        with open(archivo, "w") as f:
            json.dump(self.libros, f)
        return "Libros guardados"

    def cargar_libros(self, archivo):
        """
        Carga una lista de libros desde un archivo JSON.

        Args:
            archivo (str): La ruta del archivo JSON que contiene los libros a cargar.

        Returns:
            str: Un mensaje que indica si los libros se han cargado correctamente o si ha ocurrido un error.
        """
        try:
            with open(archivo, "r") as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"


mi_libreria = Libreria()
mi_libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
mi_libreria.guardar_libros("libreria.json")
print(mi_libreria.cargar_libros("libreria.json"))
print(mi_libreria.buscar_por_autor("Gabriel García Márquez"))