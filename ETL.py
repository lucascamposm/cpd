import requests 
import pandas as pd
import os

from Partidas import *
from TrieTree import *

#======================================================================
#
#   EXTRACT DATA
#
#======================================================================

def download_file(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Arquivo baixado com sucesso para {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o arquivo: {e}")

#====================================
# GET DATA 
#====================================
# Download do csv que será utilizado:
def extract(): 
    url = "https://raw.githubusercontent.com/adaoduque/Brasileirao_Dataset/master/campeonato-brasileiro-full.csv"
    save_path = "CSVs/campeonato-brasileiro-full.csv"

    download_file(url, save_path)


#==========================================================================
#
#   TRANSFORM DATA
#
#==========================================================================

def transform():
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

    #==============================================
    # Vários Estádios estão com '\xa0' no inicio
    #==============================================
    df['estadio'] = df['estadio'].str.replace('\xa0', '')

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

    return print('DF salvo em [CSVs/df_final.csv] ')



#==========================================================================
#   OTHER FUNCTIONS 
#==========================================================================

#df = pd.read_csv("CSVs/df_final.csv")
def get_clubes(df):
    #==========================================================================
    # Obtendo os valores únicos da coluna 'mandante'
    #==========================================================================
    mandantes_unicos = df['mandante'].unique()

    #==========================================================================
    # Obtendo os valores únicos da coluna 'visitante'
    #==========================================================================
    visitantes_unicos = df['visitante'].unique()

    #==========================================================================
    # Comparando os elementos
    #==========================================================================
    elementos_comuns = set(mandantes_unicos) & set(visitantes_unicos)
    elementos_diferentes = set(mandantes_unicos) ^ set(visitantes_unicos)

    #==========================================================================
    # Exibindo os resultados
    #==========================================================================
    print("Elementos comuns:")
    print(elementos_comuns)
    print("Elementos diferentes:")
    print(elementos_diferentes) # resultado esperado é que seja vazio --> print deve ser: "set()"
    #==========================================================================
    # Lista de Clubes
    #==========================================================================
    clubes = [clube for clube in elementos_comuns]
    print('-----------------------------------------')
    for clube in clubes:
        print(f'-> {clube}')
        print('-----------------------------------------')
    
    #=================
    #   Return 
    #=================
    return clubes


#=============================================
# Funcoes Auxiliares
#=============================================

def insira_tecla_continuar():
    print("\nInsira uma tecla para continuar...",end="")
    enter_input()

def limpar_tela():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def enter_input():
    entrada = input('\n[input]: ')
    return entrada
def print_msg(mensagem, insira_tecla_continuar=None):
    frase = (f"|                 {mensagem}                 |")
    aux_print_linha(len(frase))  #linha com "========"
    print(frase) #print da msg 
    aux_print_linha(len(frase))
    if insira_tecla_continuar is not None:
        insira_tecla_continuar()

def aux_print_linha(tamanho_linha):
    for i in range(tamanho_linha): 
        print("=",end="")
    print()

#=============================================
# imprime todos clubes disponiveis na tela
#=============================================
def print_clubes(arvore_clubes):
    arvore_clubes
    clubes = arvore_clubes.lista_clubes()
    print_msg(f'Clubes: ')
    for i in range(0, len(clubes), 5):
        for j in range(5):
            if i + j < len(clubes):
                print(f"[{i + j:02}] - {clubes[i + j]:15}", end="\t")
        print('')  # Pausa a cada grupo de 5 clubes