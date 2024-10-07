#IMPORTAR LIBRERIAS

from abc import ABC, abstractmethod
from typing import ClassVar

# DEFINIR LA CLASE BASE ItemBiblioteca

# Clase abstracta que sirve como base para todos los elementos de la biblioteca
class ItemBiblioteca(ABC):
    """Clase base abstracta para representar un material de biblioteca (libro o revista)."""
    
    # Variables de clase para llevar el seguimiento de los elementos y los prestados
    total_items: ClassVar[int] = 0
    total_prestados: ClassVar[int] = 0

    def __init__(self, codigo: str, titulo: str):
        """Constructor de un ítem de la biblioteca."""
        self._codigo = codigo
        self._titulo = titulo
        self._esta_prestado = False
        ItemBiblioteca.incrementar_total_items()

    @classmethod
    def incrementar_total_items(cls):
        """Incrementa el total de ítems en la biblioteca."""
        cls.total_items += 1

    @classmethod
    def decrementar_total_items(cls):
        """Decrementa el total de ítems en la biblioteca."""
        cls.total_items -= 1

    @classmethod
    def incrementar_prestados(cls):
        """Incrementa el contador de ítems prestados."""
        cls.total_prestados += 1

    @classmethod
    def decrementar_prestados(cls):
        """Reduce el número de ítems prestados."""
        cls.total_prestados -= 1

    @property
    def codigo(self):
        """Retorna el código interno del ítem."""
        return self._codigo

    @codigo.setter
    def codigo(self, nuevo_codigo: str):
        """Permite modificar el código interno."""
        self._codigo = nuevo_codigo

    @property
    def titulo(self):
        """Devuelve el título del ítem."""
        return self._titulo

    @titulo.setter
    def titulo(self, nuevo_titulo: str):
        """Permite modificar el título del ítem."""
        self._titulo = nuevo_titulo

    @property
    def esta_prestado(self):
        """Indica si el ítem está prestado."""
        return self._esta_prestado

    def prestar(self):
        """Marca el ítem como prestado si no lo está ya."""
        if not self._esta_prestado:
            self._esta_prestado = True
            ItemBiblioteca.incrementar_prestados()
            print(f"{self._codigo} - PRESTADO")
        else:
            print(f"{self._codigo} ya está prestado.")

    def devolver(self):
        """Marca el ítem como devuelto si estaba prestado."""
        if self._esta_prestado:
            self._esta_prestado = False
            ItemBiblioteca.decrementar_prestados()
            print(f"{self._codigo} - DEVUELTO")
        else:
            print(f"{self._codigo} no estaba prestado.")

    @abstractmethod
    def __str__(self):
        """Método abstracto para representar el ítem como cadena de texto."""
        pass

# DEFINIR LA CLASE Libro

# Clase Libro que hereda de ItemBiblioteca
class Libro(ItemBiblioteca):
    """Clase que representa un libro, con su código ISBN."""
    
    total_libros: ClassVar[int] = 0

    def __init__(self, codigo: str, titulo: str, isbn: str):
        """Constructor de un libro."""
        super().__init__(codigo, titulo)
        self._isbn = isbn
        Libro.incrementar_total_libros()

    @classmethod
    def incrementar_total_libros(cls):
        """Incrementa el total de libros en la biblioteca."""
        cls.total_libros += 1

    @property
    def isbn(self):
        """Devuelve el ISBN del libro."""
        return self._isbn

    def __str__(self):
        estado = "PRESTADO" if self._esta_prestado else "NO PRESTADO"
        return f"{self._codigo} - {self._titulo} - {estado} ({self._isbn})"
    
#DEFINIR LA CLASE REVISTA

# Clase Revista que hereda de ItemBiblioteca
class Revista(ItemBiblioteca):
    """Clase que representa una revista, con su número."""
    
    total_revistas: ClassVar[int] = 0

    def __init__(self, codigo: str, titulo: str, numero: str):
        """Constructor de una revista."""
        super().__init__(codigo, titulo)
        self._numero = numero
        Revista.incrementar_total_revistas()

    @classmethod
    def incrementar_total_revistas(cls):
        """Incrementa el total de revistas en la biblioteca."""
        cls.total_revistas += 1

    @property
    def numero(self):
        """Devuelve el número de la revista."""
        return self._numero

    def __str__(self):
        estado = "PRESTADO" if self._esta_prestado else "NO PRESTADO"
        return f"{self._codigo} - {self._titulo} - {estado} ({self._numero})"


#SIMULACION DE LAS ACCIONES

# Simulación de acciones con libros y revistas en la biblioteca
libro1 = Libro("L1_123", "La Bestia", "9788408249849")
print("Mi primer libro es: ", libro1)
print("Número ejemplares totales:", libro1.total_items)
print("Número libros totales:", libro1.total_libros)
print("Número ejemplares prestados:", libro1.total_prestados, "\n")

libro2 = Libro("L2_345", "Últimos días en Berlín", "9788408249856")
print("Mi segundo libro es: ", libro2)
print("Número ejemplares totales:", libro1.total_items)
print("Número libros totales:", libro1.total_libros)
print("Número ejemplares prestados:", libro1.total_prestados, "\n")

revista1 = Revista("R1_JDJ", "National Geographic", "5")
print("Mi primera revista es: ", revista1)
print("Número ejemplares totales:", revista1.total_items)
print("Número revistas totales:", revista1.total_revistas)
print("Número ejemplares prestados:", revista1.total_prestados, "\n")

revista2 = Revista("R2_ADA", "National Geographic", "23")
print("Mi segunda revista es: ", revista2)
print("Número ejemplares totales:", revista1.total_items)
print("Número revistas totales:", revista1.total_revistas)
print("Número ejemplares prestados:", revista1.total_prestados, "\n")

# Simulación de acciones de préstamo y devolución
revista1.prestar()
libro1.prestar()
print("Número ejemplares prestados:", libro1.total_prestados)
libro1.devolver()
print("Número ejemplares prestados:", libro1.total_prestados, "\n")

