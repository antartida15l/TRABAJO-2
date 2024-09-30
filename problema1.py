import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

memoria = 1024  
lotes_ma = 8  
eficiencia_re = 0.8  

def datos_procesados(n, x):
    if n <= 5:
        return n * x
    else:
        return 5 * x + (n - 5) * eficiencia_re * x

max_lotes_input = st.slider('Número máximo de lotes', 1, 10, 8)
lotes = np.arange(1, max_lotes_input + 1)
memorias = memoria / lotes  
datos = np.array([datos_procesados(n, memoria / n) for n in lotes])
st.title('Cantidad de datos procesados vs Número de lotes')
st.write('')
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(lotes, datos, marker='o', linestyle='-', color='b', label='Datos procesados')
ax.set_title('Cantidad de datos procesados vs Número de lotes')
ax.set_xlabel('Número de lotes')
ax.set_ylabel('Datos procesados (MB)')
ax.grid(True)
ax.legend()

st.pyplot(fig)
