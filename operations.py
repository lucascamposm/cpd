import pickle
import TrieTree
import Partidas

#=============================================
# Pesquisar Time na árvore: 
#=============================================



#=====================================
# Função auxiliar que retorna indices 
# Em comum entre duas equipes
#====================================
def get_indices_confrontos(equipe_a:str, equipe_b:str, arvore_clubes:TrieTree):
  #======================
  # TIME a
  #======================
  f_pointer_a = arvore_clubes.get_file_pointer(equipe_a)
  f_indice_a = open(f_pointer_a, 'rb')
  indices_a = pickle.load(f_indice_a)
  f_indice_a.close()
  #======================
  # TIME B
  #======================
  f_pointer_b = arvore_clubes.get_file_pointer(equipe_b)
  f_indice_b = open(f_pointer_b, 'rb')
  indices_b = pickle.load(f_indice_b)
  f_indice_b.close()

  #Indices em comum == Indices de confrontos
  indices_em_comum = set(indices_a) & set(indices_b)

  return indices_em_comum
#====================================
# Função que retorna lista De Instâncias
# de Partidas entre dois times
#====================================
def get_confrontos(equipe_a:str, equipe_b:str, arvore_clubes:TrieTree):
  confontros_indices = get_indices_confrontos(equipe_a, equipe_b,arvore_clubes)
  confrontos = []
  with open('./arquivos/partidas.bin', 'rb') as file_partidas:
    for posicao in confontros_indices:
      file_partidas.seek(posicao)
      confronto = pickle.load(file_partidas)
      #confronto.show()
      confrontos.append(confronto)
  file_partidas.close()
  return confrontos


#================================================================
# ESTATISTICAS
#================================================================
def resultados(confrontos):
    confronto = confrontos[0] #acessar primeira partida 
    time_a, time_b = confronto.get_times # para poder usar o metodo get_times
    resultados = {time_a: 0, time_b: 0, 'Empate': 0}

    for confronto in confrontos: 
        vencedor = confronto.vencedor
        resultados[vencedor] = resultados[vencedor] + 1 

    return resultados

  