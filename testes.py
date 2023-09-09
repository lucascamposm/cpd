import unittest

from Partidas import *
from TrieTree import *

from ETL import * 
from binary_functions import * 
from operations import * 
from aux_functions import *


#====================================================================
# Teste da função get_confrotos 
# com Grenais
#====================================================================


#==========================================
# Objetivo: Testar se os dados são consistentes
# e tambem fazer um log das partidas
#==========================================
class TestGrenais(unittest.TestCase):
    def test_grenais(self):
        try:
            arvore_clubes = carrega_trie()
            grenais = get_confrontos('Gremio', 'Internacional', arvore_clubes)
            self.assertIsNotNone(grenais)  # Verifique se grenais não é None

            resultados_grenais = resultados(grenais)
            self.assertIsNotNone(resultados_grenais)  # Verifique se resultados_grenais não é None

            bubble_sort(grenais)
            for grenal in grenais:
                if grenal.ano > 2010:
                    self.assertTrue(grenal.ano > 2010)  # Verifique se o ano do Grenal é maior que 2010
                    grenal.show()

        except Exception as e:
            self.fail(f'Ocorreu um erro: {e}')


#==========================================
# Objetivo: Testar se árvore Trie devolve 
# lista de clubes de maneira ordenada
#==========================================
class TestTrieMethods(unittest.TestCase):

    def test_lista_clubes(self):
        arv = Trie()
        arv.insert('Gremio')
        arv.insert('Fluminense')
        arv.insert('Vasco')
        arv.insert('Flamengo')
        arv.insert('Goias')
        arv.insert('Coritiba')
        arv.insert('Corinthians')
        

        clubes = arv.lista_clubes()
        expected = ['Corinthians', 'Coritiba', 'Flamengo', 'Fluminense', 'Goias', 'Gremio', 'Vasco']
        
        self.assertEqual(clubes, expected)


if __name__ == '__main__':
    unittest.main()
