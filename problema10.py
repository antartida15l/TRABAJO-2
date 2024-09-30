import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title('Latencia vs Número de Mensajes')
st.write('')

def latencia(x):
    return 100 - 2 * x

x_val = np.linspace(0, 60, 100)
latencias = latencia(x_val)
x_max = 40  

numero_mensajes = st.slider(
    'Selecciona el número de mensajes por segundo',
    min_value=0,
    max_value=60,
    value=0  
)

latencia_seleccionada = latencia(numero_mensajes)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_val, latencias, label='Latencia (ms)', color='b')
ax.axhline(y=20, color='r', linestyle='--', label='Latencia mínima de 20 ms')
ax.axvline(x=x_max, color='g', linestyle='--', label=f'Máximo en x={x_max}')
ax.plot(numero_mensajes, latencia_seleccionada, 'go', label='Seleccionado')
ax.set_title('Latencia vs Número de Mensajes')
ax.set_xlabel('Número de mensajes por segundo')
ax.set_ylabel('Latencia (ms)')
ax.grid(True)
ax.legend()
st.pyplot(fig)
st.write(f"La latencia para {numero_mensajes} mensajes por segundo es: {latencia_seleccionada:.2f} ms.")
