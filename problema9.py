import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title('Costo de Almacenamiento vs Cantidad de TB')
st.write('')

def costo_almacenamiento(x):
    return 50 + 5 * x

presupuesto = 500
x_val = np.linspace(0, 100, 100)
costos = costo_almacenamiento(x_val)
x_max = (presupuesto - 50) / 5
cantidad_almacenamiento = st.slider(
    'Selecciona la cantidad de almacenamiento (TB)',
    min_value=0,
    max_value=100,
    value=0
)

costo_seleccionado = costo_almacenamiento(cantidad_almacenamiento)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_val, costos, label='Costo de almacenamiento', color='b')
ax.axhline(y=presupuesto, color='r', linestyle='--', label='Presupuesto de 500 dólares')
ax.axvline(x=x_max, color='g', linestyle='--', label=f'Máximo en x={x_max:.2f}')
ax.plot(cantidad_almacenamiento, costo_seleccionado, 'go', label='Seleccionado')
ax.set_title('Costo de Almacenamiento vs Cantidad de TB')
ax.set_xlabel('Cantidad de almacenamiento (TB)')
ax.set_ylabel('Costo de almacenamiento (dólares)')
ax.grid(True)
ax.legend()
st.pyplot(fig)
st.write(f"El costo de almacenamiento para {cantidad_almacenamiento} TB es: {costo_seleccionado:.2f} dólares.")
