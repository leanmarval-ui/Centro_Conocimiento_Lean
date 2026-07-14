import streamlit as st
from utils.data_loader import contar_registros

def mostrar_metricas():

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🛠 Herramientas", contar_registros("Herramientas"))

    with col2:
        st.metric("💻 Desarrollos", contar_registros("Desarrollos"))

    with col3:
        st.metric("📊 Indicadores", contar_registros("Indicadores"))

    with col4:
        st.metric("📋 Procesos", contar_registros("Procesos"))

    col5, col6, col7 = st.columns(3)

    with col5:
        st.metric("📚 Documentación", contar_registros("Documentación"))

    with col6:
        st.metric("👥 Equipo Lean", contar_registros("Equipo"))

    with col7:
        st.metric("🚀 Backlog Analytics", contar_registros("Backlog"))