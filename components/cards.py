import streamlit as st

def crear_tarjeta(icono, titulo, descripcion, pagina=None):

    with st.container(border=True):

        st.markdown(f"### {icono} {titulo}")

        st.write(descripcion)

        st.write("")

        if pagina:
            if st.button(
                f"Abrir {titulo}",
                use_container_width=True,
                key=titulo
            ):
                st.switch_page(pagina)