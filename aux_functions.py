import requests 
import pandas as pd
import os
import platform 

from Partidas import *
from TrieTree import *
#=============================================
# Funcoes Auxiliares
#=============================================
def avanca_tela():
    insira_tecla_continuar()
    limpar_tela()

def insira_tecla_continuar():
    print("\nInsira uma tecla para continuar...",end="")
    
    return enter_input()

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