import unittest
from TrieTree import Trie

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
