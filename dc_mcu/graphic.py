import pandas as pd
import plotly.graph_objects as go
from utils.functions import get_column

# Caminho para os dados
PATH_DC_DATASET = "assets/data/dc-wikia-data.csv"
PATH_MARVEL_DATASET = "assets/data/marvel-wikia-data.csv"

# Leitura dos dados CSV
dc_dataframe = pd.read_csv(PATH_DC_DATASET)
mcu_dataframe = pd.read_csv(PATH_MARVEL_DATASET)

# Definição das colunas manipuladas
GRAPHIC_HAIR_COLUMN = 'HAIR'
GRAPHIC_EYE_COLUMN = 'EYE'


def dc_mcu_graphic_column_based(dc_dataframe, mcu_dataframe, column_title, graphic_title):
    """
    Gera um gráfico comparativo entre dois ou mais DataFrames com base em uma coluna
    """
    def extract_colors(dataframe):
        """
        Recebe um DataFrame e extrai as cores da coluna indicada na função pai
        """
        colors = list()  # Lista de cores
        for color in get_column(dataframe, column_title):
            # Verifica se a cor já está na lista e se é válida (str)
            if color not in colors and type(color) == str:
                colors.append(color)  # Adiciona cor
        return colors

    dc_colors = extract_colors(dc_dataframe)
    mcu_colors = extract_colors(mcu_dataframe)

    # Verifica as cores em comum e constroi um conjunto
    colors_in_common = set()
    for color in dc_colors:
        if color in mcu_colors:
            colors_in_common.add(color)
    for color in mcu_colors:
        if color in dc_colors:
            colors_in_common.add(color)
    colors_in_common = list(colors_in_common)

    def count_color_appearance(dataframe, colors):
        """
        Retorna a lista do número de vezes que cada cor aparece na coluna do DataFrame
        """
        count = list()  # Lista de contagem
        for color in colors:
            # Adiciona contagem de uma cor
            count.append(get_column(dataframe, column_title).count(color))
        return count

    dc_count = count_color_appearance(dc_dataframe, colors_in_common)
    mcu_count = count_color_appearance(mcu_dataframe, colors_in_common)

    # Plotagem do gráfico
    graphic_figure = go.Figure([
        go.Bar(name='DC', x=colors_in_common, y=dc_count),
        go.Bar(name='MCU', x=colors_in_common, y=mcu_count)
    ])
    graphic_figure.update_layout(title_text=graphic_title)
    return graphic_figure

hair_graphic = dc_mcu_graphic_column_based(dc_dataframe, mcu_dataframe,
                                             GRAPHIC_HAIR_COLUMN, 'Cor de cabelo: Personagens da Marvel e DC')
eye_graphic = dc_mcu_graphic_column_based(dc_dataframe, mcu_dataframe,
                                            GRAPHIC_EYE_COLUMN, 'Cor dos olhos: Personagens Marvel e DC')
