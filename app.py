import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuração inicial da página
st.set_page_config(page_title="Soma de Riemann", layout="centered")

st.title("Simulador: Soma de Riemann")
st.markdown("Arraste o controle deslizante abaixo para fatiar a área sob a curva $f(x) = \sin(x)$ em mais ou menos retângulos.")

# O controle deslizante (Slider) interativo
n = st.slider("Número de Retângulos (n):", min_value=2, max_value=150, value=4, step=1)

# --- MATEMÁTICA ---
a = 0
b = np.pi
delta_x = (b - a) / n
x_i = np.linspace(a + delta_x, b, n)
alturas = np.sin(x_i)

area_aproximada = np.sum(alturas * delta_x)
area_exata = 2.0
erro_percentual = abs(area_exata - area_aproximada) / area_exata * 100

# --- INTERFACE DE RESULTADOS ---
# Cria duas colunas para exibir os números de forma elegante
col1, col2 = st.columns(2)
col1.metric("Área Aproximada", f"{area_aproximada:.5f}")
col2.metric("Erro Percentual", f"{erro_percentual:.4f} %")

# --- GRÁFICO ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))

x_curva = np.linspace(a, b, 100)
y_curva = np.sin(x_curva)
ax.plot(x_curva, y_curva, color='cyan', linewidth=2, label='f(x) = sin(x)')

pontos_iniciais_barras = x_i - delta_x 
ax.bar(pontos_iniciais_barras, alturas, width=delta_x, align='edge', 
       color='purple', edgecolor='white', alpha=0.7, label='Soma de Riemann')

ax.set_title(f'Soma à Direita (n = {n})', fontsize=14)
ax.set_xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
ax.set_xticklabels(['0', '$\pi/4$', '$\pi/2$', '$3\pi/4$', '$\pi$'])
ax.legend()

# Comando do Streamlit para plotar o gráfico do matplotlib na tela web
st.pyplot(fig)