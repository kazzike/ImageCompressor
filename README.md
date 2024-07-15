# Image Compressor

Este script de Python comprime imágenes usando la biblioteca Pillow. El script permite a los usuarios elegir entre tres niveles de compresión (25%, 50%, y 75%) y procesa todas las imágenes en el directorio actual.

Requisitos
- Python 3.x
- Pillow -> ```Pip install pillow```


- tqdm -> `pip install tqdm`

Uso
----

1. Asegúrate de tener instaladas las dependencias mencionadas en la sección de Requisitos.
2. Guarda el script como `image_compressor.py` en el directorio donde deseas comprimir las imágenes.
3. Ejecuta el script con el comando `python image_compressor.py`.
4. Elige la opción de compresión deseada (25%, 50%, o 75%).
5. El script procesará todas las imágenes en el directorio actual y mostrará una barra de progreso.
6. Las imágenes comprimidas se guardarán en el mismo directorio con el sufijo `_zipped` en el nombre del archivo.
7. Al finalizar, el script mostrará el número de archivos procesados y el tiempo total de ejecución.

Funciones
---------

### `sanitize_filename(filename)`

Esta función elimina los caracteres especiales y espacios del nombre de archivo para evitar problemas durante la compresión.

### `compress_image(input_path, output_path, quality)`

Esta función comprime una imagen utilizando la biblioteca Pillow. Toma tres argumentos: la ruta de entrada de la imagen, la ruta de salida de la imagen comprimida, y la calidad de compresión (un valor entre 0 y 100). La función retorna un valor booleano indicando si la compresión fue exitosa, así como los tamaños original y nuevo de la imagen en KB.

### `main()`

La función principal del script. Muestra el menú al usuario, obtiene la opción elegida, y procesa todas las imágenes en el directorio actual. También muestra una barra de progreso y estadísticas al finalizar.
