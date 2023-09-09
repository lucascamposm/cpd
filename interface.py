import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from Partidas import *
from TrieTree import *  
from binary_functions import *
from operations import * 

from plots import * 

#====================================================================
# HEADER
#====================================================================

st.header('_Bem vindo ao_ is :blue[FutAnalisis] ',divider='rainbow')
st.header('_:blue[Futebol] é Aqui_ :soccer:')
st.write("""
### Classificação e Pesquisa de Dados - UFRGS
  
""")
st.text('  Por Lucas C. Machado & Nicolas Kneip')



#====================================================================
# Carrega Confrontos
#====================================================================

arvore_clubes = carrega_trie()
clubes = []
for clube in arvore_clubes.find_words():
    clubes.append(clube)
clubes.sort()


#====================================================================
# STYLE 
#====================================================================
#================
#Clube A Input 
#================
clube_a = st.selectbox('Escolha o time A', clubes)
button_clube_a = st.button('Selecionar equipe A')
if button_clube_a:
    st.write('You selected:', clube_a)
    #================
    #Clube B Input 
    #================
clube_b = st.selectbox('Escolha o Time B', clubes)
print(type(clube_b))
button_clube_b = button_clube_a = st.button('Selecionar equipe B')
if button_clube_a:
    st.write('Você selecionou:', clube_b)

#==================================================================================
# Load partidas
#==================================================================================

# Exemplo de uso da função
arvore_clubes = carrega_trie()
confrontos = get_confrontos('Gremio', 'Internacional',arvore_clubes)


#==================================================================================
# BOTOES  
#==================================================================================
def click_button():
    st.session_state.clicked = True    

st.button("Buscar Partidas", type="primary", on_click=click_button)

if 'clicked' not in st.session_state:
    st.session_state.clicked = False


if st.session_state.clicked:
    st.write(f'Filtrando Confrontos:{clube_a} vs {clube_b}')
    confrontos = get_confrontos(clube_b, clube_a,arvore_clubes)
    resultados = resultados(confrontos)
    plot_grenal_st(resultados)

#==================================================================================
# GRAFICO GRENAIS 
#==================================================================================


grenais = get_confrontos('Gremio', 'Internacional',arvore_clubes)




