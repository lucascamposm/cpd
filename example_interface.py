#====================================================================
# MENU
#====================================================================



DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)

#=================================================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from Partidas import *
from TrieTree import *  
from binaries_functions import *
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
button_clube_b = button_clube_a = st.button('Selecionar equipe B')
if button_clube_a:
    st.write('You selected:', clube_b)

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
    plot_grenal_st(resultados(confrontos))

#==================================================================================
# GRAFICO GRENAIS 
#==================================================================================


grenais = get_confrontos('Gremio', 'Internacional',arvore_clubes)




