#===============================================================
# Classe que contém a estrutura Partida
#===============================================================
#nova_ordem = ['id', 'rodada','visitante', 'placar', 'vencedor', 'estadio', 'visitante_estado', 'ano']
class Partida:
  def __init__(self, id, rodada , visitante, placar , vencedor , estadio, visitante_estado, ano):
    self.id = id
    self.rodada = rodada
    self.visitante = visitante
    self.placar = placar
    self.vencedor = vencedor
    self.estadio = estadio
    self.visitante_estado = visitante_estado
    self.ano = ano

  #------------------
  # Métodos
  #------------------
  #print completo
  def print_partida(self):
    print(f'Rodada: {self.rodada}, Visitante: {self.visitante}, Placar: {self.placar}, Vencedor: {self.vencedor}, Estadio: {self.estadio},Estado Vistante: {self.visitante_estado}, Ano:{self.ano}' )

  #print resumido
  def show(self):
    print(f'Rodada: {self.rodada}, Visitante: {self.visitante}, Vencedor: {self.vencedor}, Ano:{self.ano}, Estadio: {self.estadio} ' )

#================================================================
# Classe Partidas
#================================================================
class Partidas:
    def __init__(self):
        self.partidas = []
        
    #------------------
    # Métodos
    #------------------        
    def adicionar_partida(self, partida):
        self.partidas.append(partida)

    def filtro_partidas(self, estadio=None, ano=None, adversario=None):
        filtradas = self.partidas

        if estadio is not None:
          filtradas = [partida for partida in filtradas if partida.estadio == estadio]

        if ano is not None:
          filtradas = [partida for partida in filtradas if partida.ano == ano]

        if adversario is not None:
          filtradas = [partida for partida in filtradas if partida.visitante == adversario]

        return filtradas
