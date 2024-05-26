import unittest
import os
import json
from libreria import Libreria

class TestLibreria(unittest.TestCase):
    #  Inicializa una nueva instancia de Libreria y un libro de ejemplo antes de cada prueba.
    def setUp(self):
        self.libreria = Libreria()
        self.libro_ejemplo = {
            "titulo": "Cien años de soledad",
            "autor": "Gabriel García Márquez",
            "genero": "Novela",
            "anio": 1967
        }
    
    def tearDown(self):
        # Limpiar archivos de prueba
        if os.path.exists("test_libreria.json"):
            os.remove("test_libreria.json")
    
    
    # Casos de uso típicos
    
    def test_anadir_libro(self):
        resultado = self.libreria.anadir_libro(**self.libro_ejemplo)
        self.assertEqual(resultado, "Libro añadido")
        self.assertIn(self.libro_ejemplo, self.libreria.libros)
    
    def test_buscar_libro(self):
        self.libreria.anadir_libro(**self.libro_ejemplo)
        resultado = self.libreria.buscar_libro("Cien años de soledad")
        self.assertEqual(resultado, [self.libro_ejemplo])
    
    def test_buscar_por_autor(self):
        self.libreria.anadir_libro(**self.libro_ejemplo)
        resultado = self.libreria.buscar_por_autor("Gabriel García Márquez")
        self.assertEqual(resultado, [self.libro_ejemplo])
    
    def test_eliminar_libro(self):
        self.libreria.anadir_libro(**self.libro_ejemplo)
        resultado = self.libreria.eliminar_libro("Cien años de soledad")
        self.assertEqual(resultado, "Libro eliminado")
        self.assertNotIn(self.libro_ejemplo, self.libreria.libros)
        
        resultado_no_encontrado = self.libreria.eliminar_libro("Libro no existente")
        self.assertEqual(resultado_no_encontrado, "Libro no encontrado")
    
    def test_guardar_libros(self):
        self.libreria.anadir_libro(**self.libro_ejemplo)
        resultado = self.libreria.guardar_libros("test_libreria.json")
        self.assertEqual(resultado, "Libros guardados")
        self.assertTrue(os.path.exists("test_libreria.json"))
        
        with open("test_libreria.json", "r") as f:
            libros_cargados = json.load(f)
        self.assertEqual(libros_cargados, [self.libro_ejemplo])
    
    def test_cargar_libros(self):
        self.libreria.anadir_libro(**self.libro_ejemplo)
        self.libreria.guardar_libros("test_libreria.json")
        
        nueva_libreria = Libreria()
        resultado = nueva_libreria.cargar_libros("test_libreria.json")
        self.assertEqual(resultado, "Libros cargados")
        self.assertEqual(nueva_libreria.libros, [self.libro_ejemplo])
        
        resultado_no_encontrado = nueva_libreria.cargar_libros("archivo_inexistente.json")
        self.assertEqual(resultado_no_encontrado, "Archivo no encontrado")
    
    
    # Casos extremos
    
    def test_anadir_libro_con_titulo_largo(self):
        # Generar un título muy largo
        titulo_largo = "a" * 1000
        resultado = self.libreria.anadir_libro(titulo_largo, "Autor", "Género", 2000)
        self.assertEqual(resultado, "Libro añadido")
    
    def test_buscar_libro_con_titulo_inexistente(self):
        resultado = self.libreria.buscar_libro("Título inexistente")
        self.assertEqual(resultado, [])
    
   
    # Errores de entrada

    def test_anadir_libro_con_datos_faltantes(self):
        resultado = self.libreria.anadir_libro("Título", "Autor")
        self.assertEqual(resultado, "Datos incompletos")
    
    def test_buscar_libro_con_titulo_vacio(self):
        resultado = self.libreria.buscar_libro("")
        self.assertEqual(resultado, [])
    
    def test_eliminar_libro_con_titulo_vacio(self):
        resultado = self.libreria.eliminar_libro("")
        self.assertEqual(resultado, "Título vacío")

if __name__ == '__main__':
    unittest.main()