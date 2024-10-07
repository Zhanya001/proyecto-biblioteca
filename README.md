# Biblioteca: Sistema de Préstamo y Devolución de Libros y Revistas

Este proyecto implementa un sistema para gestionar el préstamo y devolución de libros y revistas en una biblioteca. Cada libro tiene un código ISBN, y cada revista tiene un número de edición. El sistema permite registrar el préstamo y devolución de estos ítems, manteniendo un control del inventario total y de los elementos prestados.

## Características

- **Gestión completa**: Registro de libros y revistas con posibilidad de préstamo y devolución.
- **Estructura orientada a objetos**: Uso de clases abstractas y herencia.
- **Control de inventario**: Seguimiento del total de ítems y los prestados.
- **Simulación en Jupyter Notebook**: Puedes probar el funcionamiento directamente en Jupyter.

## Requisitos

- **Python 3.7+**
- **Jupyter Notebook** para ejecutar el proyecto de manera interactiva.

## Instalación

### Paso 1: Clonar el repositorio

1. Clona el repositorio a tu máquina local:

```bash
git clone https://github.com/usuario/proyecto-biblioteca.git
cd proyecto-biblioteca
```

2. Crea un entorno virtual para aislar las dependencias del proyecto utilizando los siguientes comandos:

En macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

En Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

4. Para ejecutar el proyecto, abre Jupyter Notebook ejecutando el siguiente comando:

```bash
jupyter notebook
```

Luego, navega al archivo .ipynb del proyecto y ejecútalo en celdas.

# Estructura del Proyecto
El proyecto está organizado utilizando clases que representan los ítems de la biblioteca:

ItemBiblioteca: Clase abstracta base para representar un ítem (libro o revista).
Libro: Hereda de ItemBiblioteca y añade el atributo ISBN.
Revista: Hereda de ItemBiblioteca y añade el número de la revista.

# Ejemplo de Uso
A continuación, se muestra un ejemplo de cómo crear un libro, prestarlo y devolverlo.

```bash
# Creación de un libro
libro1 = Libro("L1_123", "La Bestia", "9788408249849")
print(libro1)

# Préstamo del libro
libro1.prestar()

# Devolución del libro
libro1.devolver()
```

Resultados esperados:

```bash
L1_123 - La Bestia - NO PRESTADO (9788408249849)
L1_123 - PRESTADO
L1_123 - DEVUELTO
```

.gitignore
El archivo .gitignore está configurado para ignorar archivos innecesarios que no deben ser incluidos en el repositorio, tales como:

Entornos virtuales (venv/)
Cachés de Python (__pycache__/)
Archivos de configuración locales (.vscode/, .idea/)
Checkpoints de Jupyter (.ipynb_checkpoints/)

# Contacto
Si tienes preguntas o deseas más información, puedes contactarme a través de LinkedIn: [Ariet Michal](https://www.linkedin.com/in/ariet-michal).
