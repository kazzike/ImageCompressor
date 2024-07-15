import os  # Proporciona una forma de usar funcionalidades dependientes del sistema operativo como leer o escribir en el sistema de archivos.
import re  # Proporciona herramientas para trabajar con expresiones regulares, permitiendo buscar y manipular cadenas de texto de manera eficiente.
from PIL import Image  # PIL (Python Imaging Library) es una biblioteca que permite abrir, manipular y guardar diferentes tipos de archivos de imagen.
from tqdm import tqdm  # Proporciona una barra de progreso visual en la terminal para iteraciones, útil para mostrar el progreso de bucles largos.
from datetime import datetime  # Proporciona clases para manipular fechas y horas, permitiendo realizar operaciones y formatear fechas y horas de manera sencilla.


def sanitize_filename(filename):
    """
    Elimina caracteres especiales y espacios del nombre de archivo.
    
    Args:
    filename (str): El nombre original del archivo.
    
    Returns:
    str: El nombre del archivo sin caracteres especiales ni espacios.
    """
    return re.sub(r'[^\w\s.-]', '', filename)

def compress_image(input_path, output_path, quality):
    """
    Comprime y guarda una imagen con la calidad especificada.

    Args:
    input_path (str): Ruta al archivo de imagen original.
    output_path (str): Ruta donde se guardará la imagen comprimida.
    quality (int): Calidad de compresión (0-100).

    Returns:
    tuple: (bool, float, float) Indicador de éxito, tamaño original en KB, nuevo tamaño en KB.
    """
    try:
        # Cargar la imagen usando Pillow
        img = Image.open(input_path)

        # Comprimir y guardar la imagen con la calidad especificada
        img.save(output_path, quality=quality)

        # Calcular el tamaño original y el nuevo tamaño en KB
        original_size = os.path.getsize(input_path) / 1024  # en KB
        new_size = os.path.getsize(output_path) / 1024  # en KB

        # Retornar éxito y tamaños
        return True, original_size, new_size

    except Exception as e:
        # Manejar errores y retornar False en caso de falla
        print(f"Error procesando {input_path}: {e}")
        return False, 0, 0

def main():
    """
    Función principal que maneja el flujo del programa.
    Presenta un menú al usuario, obtiene la opción seleccionada,
    procesa las imágenes en el directorio actual,
    y muestra una barra de progreso y estadísticas.
    """
    # Mostrar el menú y obtener la opción del usuario
    print("Compresor de Imágenes")
    print("Ingrese la opción a utilizar")
    print("1) Comprimir 25%")
    print("2) Comprimir 50%")
    print("3) Comprimir 75%")

    option = input("Opción: ").strip()

    # Configurar la calidad de compresión según la opción elegida
    if option == '1':
        quality = 75
    elif option == '2':
        quality = 50
    elif option == '3':
        quality = 25
    else:
        print("Opción no válida")
        return

    # Obtener el directorio actual y listar los archivos de imagen
    folder_path = os.getcwd()
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.webp', '.png', '.gif', '.bmp'))]

    # Configurar la barra de progreso
    progress_bar = tqdm(image_files, desc="Processing", unit="image")

    processed_count = 0
    start_time = datetime.now()

    # Procesar cada archivo de imagen
    for image_file in progress_bar:
        base, ext = os.path.splitext(image_file)
        sanitized_name = sanitize_filename(base)
        new_name = f"{sanitized_name}_zipped{ext.lower()}"
        input_path = os.path.join(folder_path, image_file)
        output_path = os.path.join(folder_path, new_name)

        # Comprimir las imágenes y actualizar el conteo
        success, original_size, new_size = compress_image(input_path, output_path, quality=quality)
        if success:
            processed_count += 1

        # Actualizar la barra de progreso con los tamaños de los archivos
        progress_bar.set_postfix({"Processed": processed_count, "Original KB": f"{original_size:.2f}", "New KB": f"{new_size:.2f}"})

    end_time = datetime.now()
    elapsed_time = end_time - start_time

    # Mostrar mensaje de finalización y estadísticas
    print(f"\nCompresión de imágenes completa.")
    print(f"Archivos procesados: {processed_count}")
    print(f"Tiempo total: {elapsed_time}")

if __name__ == "__main__":
    main()
