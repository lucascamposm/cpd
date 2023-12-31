import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as rc
import pickle 
import requests 
import os

from Partidas import *
from TrieTree import *

from ETL import * 
from binary_functions import * 
from operations import * 
from aux_functions import *

#=============================================
# comando para instalar bibliotecas:  
# pip install -r requirements.txt
#=============================================


def cria_binarios(df):
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
    # ARVORES TRIE 
    # ================================================================
    # ======================================
    # Cria um arquivo binario para cada 
    # clube e também uma árvore que 
    # aponta para  cada  um desses arquivos
    #=======================================
    indices = create_trie(clubes)
        

    # ================================================================
    # Cria o binário contendo todas partidas e retorna o 
    # dicionário contendo os indices de cada clube 
    #=================================================================
    # Exemplo: 
    # indices['Gremio'] = [192,111,3232,111...]
    # indices['Flamengo'] = [192, 233, 1222, 11, ...]
    indices = cria_bin_partidas(lista_de_partidas, indices)

    # ================================================================
    #Salva os indices de cada clube em seu respectivo arquivo binario 
    #=================================================================
    salvar_indices(indices)

    return print('Arquivos Binários Criados com Sucesso')

#=================================================================
# Cria um arquivo binario para cada clube com uma árvore Trie 
# contendo todos adversarios que já enfrentou 
#=================================================================
def create_tries_adversarios(clubes):
    for clube in clubes:
            adversarios = lista_adversarios(clube)
            create_trie_adversarios(adversarios,clube)
    return True

#=================================================================
# TESTES  
#=================================================================
#=================
# DIRETORIOS   
#=================
def teste_diretorios():
    diretorios = ['arquivos', 'adversarios', 'CSVs', 'indices_arquivos']

    print_msg('Iniciando Teste de Diretórios')
    for diretorio in diretorios:
        # Verifica se o diretório existe e cria-o se não existir
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
            print_msg(f' Erro Fatal! Diretorio: {diretorio} não encontrado')
            print(f'Para rodar o programa sera necessario criar uma pasta {diretorio} neste local')
        else:
            print(f'Diretorio {diretorio:18} -> OK')
    return avanca_tela()
#=================
# ARQUIVOS
#=================
#Verifica se arquivo foi criado 
def testa_arquivo(nome_arquivo, diretorio, nao_imprimir=None):
    # Caminho completo para o arquivo
    caminho_completo = os.path.join(diretorio, nome_arquivo)

    # Verifica se o arquivo existe
    if os.path.exists(caminho_completo):
        if nao_imprimir is None: # Não nao_imprimir -> imprimir
            print(f'Arquivo {nome_arquivo:32} -> OK')
        return True 
    else:
        print(f'Arquivo {nome_arquivo:32} -> ERRO')
        return False
    
def testes_arquivos():
    print_msg('Iniciando Teste de Arquivos')

    #===================
    # CSV RAW
    #===================
    csv_raw = "campeonato-brasileiro-full.csv"
    if testa_arquivo(csv_raw,'CSVs') == False:
        extract()
    #===================
    # CSV FINAL
    #===================
    csv_final = "df_final.csv"
    if testa_arquivo(csv_final,'CSVs') == False:
        transform()
        print_msg('Testando novamente:  ')
        testa_arquivo(csv_final,'CSVs')

    #====================================
    # Arquivo Binario contendo as partidas 
    #=====================================
    bin_partidas = 'partidas.bin'
    if testa_arquivo(bin_partidas, 'arquivos') == False:
        df = pd.read_csv("CSVs/df_final.csv")
        cria_binarios(df)
        avanca_tela()
        print_msg('Testando novamente:  ')
        testa_arquivo(bin_partidas, 'arquivos')


    #==============================
    # Teste Trie de Clubes  
    #==============================
    bin_partidas = 'trie_clubes.bin'
    if testa_arquivo(bin_partidas, 'indices_arquivos') == False:
        df = pd.read_csv("CSVs/df_final.csv")
        cria_binarios(df)
        avanca_tela()
        print_msg('Testando novamente:  ')
        testa_arquivo(bin_partidas, 'indices_arquivos')

    #===========================
    # Carregar listar de Clubes 
    # para os seguintes testes 
    #============================
    arvore_clubes = carrega_trie()
    clubes = arvore_clubes.lista_clubes()

    #==============================
    # Teste Arquivos Indices  
    #==============================
    # tenta carregar a arvore de um time
    #se arvore nao existir, chama a função que gera as arvores
    try:
        clubes_missing_indice = []
        for clube in clubes:
            if testa_arquivo(f'{clube}.bin', 'adversarios', True) == False:
                create_tries_adversarios(clubes)
            else:
                clubes_missing_indice.append(clube)
                
        print(f'Arquivos de Indices para cada Clube      -> OK')
    except: 
        #Aí sim chama a função
        print_msg('Erro ao carregar indices para os clubes: ')
        print(clubes_missing_indice)

    #==============================
    # Teste Trie Adversarios 
    #==============================
    # tenta carregar a arvore de um time
    #se arvore nao existir, chama a função que gera as arvores
    try:
        clubes_missing_tries = []
        for clube in clubes:
            if testa_arquivo(f'{clube}.bin', 'adversarios', True) == False:
                create_tries_adversarios(clubes)
            else:
                clubes_missing_tries.append(clube)
        print(f'Arquivos Trie Clube_Adversarios          -> OK')
    except: 
        #Aí sim chama a função
        create_tries_adversarios(clubes)
        print_msg('Erro ao carregar indices para os clubes: ')
        print(clubes_missing_tries)


    return avanca_tela()
#====================================================================
# Carrega Confrontos
#====================================================================

def main():
    limpar_tela()
    #====================================================================
    # Testes Iniciais
    #====================================================================
    # Diretorios 
    dir_teste = teste_diretorios()
    # Arquivos
    testes_arquivos()
    

    #====================================================================
    # Grenais
    #====================================================================
    try: 
        arvore_clubes = carrega_trie()
        grenais = get_confrontos('Gremio', 'Internacional',arvore_clubes)
        print_msg(f'Resultados Grenais: {resultados(grenais)}')
    except Exception:
        df = pd.read_csv("CSVs/df_final.csv")
        cria_binarios(df)
    avanca_tela()

    #===================================================================
    # ARENA VS OLIMPICO
    #==================================================================
    
    #função previamente estruturada para calcular especificamente 
    # o desempenho do Grêmio nestes dois estádios 
    partidas_arena, partidas_olimpico = get_arena_vs_olimpico()

    #prints
    print_msg(f'Aproveitamento Arena do Grêmio vs Olímpico Monumental')
    print(f'Aproveitamento da Arena   : {partidas_arena}')
    print(f'Aproveitamento da Olimpico: {partidas_olimpico}')
    avanca_tela()

    #===================================================================
    # Tela -> Get Confrontos
    #==================================================================
    continuar_buscando = True
    while (continuar_buscando): 


        #==============================
        # Escolhe CLube 
        #==============================
        clube = tela_escolhe_um_time(arvore_clubes)
        limpar_tela()
        print_msg(f'Clube Escolhido -> {clube}')
        
    
        #==============================
        # Escolhe Adversario 
        #==============================
        trie_adversarios_clube = carrega_trie(clube)
        adversario = tela_escolhe_um_time(trie_adversarios_clube, 'Escolha um Adversario')
        try: 
            confrontos = get_confrontos(adversario, clube,arvore_clubes)
            bubble_sort(confrontos) # Ordena confrontos  
            limpar_tela()
            print_msg(f'Resultados do Confronto: {resultados(confrontos)}')
            print_confrontos(confrontos)
        except:
            limpar_tela()
            print_msg('Erro ao buscar as partidas')

        
        avanca_tela()


        continuar_buscando = print_deseja_continuar_buscando()


if __name__ == "__main__":
    main()