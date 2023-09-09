import pickle
import TrieTree
import Partidas


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
#==========================================
# Função que retorna lista De Instâncias
# de Partidas entre dois times
#==========================================
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


#==========================================
# Função que retorna lista De Instâncias
# de Partidas entre dois times
#==========================================
def get_todas_partidas(equipe:str):
    file_indice = open(f'./indices_arquivos/indices_{equipe}.bin', 'rb')
    indices_equipe = pickle.load(file_indice)

    confrontos = []
    with open(f'./arquivos/partidas.bin', 'rb') as file_partidas:
        for posicao in indices_equipe:
            file_partidas.seek(posicao)
            confronto = pickle.load(file_partidas)
            #confronto.show()
            confrontos.append(confronto)
    file_partidas.close()
    
    return confrontos

#================================================================
# Lista todos Adversários 
# Por exemplo: Grêmio já enfrentou Flamengo, Bragantino, etc.
# porém hipoteticamente talvez nunca tenha enfrentado o time AAA
# Então, para evitar erros é importante ter esta informação
#================================================================
def lista_adversarios(equipe:str):
    confrontos = get_todas_partidas(equipe)
    adversarios = set()

    for confronto in confrontos: 
        time_a, time_b = confronto.get_times # 
        adversario = time_a if time_a != equipe else time_b
        adversarios.add(adversario)
        
    return adversarios


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

#================================================================
# Dados Arena do Grêmio vs Olímpico Monumental
#================================================================
def get_arena_vs_olimpico(): 
    partidas_gremio = get_todas_partidas('Gremio')
    partidas_arena = {'Vitorias': 0, 'Empates': 0, 'Derrotas': 0}
    partidas_olimpico = {'Vitorias': 0, 'Empates': 0, 'Derrotas': 0}

    for partida in partidas_gremio:
        if partida.mandante == 'Gremio':

            if partida.estadio == 'Arena do Grêmio':
                if partida.vencedor == 'Gremio':
                    partidas_arena['Vitorias'] = partidas_arena['Vitorias'] + 1 
                elif partida.vencedor == 'Empate':
                    partidas_arena['Empates'] = partidas_arena['Vitorias'] + 1 
                else:
                    partidas_arena['Derrotas'] = partidas_arena['Derrotas'] + 1 
                

            if partida.estadio == 'Olímpico':
                if partida.vencedor == 'Gremio':
                    partidas_olimpico['Vitorias'] = partidas_olimpico['Vitorias'] + 1 
                elif partida.vencedor == 'Empate':
                    partidas_olimpico['Empates'] = partidas_olimpico['Vitorias'] + 1 
                else:
                    partidas_olimpico['Derrotas'] = partidas_olimpico['Derrotas'] + 1 

    return partidas_arena, partidas_olimpico