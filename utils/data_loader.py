import pandas as pd

ARCHIVO = "data/Centro_Conocimiento_LEAN.xlsx"

def leer_hoja(nombre_hoja):
    return pd.read_excel(
        ARCHIVO,
        sheet_name=nombre_hoja
    )

def contar_registros(nombre_hoja):
    return len(leer_hoja(nombre_hoja))