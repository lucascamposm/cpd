#====================================================================
# Gráfico
#====================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as rc

import streamlit as st

def plot_grenal(resultados:dict): 
    vitorias_gremio = resultados['Gremio']
    vitorias_internacional = resultados['Internacional']
    empates = resultados['Empate']
    plt.bar('Vitórias do Grêmio', vitorias_gremio, color='Blue')
    plt.bar('Vitórias do Internacional', vitorias_internacional, color='Red')
    plt.bar('Empates', empates, color='Black')

    # Adicionar rótulos e título
    plt.xlabel('Resultados')
    plt.ylabel('Vitórias')
    plt.title('Grenais disputados no estádio do Grêmio')
    # Mostrar o gráfico
    return plt.show()

def plot_grenal_st(resultados: dict):
    time_a, time_b = [key for key in resultados if key != 'Empate']
    # Criar o gráfico usando o Matplotlib
    fig, ax = plt.subplots()
    colors = ['Blue', 'Red', 'Black'] if time_a != 'Internacional' else ['Red', 'Blue', 'Black']

    ax.bar(f'Vitórias do {time_a}', resultados[time_a], color= colors[0])
    ax.bar(f'Vitórias do {time_b}', resultados[time_b], color=colors[1])
    ax.bar('Empates', resultados['Empate'], color=colors[2])

    # Adicionar rótulos e título
    ax.set_xlabel('Resultados', color="Green")
    ax.set_ylabel('Vitórias', color="Green")
    ax.set_title(f'Confrontos {time_b} vs {time_a}')

    # Exibir o gráfico no Streamlit
    st.pyplot(fig)
