# Proyecto de Categorización de Noticias

## Descripción
Este proyecto aborda el problema de categorización de noticias de la manera más eficiente posible, implementando soluciones específicas para responder a cada una de las preguntas planteadas en los problemas.

## Requisitos
Para ejecutar este proyecto, es necesario contar con un entorno virtual que tenga una versión de **Python** entre **3.8 y 3.11**, ya que la librería **TensorFlow**, utilizada en el desarrollo, es compatible dentro de este rango de versiones.

Se recomienda el uso de **Conda** para la gestión del entorno virtual.

## Instalación
### 1. Crear un entorno virtual
Si utilizas **Conda**, puedes crear y activar un entorno con el siguiente comando:
```bash
conda create --name noticias_env python=3.10 -y
conda activate noticias_env
```

### 2. Instalar dependencias
Para asegurarte de que todas las librerías necesarias estén presentes, ejecuta:
```bash
pip install -r requirements.txt
```

## Estructura del Proyecto
El dataset debe estar ubicado en la siguiente ruta dentro del proyecto:
```
categorizacion_noticias/
│── data/
│   └── data.json
│── catalogar_noticias.py
│── autores.py
│── estilos_escritura.py
│── informacion_util.py
│── requirements.txt
```
Colocar el archivo en la ubicación correcta garantizará que los scripts puedan acceder a los datos sin problemas.

## Ejecución del Proyecto
Para ejecutar el análisis de noticias, corre los scripts en el siguiente orden:
```bash
python catalogar_noticias.py
python autores.py
python estilos_escritura.py
python informacion_util.py
```

## Notas
- Asegúrate de que el entorno virtual esté activado antes de ejecutar los scripts.
- Revisa que el dataset esté correctamente ubicado en la carpeta **data/**.

¡Listo! Con esto, el proyecto debería ejecutarse sin inconvenientes. 🚀

