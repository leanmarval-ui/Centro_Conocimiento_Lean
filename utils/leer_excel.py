import pandas as pd


ARCHIVO = "data/Centro_Conocimiento_LEAN.xlsx"


def leer_hoja(nombre_hoja):
    """
    Lee una hoja del archivo maestro.
    """

    return pd.read_excel(
        ARCHIVO,
        sheet_name=nombre_hoja
    )