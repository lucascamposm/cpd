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
# Tela-> Escolhe um time
#=============================================

def tela_escolhe_um_time(arvore_clubes, mensagem_print_trie=None):
    clubes = arvore_clubes.lista_clubes()

    bool_avanca_tela = False
    while(bool_avanca_tela == False):
        limpar_tela()
        arvore_clubes.print_clubes(mensagem_print_trie)
        
        print_msg("Selecione uma opção:")
        clube_index = insira_tecla_continuar()
        
        try: 
            type(clube_index) # tenta parsear para int, se falhar vai cair na exceção
            clube = clubes[int(clube_index)]

            if arvore_clubes.search(clube):
                bool_avanca_tela = True
            else:
                limpar_tela()
                print_msg('Opção Invalida')
                print(f'O numero inteiro entre 0 e {len(clubes)-1}')
                insira_tecla_continuar()

        except Exception as e: 
            limpar_tela()
            print_msg('Opção Invalida')
            insira_tecla_continuar()

    return clube


#=============================================
# Imprime todos confrontos entre dois times
#=============================================
def print_confrontos(confrontos: ListaDePartidas):
    counter = 0
    print_msg('Confrontos: ')
    for confronto in confrontos:
        confronto.show()
        counter +=1 
        if counter == 10:
            avanca_tela()
            print_msg('Confrontos:')
            counter = 0

#=============================================
# Tela -> Deseja Continuar Buscando?
#=============================================

def print_deseja_continuar_buscando() -> bool:
    print_msg('Deseja Continuar Buscando?')
    aux_deseja_buscar = input('([S] Sim [N] Não): ')
    if aux_deseja_buscar == 'S' or aux_deseja_buscar == 's':
        print(f'aux_deseja_buscar - {aux_deseja_buscar}')
        continuar_buscando = True
    else: 
        continuar_buscando = False
    return continuar_buscando


#=============================================
# Bubble_sort
#=============================================
def bubble_sort(confrontos:ListaDePartidas, decrescente=None):
    qtd_elementos = len(confrontos)
    for i in range(qtd_elementos - 1):
        for j in range(qtd_elementos - 1 - i):
            if decrescente is not None:
                if confrontos[j].ano > confrontos[j + 1].ano:
                    confrontos[j], confrontos[j + 1] = confrontos[j + 1], confrontos[j]
            else:
                if confrontos[j].ano < confrontos[j + 1].ano:
                    confrontos[j], confrontos[j + 1] = confrontos[j + 1], confrontos[j]
