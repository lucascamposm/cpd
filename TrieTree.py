#===============================
# ARVORES TRIE 
#===============================

#===============================
#Classe Nodo
#===============================
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word =False
        self.file_pointer_name = ''

#===============================
# Classe Principal 
#===============================
class Trie:
    def __init__(self):
        self.root = TrieNode()
    #=============================================
    # - Métodos 
    #=============================================
    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end_of_word = True
        cur.filePointerName = (f"./indices_arquivos/indices_{word}.bin")
        
    #=============================================
    # - Métodos de Busca
    #=============================================
    def search(self, word:str) -> bool:
        #Returns if the word in the trie
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.is_end_of_word

    #=============================================
    # + Método que retorna todos times que começam
    # com certo prefixo
    #=============================================
    def starts_with(self, prefix: str) -> list:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return []
            cur = cur.children[c]
        # Inicializa a lista de palavras com o prefixo
        words = []
        current_word = list(prefix)
        # Chama o método privado _dfs para encontrar palavras
        self._dfs(cur, current_word, words)
        return words

    #=============================================
    # + Método para listar todos os clubes
    #=============================================
    def find_words(self):
        words = []
        current_word = []

        # Chama o método privado _dfs para encontrar palavras
        self._dfs(self.root, current_word, words)
        return words
    def lista_clubes(self):
        clubes = []
        for clube in self.find_words():
            clubes.append(clube)
        
        #Ordenação por Insertion Sort
        for i in range(1, len(clubes)):
            key = clubes[i]
            j = i - 1
            while j >= 0 and key < clubes[j]:
                clubes[j + 1] = clubes[j]
                j -= 1
            clubes[j + 1] = key

        return clubes

    #=============================================
    # - Método privado _dfs para encontrar palavras
    #=============================================
    def _dfs(self, node, current_word, words):
        if node.is_end_of_word:
            words.append(''.join(current_word))
        for char, child_node in node.children.items():
            current_word.append(char)
            self._dfs(child_node, current_word, words)
            current_word.pop()
    #=============================================
    # + Método pra pegar o arquivo bin de índice
    #=============================================
    def get_file_pointer(self, time) -> str:
      node = self.root
      for ch in time:
          if ch not in node.children:
              return False
          node = node.children[ch]
      if (node.is_end_of_word):
          return node.filePointerName
      else:
          return False

    #=============================================
    # + Métodos de Print PRINT 
    #=============================================
    def print_trie(self):
        self._print_trie_recursive(self.root, "")

    def _print_trie_recursive(self, node, indent):
        if node.is_end_of_word:
            print(indent + "*")  # Usando "*" para representar o final da palavra

        for char, child_node in node.children.items():
            print(indent + "└── " + char)
            self._print_trie_recursive(child_node, indent + "    ")
