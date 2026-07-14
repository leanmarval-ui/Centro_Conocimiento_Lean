import streamlit as st


def mostrar_encabezado(icono, titulo, descripcion):
    """
    Muestra el encabezado estándar de todas las páginas.
    """

    st.title(f"{icono} {titulo}")

    st.markdown(descripcion)

    st.divider()