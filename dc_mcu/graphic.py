import pandas as pd
import plotly.express as px

# Caminho para os dados
PATH_DC_DATASET = "assets\data\dc-wikia-data.csv"
PATH_MARVEL_DATASET = "assets\data\marvel-wikia-data.csv"

# Leitura dos dados CSV 
dc_dataframe = pd.read_csv(PATH_DC_DATASET)
mcu_dataframe = pd.read_csv(PATH_MARVEL_DATASET)
