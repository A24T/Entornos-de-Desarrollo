# Biblioteca Python
Este repositorio contiene una implementación simple de una biblioteca en Python, junto con pruebas unitarias que abarcan casos típicos, casos extremos y errores de entrada. También se incluye un archivo de texto que describe un nuevo método añadido a la biblioteca, junto con su prueba unitaria correspondiente. Se utilizaron técnicas de debugging durante el desarrollo para identificar y solucionar errores.

### Contenido del repositorio
1. **libreria.py:** Este archivo contiene la implementación de la clase "Libreria", que proporciona funcionalidades básicas para gestionar una colección de libros, como añadir libros, buscar por título o autor, eliminar libros, guardar y cargar la colección desde un archivo JSON.
2. **libreria_pep8.py:** Implementación de la clase "Libreria" siguiendo las convenciones de estilo PEP 8.
3. **libreria_pep257.py:** Implementación de la clase "Libreria" con docstrings siguiendo las convenciones de estilo PEP 257.
4. **test.py:** Archivo que contiene las pruebas unitarias para verificar el funcionamiento correcto de los métodos en las clases "Libreria". Estas pruebas cubren casos típicos, casos extremos y errores de entrada utilizando el módulo "unittest" de Python.
5. **nuevo_metodo.txt:** Archivo de texto que describe un nuevo método añadido a la clase "Libreria", junto con su prueba unitaria correspondiente.

### Uso de la biblioteca
Puedes utilizar la clase *Libreria* en tu propio proyecto Python para gestionar una colección de libros. Aquí hay un ejemplo básico de cómo puedes utilizarla:

#####Python

```python
from libreria import Libreria

# Crear una instancia de la clase Libreria
mi_libreria = Libreria()

# Añadir un libro a la colección
mi_libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)

# Buscar libros por autor
libros_de_garcia_marquez = mi_libreria.buscar_por_autor("Gabriel García Márquez")
for libro in libros_de_garcia_marquez:
    print(libro)
```

###Pruebas Unitarias
Las pruebas unitarias en el archivo *"test.py"* cubren una amplia gama de casos para garantizar el correcto funcionamiento de los métodos en las clases "Libreria". Esto incluye **casos típicos para escenarios comunes, casos extremos para situaciones inusuales y errores de entrada para manejar situaciones inesperadas.**

###Nuevo método agregado
Se agregó un nuevo método a la clase "Libreria" para mejorar su funcionalidad. Puedes encontrar detalles sobre este nuevo método en el archivo de texto *"nuevo_metodo.txt"*, junto con su prueba unitaria correspondiente.

###Depuración (Debugging)
Se utilizaron técnicas de debugging durante el desarrollo de la biblioteca para identificar y corregir errores. Esto garantiza que la biblioteca funcione correctamente y sea confiable para su uso.
###Contribución
Si encuentras algún problema o tienes alguna sugerencia de mejora, no dudes en abrir un issue en este repositorio o enviar un pull request con tus cambios.

***¡Espero que esta biblioteca sea útil para ti!***   :tw-1f600:
