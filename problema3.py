import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title('Tiempo de ejecución del script vs Número de datos procesados')
st.write('')
limite_tiempo = st.slider('Límite máximo de tiempo (segundos)', 10, 100, 50) 

def tiempo_ejecucion(x):
    return 5 * x + 2

x_val = np.arange(0, 11)  
tiempos = tiempo_ejecucion(x_val)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_val, tiempos, label='Tiempo de ejecución', color='b', marker='o')
ax.axhline(limite_tiempo, color='r', linestyle='--', label=f'Límite de {limite_tiempo} segundos')
ax.set_title('Tiempo de ejecución del script vs Número de datos procesados')
ax.set_xlabel('Número de datos procesados')
ax.set_ylabel('Tiempo de ejecución (segundos)')
ax.grid(True)
ax.legend()

st.pyplot(fig)
