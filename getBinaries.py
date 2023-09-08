from TrieTree import *
from Partidas import *
import pickle
#================================================================
# Dicionario de Indices - Clubes
#================================================================


#================================================================
# Partidas PICKLE WRITE
#================================================================

def cria_bin_partidas(lista_de_partidas, indices: dict[str, list]) -> dict[str, list]:
    try:
        with open("./arquivos/partidas.bin", "wb") as arquivo_dados:
            for partida in lista_de_partidas:
                # pega o indice e salva no dict de indices
                indice = arquivo_dados.tell() 
                for time in partida.get_times:
                    indices[time].append(indice)
                #escreve no arquivo binario
                pickle.dump(partida ,arquivo_dados) #salva no arquivo binário 
        arquivo_dados.close()
        print('Arquivos Binário Gerado Com sucesso!')
    except Exception as e:
        print(f"Erro ao gerar o arquivo:\n {e}")
    
    return indices



#=============================================
#Insere clubes - Trie 
#=============================================
def create_trie(clubes):
    indices = {}

    arv = Trie()
    for clube in clubes:
        arv.insert(clube)
        indices[clube] = []

    #print(arv.starts_with('F'))  
    with open(f"./indices_arquivos/trie_clubes.bin", "wb") as arquivo:
        pickle.dump(arv,arquivo)
        arquivo.close()

    return indices



#====================================================================
# Salvar Índices 
#====================================================================
def salvar_indices(indices:dict):
    try: 
        for clube in indices: 
            with open(f"./indices_arquivos/indices_{clube}.bin", "wb") as arquivo:
                pickle.dump(indices[clube],arquivo)
            arquivo.close()
        print('indices Criados com sucesso!')
    except Exception as e:
        print(f'Erro ao Salvar indices -> {e}')
    return print('sucesso')


#====================================================================
# CARREGA TRIE 
#===================================================================
#Carrega Árvore Trie de Arquivos
def carrega_trie():
    with open(f"./indices_arquivos/trie_clubes.bin", "rb") as arquivo:
        clubes_trie = pickle.load(arquivo)
        arquivo.close()
    return clubes_trie


