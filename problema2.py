import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title('Peticiones procesadas por el sistema')
st.write('')
nodos = st.slider('Número de nodos', 1, 50, 20)  
max_peticiones_sistema = st.slider('Límite máximo de peticiones del sistema', 100, 1000, 400)  

def peticiones_procesadas_por_nodo(x):
    return nodos * x

x_val = np.linspace(1, 20, 100) 
peticiones_totales = peticiones_procesadas_por_nodo(x_val)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_val, peticiones_totales, label='Peticiones procesadas', color='b')
ax.axhline(max_peticiones_sistema, color='r', linestyle='--', label=f'Límite de {max_peticiones_sistema} peticiones')
ax.set_title('Peticiones procesadas por el sistema vs Peticiones por nodo')
ax.set_xlabel('Peticiones por nodo')
ax.set_ylabel('Peticiones totales procesadas')
ax.grid(True)
ax.legend()
st.pyplot(fig)
