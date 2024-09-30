import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title('Consumo Total de Energía vs Tamaño de Lote')
st.write('')
tamaño_lote = st.slider('Selecciona el tamaño del lote (x)', min_value=1, max_value=20, value=10)

def energia_consumida(x):
    if x <= 10:
        return x
    else:
        return x * (1 + 0.1 * (x - 10))

def consumo_total(x):
    return x * energia_consumida(x)

x_values = np.linspace(1, 20, 100)
consumo = np.array([consumo_total(x) for x in x_values])
x_max = np.max(x_values[consumo <= 200])

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_values, consumo, label='Consumo total de energía', color='b')
ax.axhline(y=200, color='r', linestyle='--', label='Restricción de 200 unidades de energía')
ax.axvline(x=x_max, color='g', linestyle='--', label=f'Máximo en x={x_max:.2f}')
ax.plot(x_max, consumo_total(x_max), 'go')
ax.axvline(x=tamaño_lote, color='purple', linestyle='--', label=f'Tamaño de lote seleccionado: {tamaño_lote}')
ax.plot(tamaño_lote, consumo_total(tamaño_lote), 'mo') 
ax.set_title('Consumo total de energía vs Tamaño de lote')
ax.set_xlabel('Tamaño de lote (x)')
ax.set_ylabel('Consumo total de energía (unidades)')
ax.grid(True)
ax.legend()
st.pyplot(fig)
st.write(f"El tamaño de lote máximo que satisface la restricción de 200 unidades de energía es aproximadamente: {x_max:.2f}.")
st.write(f"Consumo total de energía para el tamaño de lote seleccionado ({tamaño_lote}): {consumo_total(tamaño_lote):.2f} unidades.")
