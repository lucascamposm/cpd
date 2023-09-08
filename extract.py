import requests


#======================================================================
# GET DATA 
#====================================================================
def download_file(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Arquivo baixado com sucesso para {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o arquivo: {e}")


#====================================
# Download do csv que será utilizado:
#====================================

url = "https://raw.githubusercontent.com/adaoduque/Brasileirao_Dataset/master/campeonato-brasileiro-full.csv"
save_path = "CSVs/campeonato-brasileiro-full.csv"

download_file(url, save_path)
