import streamlit as st


def mostrar_hero():

    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        st.image("assets/logos/logo_lean.jpg", width=140)

    with col2:

        st.markdown(
            """
            <div style='text-align:center;'>

            <h1 style='color:#1C4D78; margin-bottom:0;'>
            Centro de Conocimiento LEAN
            </h1>

            <h3 style='color:#4F6F8F; margin-top:5px;'>
            Área LEAN - Marval
            </h3>

            <p style='font-size:18px; color:#555555;'>

            Organizar • Estandarizar • Compartir • Mejorar

            </p>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.image("assets/logos/logo_marval.jpg", width=150)

    st.divider()