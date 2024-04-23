# RootMap CLI

Este script de Python genera un archivo de texto visualizando la estructura de directorios de un proyecto,
excluyendo directorios y archivos específicos que no son relevantes para la vista general del usuario.

## Características

- Excluye automáticamente directorios de dependencias comunes como `node_modules`, `vendor` y `target`.
- Filtra archivos y directorios basados en patrones específicos, como hashes de Git.
- Ordena directorios y archivos dentro de cada directorio padre conforme al estilo de Visual Studio Code,
  mostrando primero directorios y luego archivos.

## Instalación de Dependencias

Este script utiliza módulos estándar de Python, por lo tanto no requiere la instalación de dependencias externas.
Asegúrate de tener Python instalado en tu sistema. Si decides implementar visualizaciones gráficas avanzadas
o añadir nuevas funcionalidades que requieran módulos externos, deberás gestionar las dependencias correspondientes.

## Uso del Script

Para usar este script, sigue estos pasos:
1. Guarda el script en un archivo, por ejemplo `directory_tree.py`.
2. Abre la terminal o línea de comandos.
3. Ejecuta el script pasando el directorio que deseas explorar como argumento:
   ```bash
   python directory_tree.py -o output.txt /path/to/directory
   ```
   - `-o output.txt` es opcional. Si no se especifica, el nombre del archivo por defecto será `directory_tree.txt`.
   - Reemplaza `/path/to/directory` con la ruta real que deseas escanear.

## Ejemplo de Salida
La salida en el archivo será similar a esto, dependiendo de la estructura del directorio que explores:
   ```
   notes-app/
   │
   ├── src/
   │   ├── assets/
   │   │   ├── images/
   │   │   └── styles/
   │   │
   │   ├── components/
   │   │   ├── NoteCard.js
   │   │   ├── NoteList.js
   │   │   └── SearchBar.js
   │   │
   │   ├── pages/
   │   │   ├── HomePage.js
   │   │   └── NotePage.js
   │   │
   │   ├── utils/
   │   │   └── storage.js
   │   │
   │   ├── app.js
   │   └── index.js
   │
   ├── public/
   │   ├── index.html
   │   └── favicon.ico
   │
   ├── tests/
   │   ├── components/
   │   └── utils/as
   │
   ├── package.json
   └── README.md
   ```

## Contribuciones
Las contribuciones para mejorar este script son bienvenidas. Considera clonar el repositorio y enviar tus cambios
para revisión a través de pull requests si deseas añadir funcionalidades o mejorar la eficiencia del código.

## Licencia
Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` en el repositorio para más detalles.
