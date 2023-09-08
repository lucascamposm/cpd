import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as rc
import pickle 
import requests 


#===============================
# Ler CSV
#===============================
df = pd.read_csv("CSVs/df_final.csv")


print(df.head())