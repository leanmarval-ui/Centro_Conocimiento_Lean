import streamlit as st
import os
from datetime import datetime

from config import *
from components.hero import mostrar_hero
from components.cards import crear_tarjeta
from components.metrics import mostrar_metricas
from components.welcome import mostrar_bienvenida

# ---------------------------------------
# Configuración de la aplicación
# ---------------------------------------

st.set_page_config(
    page_title=APP_NAME,
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------
# Encabezado
# ---------------------------------------

mostrar_hero()

# ---------------------------------------
# Bienvenida
# ---------------------------------------

mostrar_bienvenida()

st.markdown("---")

st.markdown("## 📊 Resumen del Área")

mostrar_metricas()

archivo = "data/Centro_Conocimiento_LEAN.xlsx"

fecha_actualizacion = datetime.fromtimestamp(
    os.path.getmtime(archivo)
).strftime("%d/%m/%Y %H:%M")

st.info(
    f"""
**Versión:** 1.0.0

**Última actualización:** {fecha_actualizacion}

**Responsable:** Área LEAN - Marval

**Estado:** En producción interna del Área LEAN
"""
)

st.markdown("---")

st.markdown("## ⭐ Accesos rápidos")

col1, col2 = st.columns(2)

with col1:

    crear_tarjeta(
        "🛠",
        "Herramientas",
        "Consulta las plataformas utilizadas por el Área LEAN.",
        "pages/01_🛠_Herramientas.py"
    )

    crear_tarjeta(
        "📊",
        "Indicadores",
        "Consulta dashboards e indicadores.",
        "pages/03_📊_Indicadores.py"
    )

with col2:

    crear_tarjeta(
        "💻",
        "Desarrollos",
        "Consulta aplicaciones y automatizaciones.",
        "pages/02_💻_Desarrollos.py"
    )

    crear_tarjeta(
        "📚",
        "Documentación",
        "Consulta manuales y procedimientos.",
        "pages/05_📚_Documentacion.py"
    )