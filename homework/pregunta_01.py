# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import os
import zipfile
import csv

def extract_zip(zip_file: str, destination: str):

    if not os.path.isdir(destination):
        with zipfile.ZipFile(zip_file, "r") as archive:
            archive.extractall(path=os.path.dirname(destination))



def write_to_csv(datos: list[dict], directorio: str, nombre_archivo: str):

    os.makedirs(directorio, exist_ok=True)
    ruta_salida = os.path.join(directorio, f"{nombre_archivo}.csv")
    
    with open(ruta_salida, "w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=["phrase", "target"])
        escritor.writeheader()
        escritor.writerows(datos)

def parse_text_files(source_folder: str) -> list[dict]:

    registros = []
    for clase in sorted(os.listdir(source_folder)):
        clase_path = os.path.join(source_folder, clase)
        if os.path.isdir(clase_path):
            for archivo in os.listdir(clase_path):
                ruta = os.path.join(clase_path, archivo)
                with open(ruta, "r", encoding="utf-8") as f:
                    contenido = f.read().strip()
                    registros.append({"phrase": contenido, "target": clase})
    return registros


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```

    """
    
    
    zip_input = "files/input.zip"
    input_root = "files/input"
    output_path = "files/output"

    # Paso 1: Extraer archivo ZIP
    extract_zip(zip_input, input_root)

    # Paso 2 y 3: Procesar train y test, y guardar como CSV
    for split in ["train", "test"]:
        folder = f"{input_root}/{split}"
        entries = parse_text_files(folder)
        write_to_csv(entries, output_path, f"{split}_dataset")

if __name__ == "__main__":
    pregunta_01()