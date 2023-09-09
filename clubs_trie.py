from TrieTree import * 
from operations import *




def lista_clubes(arvore_clubes:TrieTree): 
    clubes = []
    for clube in arvore_clubes.find_words():
        clubes.append(clube)
    clubes.sort()
    return clubes