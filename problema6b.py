import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

ancho_banda_total = 1000  
max_archivos = 50
archivos_extras = 30
st.title('Sistema de Transmisión de Datos')
st.write('')
n_archivos = st.slider('Número de Archivos a Transmitir', 1, max_archivos, 1)
ancho_banda_por_archivo = st.slider('Ancho de Banda por Archivo (Mbps)', 1, 100, 10)

if n_archivos <= archivos_extras:
    ancho_banda_usado = n_archivos * ancho_banda_por_archivo
    ancho_banda_disponible = ancho_banda_total - ancho_banda_usado
    d = ancho_banda_total
else:
    ancho_banda_reducido = ancho_banda_total * (1 - 0.05 * (n_archivos - archivos_extras))
    ancho_banda_usado = n_archivos * ancho_banda_por_archivo
    ancho_banda_disponible = ancho_banda_reducido - ancho_banda_usado
    d = ancho_banda_reducido

st.write(f'Ancho de banda utilizado: {ancho_banda_usado:.2f} Mbps')
st.write(f'Ancho de banda disponible: {ancho_banda_disponible:.2f} Mbps')
st.write(f'Ancho de banda TOTAL: {d:.2f} Mbps')

if ancho_banda_usado > d:
    st.write(f'⚠️ **Exceso de ancho de banda!** El sistema está utilizando más de {d} Mbps.')
x_values = np.arange(1, max_archivos + 1)
ancho_banda_disponible_list = []
for n in x_values:
    if n <= archivos_extras:
        ancho_banda_disponible_list.append(ancho_banda_total)
    else:
        ancho_banda_disponible_list.append(ancho_banda_total * (1 - 0.05 * (n - archivos_extras)))

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_values, ancho_banda_disponible_list, label='Ancho de Banda Disponible (Mbps)', color='b')
ax.axhline(y=ancho_banda_total, color='r', linestyle='--', label='Ancho de Banda Total (1000 Mbps)')
ax.axvline(x=30, color='red', linestyle='--', label='Límite sin penalización')
ax.axvline(x=n_archivos, color='green', linestyle='--', label=f'Archivos Seleccionados: {n_archivos}')
ax.set_title('Relación entre Número de Archivos y Ancho de Banda Disponible')
ax.set_xlabel('Número de Archivos Transmitidos')
ax.set_ylabel('Ancho de Banda Disponible (Mbps)')
ax.grid(True)
ax.legend()
st.pyplot(fig)

