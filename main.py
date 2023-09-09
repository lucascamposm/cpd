import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as rc
import pickle 
import requests 


from Partidas import *
from TrieTree import *

from ETL import * 
from binary_functions import * 
from operations import * 

#=============================================
# comando para instalar bibliotecas:  
# pip install -r requirements.txt
#
#=============================================





#===============================
# Ler CSV
#===============================
try:
    df = pd.read_csv("CSVs/df_final.csv")

except:
    print('ERRO FATAL')
    #=============================================
    # EXTRACT 
    #=============================================
    extract()
    #=============================================
    # TRANSFORM 
    #=============================================
    transform()

def cria_binarios():
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
    # ================================================================
    # Lista de Nomes de todos clubes 
    #=================================================================
    clubes = get_clubes(df)

    # ================================================================
    #Cria um arquivo binario para cada clube 
    # e também uma árvore que aponta para cada
    # um desses arquivos
    #=================================================================
    indices = create_trie(clubes)

    # ================================================================
    #Cria o binário contendo todas partidas e retorna o 
    # dicionário contendo os indices de cada clube 
    #=================================================================
    # Exemplo: 
    # indices['Gremio'] = [192,111,3232,111...]
    indices = cria_bin_partidas(lista_de_partidas, indices)

    # ================================================================
    #Salva os indices de cada clube em seu respectivo arquivo binario 
    #=================================================================
    salvar_indices(indices)

    return print('Arquivos Binários Criados com Sucesso')



#====================================================================
# Carrega Confrontos
#====================================================================
try: 
    arvore_clubes = carrega_trie()
    grenais = get_confrontos('Gremio', 'Internacional',arvore_clubes)

except Exception:
    cria_binarios()
#for grenal in grenais:
  #grenal.show()





#====================================================================
# MENU
#====================================================================
print_msg(f'Resultados Grenais: {resultados(grenais)}')


