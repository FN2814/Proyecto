# Proyecto
 e-actividad 3.1 - Diseño web con HTML & CSS.

# Sitio Web de Ciberseguridad

Este proyecto consiste en el desarrollo de un sitio web para una empresa ficticia de ciberseguridad. El sitio incluye una página de inicio, una sección sobre la empresa, una página de servicios y una página de contacto.

## Requisitos Previos

- Python 3
- Flask
- Flask-CORS
- Navegador web moderno

## Instalación y Configuración

### Paso 1: Clonar o Descargar el Proyecto

Clona el repositorio o descarga los archivos del proyecto a tu máquina local.

Usa el siguiente enlace:

- https://github.com/FN2814/Proyecto.git

### Paso 2: Instalar Dependencias

Navega a la carpeta `backend` e instala las dependencias necesarias ejecutando los siguientes comandos:

```bash
pip install flask flask-cors
```

### Paso 3: Ejecución del Servidor Backend

## Paso 1: Iniciar el Servidor Flask
Para iniciar el servidor backend, navega a la carpeta backend y ejecuta el archivo app.py:

```bash
cd /ruta/a/tu/proyecto/backend
python app.py
```

##Paso 2: Verificación del Servidor
En la terminal en la que estás ejecutando tu servidor verás el contenido correspondiente que indica que todo está funcionando bien.

De igual manera podrías intentar entrando en la dirección: 

####127.0.0.1:5000

# Uso del Sitio Web

## Navegación por las Páginas

- Página de Inicio: Abre pages/index.html en tu navegador.
- Sobre Nosotros: Abre pages/about.html en tu navegador.
- Servicios: Abre pages/services.html en tu navegador.
- Contacto: Abre pages/contact.html en tu navegador.

##Uso del Formulario de Contacto

- Rellenar el Formulario: Ingrese los datos requeridos en el formulario de contacto.
- Enviar el Formulario: Haga clic en el botón "Enviar".
- Verificar la Respuesta: Se mostrará un mensaje indicando si los datos se guardaron correctamente.

## Verificación de Datos Guardados

Ejecuta el script para ver los datos almacenados:

```bash
python query_db.py
```

Esto se explicará de forma más clara posteriormente

# Consulta de la Base de Datos
Para verificar que los datos se han guardado correctamente, puede ejecutar un script Python para consultar la base de datos:

```python
import sqlite3

def fetch_data():
    try:
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM contacts")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print("Error al consultar la base de datos:", e)
    finally:
        if con:
            con.close()

if __name__ == '__main__':
    fetch_data()
```

Ejecuta el script para ver los datos almacenados:

```bash
python query_db.py
```

#Contribuciones
Las contribuciones al proyecto son bienvenidas. Por favor comunicarse a cardozaferrerje@uvm.edu.ve para proponer algún cambio

##Estructura del proyecto

Para mayor información sobre la estructura del proyecto, consulta el directorio: 

Proyecto 1.0/documentation/estructura_proyecto.md
