import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Visualización de Gráficos", layout="wide")
sns.set(style="whitegrid")

st.title("📊 Visualización de Gráficos de Datos")

tab1, tab2, tab3, tab4 = st.tabs([
    "🚶‍♂️ Tiempo vs Distancia",
    "🛌 Edad vs Horas de Sueño",
    "⚙️ Velocidad vs Impurezas",
    "🎵 Ventas de la Industria Musical"
])

# --- TAB 1 ---
with tab1:
    st.subheader("Gráfico de Barras: Tiempo vs Distancia")
    datos1 = pd.DataFrame({
        "Tiempo": [15, 30, 45, 60],
        "Distancia": [3, 6, 9, 12]
    })
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    sns.barplot(
        x="Tiempo",
        y="Distancia",
        data=datos1,
        palette="Set2",
        order=datos1.sort_values("Tiempo", ascending=False)["Tiempo"]
    )
    plt.title("Distribución por categoría", fontsize=16)
    plt.xlabel("Tiempo")
    plt.ylabel("Distancia")
    for i, v in enumerate(datos1.sort_values("Tiempo", ascending=False)["Distancia"]):
        ax1.text(i, v + 0.5, str(v), ha="center", fontweight="bold")
    st.pyplot(fig1)

# --- TAB 2 ---
with tab2:
    st.subheader("Gráfico de Barras: Edad vs Horas de Sueño")
    datos2 = pd.DataFrame({
        "Edad": [1, 3, 6, 9, 12, 18, 24, 36],
        "horas de sueño": [16, 15, 14.10, 14, 13.50, 13.40, 13.30, 12]
    })
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    sns.barplot(
        x="Edad",
        y="horas de sueño",
        data=datos2,
        palette="Set2",
        order=datos2.sort_values("Edad", ascending=False)["Edad"]
    )
    plt.title("Distribución por categoría", fontsize=16)
    plt.xlabel("Edad")
    plt.ylabel("Horas de sueño")
    for i, v in enumerate(datos2.sort_values("Edad", ascending=False)["horas de sueño"]):
        ax2.text(i, v + 0.2, str(v), ha="center", fontweight="bold")
    st.pyplot(fig2)

# --- TAB 3 ---
with tab3:
    st.subheader("Gráfico de Dispersión: Velocidad vs Impurezas")
    datos3 = pd.DataFrame({
        "Velocidad": [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42],
        "Impurezas": [8.5, 9.5, 12, 10.5, 13.5, 15, 13.5, 15, 16.5, 16.5, 19, 18.5]
    })
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    sns.scatterplot(
        x="Velocidad",
        y="Impurezas",
        data=datos3,
        color="green",
        s=100
    )
    plt.title("Relación entre Velocidad e Impurezas", fontsize=16)
    plt.xlabel("Velocidad")
    plt.ylabel("Impurezas")
    st.pyplot(fig3)

# --- TAB 4 ---
with tab4:
    st.subheader("Gráfico de Dispersión: Ventas Discográficas por Año")
    datos4 = pd.DataFrame({
        "Año": [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009],
        "Ventas": [15, 14, 13.5, 13, 12, 12.5, 13, 12.5, 11, 9, 6]
    })
    fig4, ax4 = plt.subplots(figsize=(8, 5))
    sns.scatterplot(
        x="Año",
        y="Ventas",
        data=datos4,
        color="red",
        s=100
    )
    plt.title("Ventas Industria Musical Discográficas", fontsize=16)
    plt.xlabel("Año (1999–2009)")
    plt.ylabel("Ventas (en billones)")
    st.pyplot(fig4)
