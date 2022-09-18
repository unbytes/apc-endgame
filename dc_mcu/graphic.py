import pandas as pd

PATH_DC_WIKIA_DATASET = 'https://raw.githubusercontent.com/MateusVrs/apc-endgame/MateuSunaMarco/01/assets/data/dc-wikia-data.csv'
PATH_MCU_WIKIA_DATASET = 'https://raw.githubusercontent.com/MateusVrs/apc-endgame/MateuSunaMarco/01/assets/data/marvel-wikia-data.csv'

dc_wikia_dataframe = pd.read_csv(PATH_DC_WIKIA_DATASET)
mcu_wikia_dataframe = pd.read_csv(PATH_MCU_WIKIA_DATASET)
