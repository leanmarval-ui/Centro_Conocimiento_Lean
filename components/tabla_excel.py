import streamlit as st
from utils.data_loader import leer_hoja


def mostrar_tabla(nombre_hoja, titulo):

    st.title(titulo)

    df = leer_hoja(nombre_hoja)

    # Buscador
    buscar = st.text_input(
        "🔍 Buscar",
        placeholder="Escribe una palabra..."
    )

    if buscar:
        df = df[
            df.astype(str)
              .apply(
                  lambda fila: fila.str.contains(
                      buscar,
                      case=False,
                      na=False
                  ).any(),
                  axis=1
              )
        ]

    if df.empty:
        st.warning("No se encontraron registros.")
        return

    st.success(f"Se encontraron {len(df)} registros.")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Descargar información",
        data=csv,
        file_name=f"{nombre_hoja}.csv",
        mime="text/csv",
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )