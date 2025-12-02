from pathlib import Path
import csv

def leer_csv_login(ruta_relativa_desde_raiz):
    ruta_script = Path(__file__).resolve()
    ruta_raiz = ruta_script.parent.parent
    ruta_absoluta = ruta_raiz / ruta_relativa_desde_raiz

    if not ruta_absoluta.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {ruta_absoluta}")

    datos = []

    with open(ruta_absoluta, newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo, delimiter=',')

        for fila in lector:
            usuario = fila["usuario"].strip()
            password = fila["password"].strip()
            debe_funcionar = fila["debe_funcionar"].strip().lower() == 'true'
            datos.append((usuario, password, debe_funcionar))

    return datos
