import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title('Uso de CPU vs Número de peticiones procesadas por segundo')
st.write('')
limite_uso_cpu = st.slider('Límite máximo de uso de CPU (%)', 50, 100, 80)
max_peticiones = st.slider('Máximo de peticiones procesadas por segundo', 5, 50, 20)

def uso_cpu(x):
    return 2 * x**2 + 10 * x

x_val = np.arange(0, max_peticiones + 1, 0.1)
uso_cpu_values = uso_cpu(x_val)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_val, uso_cpu_values, label='Uso de CPU', color='b')
ax.axhline(limite_uso_cpu, color='r', linestyle='--', label=f'Límite del {limite_uso_cpu}% de CPU')
ax.set_title('Uso de CPU vs Número de peticiones procesadas por segundo')
ax.set_xlabel('Número de peticiones procesadas por segundo')
ax.set_ylabel('Uso de CPU (%)')
ax.grid(True)
ax.legend()
st.pyplot(fig)
