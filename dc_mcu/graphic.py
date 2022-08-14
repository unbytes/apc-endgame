import pandas as pd
import plotly.graph_objects as go

# Caminho para os dados
PATH_DC_DATASET = "assets\data\dc-wikia-data.csv"
PATH_MARVEL_DATASET = "assets\data\marvel-wikia-data.csv"

# Leitura dos dados CSV 
dc_dataframe = pd.read_csv(PATH_DC_DATASET)
mcu_dataframe = pd.read_csv(PATH_MARVEL_DATASET)

# Definição das colunas manipuladas
GRAPHIC_HAIR_COLUMN = 'HAIR'
GRAPHIC_EYE_COLUMN = 'EYE'

def generate_graphic_column_based(bar_group_order, dataframes, column_title, graphic_title):
    """
    Gera um gráfico comparativo entre dois ou mais DataFrames com base em uma coluna
    """
    def extract_colors(dataframe):
        """
        Recebe um DataFrame e extrai as cores da coluna indicada na função pai
        """
        colors = list() # Lista de cores
        for color in dataframe[column_title]:
            if color not in colors and type(color) == str: # Verifica se a cor já está na lista e se é válida (str)
                colors.append(color) # Adiciona cor
        return colors 

    colors_matrix = list()
    for dataframe in dataframes:
        colors_matrix.append(extract_colors(dataframe))

    # Verifica as cores em comum e constroi um conjunto
    if len(colors_matrix) <= 0:
        return None
    else:
        colors_in_common = set(colors_matrix[0])
        for colors in colors_matrix[1:]:
            colors_in_common = colors_in_common.union(set(colors))
    colors_in_common = list(colors_in_common)

    def count_color_appearance(dataframe, colors):
        """
        Retorna a lista do número de vezes que cada cor aparece na coluna do DataFrame
        """
        count = list() # Lista de contagem
        for color in colors:
            count.append(list(dataframe[column_title]).count(color)) # Adiciona contagem de uma cor
        return count

    count_matrix = list()
    for dataframe in dataframes:
        count_matrix.append(count_color_appearance(dataframe, colors_in_common))
    
    # Plotagem do gráfico
    graphic_bars = list()
    for count, bar_group in zip(count_matrix, bar_group_order):
        graphic_bars.append(go.Bar(name=bar_group, x=colors_in_common, y=count))
        
    graphic_figure = go.Figure(graphic_bars)
    graphic_figure.update_layout(title_text=graphic_title)
    graphic_figure.show()

dataframes = [dc_dataframe, mcu_dataframe]
group_order = ['DC', 'MCU']
generate_graphic_column_based(group_order, dataframes, GRAPHIC_HAIR_COLUMN, 'Cor de cabelo: Personagens da Marvel e DC')
generate_graphic_column_based(group_order, dataframes, GRAPHIC_EYE_COLUMN, 'Cor dos olhos: Personagens Marvel e DC')
