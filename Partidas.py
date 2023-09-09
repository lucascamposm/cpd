from dataclasses import dataclass
from typing import List

#===============================================================
# Classe que contém a estrutura Partida
#===============================================================
#nova_ordem = ['id', 'rodada','mandante, 'visitante', 'placar', 'vencedor', 'estadio', 'visitante_estado', 'ano']
class Partida:
  def __init__(self, id, rodada , mandante, visitante, placar , vencedor , estadio, visitante_estado, ano):
    self.id = id
    self.rodada = rodada
    self.mandante = mandante
    self.visitante = visitante
    self.placar = placar
    self.vencedor = vencedor
    self.estadio = estadio
    self.visitante_estado = visitante_estado
    self.ano = ano

  #------------------
  # Métodos
  #------------------

  # Getters usando o decorador @property
  @property
  def get_times(self):
      return self.mandante, self.visitante

  #print completo
  def print_partida(self):
    print(f'Rodada: {self.rodada}, Mandante: {self.mandante}, Visitante: {self.visitante}, Placar: {self.placar}, Vencedor: {self.vencedor}, Estadio: {self.estadio},Estado Vistante: {self.visitante_estado}, Ano:{self.ano}' )

  #print resumido
  def show(self):
    print(f'[ Ano:{self.ano:04} Rodada: {self.rodada:02}, Mandante: {self.mandante:15},Visitante: {self.visitante:15}, Vencedor: {self.vencedor:15}, Estadio: {self.estadio:37}    ]' )

#================================================================
# Classe Partidas
#================================================================
@dataclass
class ListaDePartidas:
    partidas: List[Partida]


def bubble_sort(confrontos:ListaDePartidas, decrescente=None):
    qtd_elementos = len(confrontos)
    for i in range(qtd_elementos - 1):
        for j in range(qtd_elementos - 1 - i):
            if decrescente is None:
                if confrontos[j].ano > confrontos[j + 1].ano:
                    confrontos[j], confrontos[j + 1] = confrontos[j + 1], confrontos[j]
            else:
                if confrontos[j].ano < confrontos[j + 1].ano:
                    confrontos[j], confrontos[j + 1] = confrontos[j + 1], confrontos[j]
