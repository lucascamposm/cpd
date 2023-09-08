#=============================================
# comando para instalar bibliotecas:  
# pip install -r requirements.txt
#
#=============================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as rc
import pickle 
import requests 

#===============================
# Ler CSV
#===============================
df = pd.read_csv("CSVs/campeonato-brasileiro-full.csv")

#==============================================
# Trocar "-" por "Empate" na coluna 'Vencedor'
#==============================================
df = df.replace('-','Empate')

#==============================================
# Removendo as colunas indesejadas
#==============================================
df = df.drop(['formacao_mandante', 'formacao_visitante', 'tecnico_mandante', 'tecnico_visitante'], axis=1)

#================================================================
# Renomeando colunas 'rodata' e 'arena'
#================================================================
df = df.rename(columns={'ID'              : 'id',
                        'rodata'          : 'rodada',
                        'arena'           : 'estadio',
                        'mandante_Placar' : 'mandante_placar',
                        'visitante_Placar':'visitante_placar',
                        'mandante_Estado' : 'mandante_estado',
                        'visitante_Estado': 'visitante_estado'
                        })

#==============================================
# Criar novas colunas 'Data' e  'Ano'
#==============================================
df['data'] = pd.to_datetime(df['data'])
df['ano'] = df['data'].dt.year

#==============================================
# Eliminar as partidas antes de 2003
#==============================================
# Observação: aqui se usa ___".index"___ pois a ideia eh remover os valores especificos
df = df.drop(df[df.ano < 2003].index)

#==============================================================================
# df_mandante recebe df que estava sendo trabalhado até então
#==============================================================================
#df_final = df.drop(df[(df['mandante'] != 'Gremio')].index)]
df_final = df.copy('')

#==================================================================================
# Concatenar as colunas mandante_placar e visitante_placar em apenas uma chamada
# resultado, em que o valor da esquerda corresponde ao mandante_placar
#==================================================================================
df_final['placar'] = df_final['mandante_placar'].astype(str) + 'x' + df_final['visitante_placar'].astype(str)

#==================================================================================
# Remoção colunas de mandante , mandante_placar, visitante_placar, mandante_estado
#==================================================================================
# 
df_final = df_final.drop(['mandante_placar', 'visitante_placar', 'mandante_estado','hora','data'], axis=1)

#==================================================================================
# Reordenação das colunas do df_mandante, apenas para facilidade visual
#==================================================================================
nova_ordem = ['id', 'rodada','mandante', 'visitante', 'placar', 'vencedor', 'estadio', 'visitante_estado', 'ano']
df_final = df_final[nova_ordem]

#===============================================================
# Salvando em CSV df que contém apenas partidas que ocorreram
# na 'Arena do Grêmio' ou no 'Olímpico Monumental'
#===============================================================
df_final.to_csv('CSVs/df_final.csv', index=False)