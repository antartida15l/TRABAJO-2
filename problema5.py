import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title('Tiempo de entrenamiento vs Tamaño del lote (Batch size)')
st.write('')
batch_size = st.slider('Tamaño del lote', 16, 128, 16)  

def tiempo_entrenamiento(x):
    return (1000 / x) + 0.1 * x

x_val = np.arange(16, 129, 1)
tiempos = tiempo_entrenamiento(x_val)
min_index = np.argmin(tiempos)
batch_size_min = x_val[min_index]
tiempo_min = tiempos[min_index]
tiempo_actual = tiempo_entrenamiento(batch_size)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_val, tiempos, label='Tiempo de entrenamiento', color='b')
ax.axvline(x=batch_size_min, color='r', linestyle='--', label=f'Mínimo global en x={batch_size_min} (Tiempo: {tiempo_min:.2f})')
ax.axvline(x=batch_size, color='g', linestyle='--', label=f'Tamaño de lote seleccionado: {batch_size} (Tiempo: {tiempo_actual:.2f})')

ax.set_title('Tiempo de entrenamiento vs Tamaño del lote (Batch size)')
ax.set_xlabel('Tamaño del lote (Batch size)')
ax.set_ylabel('Tiempo de entrenamiento')
ax.grid(True)
ax.legend()
st.pyplot(fig)
st.write(f'El tamaño de lote que minimiza el tiempo de entrenamiento es: {batch_size_min} con un tiempo de {tiempo_min:.2f} ')
st.write(f'El tiempo de entrenamiento para el tamaño de lote seleccionado ({batch_size}) es: {tiempo_actual:.2f}')
