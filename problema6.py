import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def calcular_ancho_banda(archivos_transmitidos, ancho_banda_total=1000):
    if archivos_transmitidos > 30:
        archivos_extra = archivos_transmitidos - 30
        reduccion = (5 / 100) * archivos_extra
        ancho_banda_disponible = ancho_banda_total * (1 - reduccion)
    else:
        ancho_banda_disponible = ancho_banda_total
    
    return max(0, ancho_banda_disponible)

def maximizar_archivos(x, ancho_banda_total=1000):
    for archivos in range(50, 0, -1):  
        ancho_banda_disponible = calcular_ancho_banda(archivos, ancho_banda_total)
        if archivos * x <= ancho_banda_disponible:  
            return archivos, ancho_banda_disponible
    return 0, 0

st.title("Maximización de Transmisión de Archivos con Gráfico")
x = st.slider("Ancho de banda por archivo (Mbps)", min_value=1, max_value=100, value=20)
ancho_banda_total = st.slider("Ancho de banda total del sistema (Mbps)", min_value=500, max_value=2000, value=1000)
if st.button("Calcular Máximo de Archivos"):
    archivos_max, ancho_banda_restante = maximizar_archivos(x, ancho_banda_total)
    st.write(f"Número máximo de archivos que se pueden transmitir: {archivos_max}")
    st.write(f"Ancho de banda disponible restante: {ancho_banda_restante:.2f} Mbps")
    archivos = np.arange(1, 51)
    ancho_banda_disponible = [calcular_ancho_banda(a, ancho_banda_total) for a in archivos]
    fig, ax = plt.subplots()
    ax.plot(archivos, ancho_banda_disponible, label='Ancho de banda disponible (Mbps)')
    ax.axvline(x=30, color='red', linestyle='--', label='Límite sin penalización')
    ax.axvline(x=archivos_max, color='green', linestyle='--', label=f'Máximo Archivos: {archivos_max}')
    ax.set_xlabel('Número de archivos transmitidos')
    ax.set_ylabel('Ancho de banda disponible (Mbps)')
    ax.set_title('Relación entre número de archivos y ancho de banda disponible')
    ax.legend()
    st.pyplot(fig)
