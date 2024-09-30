import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title('Tiempo de respuesta vs Número de trabajos procesados')
st.write('')
max_x = st.slider('Selecciona el número de trabajos procesados por segundo', 5, 20, 20)

def tiempo_respuesta(x):
    return (100 / x) + 2 * x

x_val = np.arange(5, max_x, 0.1)
tiempos = tiempo_respuesta(x_val)
x_optimo = np.sqrt(50)
t_optimo = tiempo_respuesta(x_optimo)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_val, tiempos, label='Tiempo de respuesta', color='b')
ax.axvline(x_optimo, color='r', linestyle='--', label=f'Mínimo en x={x_optimo:.2f}')
ax.scatter(x_optimo, t_optimo, color='r', zorder=5)
ax.set_title('Tiempo de respuesta vs Número de trabajos procesados')
ax.set_xlabel('Número de trabajos por segundo')
ax.set_ylabel('Tiempo de respuesta')
ax.grid(True)
ax.legend()
st.pyplot(fig)
