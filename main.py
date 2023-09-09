import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as rc
import pickle 
import requests 


from Partidas import *
from equipes import *
from TrieTree import *


from  binaries_functions import * 
from operations import * 

#=============================================
# comando para instalar bibliotecas:  
# pip install -r requirements.txt
#
#=============================================

#+++++++++++++++++++++++++++++++
#   LOAD  DATA
#+++++++++++++++++++++++++++++++
#===============================
# Ler CSV
#===============================
df = pd.read_csv("CSVs/df_final.csv")

# ================================================================
# Cria lista de instâncias (uma para cada linha)
#=================================================================
# lista_de_partidas: Lista de instâncias do objeto Partida
lista_de_partidas = [Partida(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]) for row in zip(
                                                                                           df['id'],
                                                                                           df['rodada'],
                                                                                           df['mandante'],
                                                                                           df['visitante'],
                                                                                           df['placar'],
                                                                                           df['vencedor'],
                                                                                           df['estadio'],
                                                                                           df['visitante_estado'],
                                                                                           df['ano'])]
clubes = get_clubes(df)


#Cria um arquivo binario para cada clube 
# e também uma árvore que aponta para cada
# um desses arquivos
indices = create_trie(clubes)

#Cria o binário contendo todas partidas e retorna o 
# dicionário contendo os indices de cada clube 
# Exemplo: 
# indices['Gremio'] = [192,111,3232,111]
indices = cria_bin_partidas(lista_de_partidas, indices)

#Salva os indices de cada clube em seu respectivo arquivo binario 
salvar_indices(indices)

#Carrega Árvore Trie de Arquivos
with open(f"./indices_arquivos/trie_clubes.bin", "rb") as arquivo:
  clubes_trie = pickle.load(arquivo)
arquivo.close()

#====================================================================
# Carrega Confrontos
#====================================================================
arvore_clubes = carrega_trie()
grenais = get_confrontos('Gremio', 'Internacional',arvore_clubes)

#for grenal in grenais:
  #grenal.show()


#====================================================================
# MENU
#====================================================================

print(resultados(grenais))

