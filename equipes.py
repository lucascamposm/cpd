
import pandas as pd 
#df = pd.read_csv("CSVs/df_final.csv")
def get_clubes(df):
    #==========================================================================
    # Obtendo os valores únicos da coluna 'mandante'
    #==========================================================================
    mandantes_unicos = df['mandante'].unique()

    #==========================================================================
    # Obtendo os valores únicos da coluna 'visitante'
    #==========================================================================
    visitantes_unicos = df['visitante'].unique()

    #==========================================================================
    # Comparando os elementos
    #==========================================================================
    elementos_comuns = set(mandantes_unicos) & set(visitantes_unicos)
    elementos_diferentes = set(mandantes_unicos) ^ set(visitantes_unicos)

    #==========================================================================
    # Exibindo os resultados
    #==========================================================================
    print("Elementos comuns:")
    print(elementos_comuns)
    print("Elementos diferentes:")
    print(elementos_diferentes) # resultado esperado é que seja vazio --> print deve ser: "set()"
    #==========================================================================
    # Lista de Clubes
    #==========================================================================
    clubes = [clube for clube in elementos_comuns]
    print('-----------------------------------------')
    for clube in clubes:
        print(f'-> {clube}')
        print('-----------------------------------------')
    
    #=================
    #   Return 
    #============
    return clubes