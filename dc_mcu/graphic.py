import pandas as pd
import plotly.graph_objects as go
from utils.functions import get_column_without_nan, unique_value_list

PATH_DC_WIKIA_DATASET = 'https://raw.githubusercontent.com/MateusVrs/apc-endgame/MateuSunaMarco/01/assets/data/dc-wikia-data.csv'
PATH_MCU_WIKIA_DATASET = 'https://raw.githubusercontent.com/MateusVrs/apc-endgame/MateuSunaMarco/01/assets/data/marvel-wikia-data.csv'

dc_wikia_dataframe = pd.read_csv(PATH_DC_WIKIA_DATASET)
mcu_wikia_dataframe = pd.read_csv(PATH_MCU_WIKIA_DATASET)


def create_comparative_graphic_column_based(first_df, second_df, first_name, second_name, column_title):
    """Gera um gráfico comparativo entre uma coluna de dois DataFrames

    Args:
      first_df: Primeiro DataFrame a ser utilizado
      second_df: Segundo DataFrame a ser utilizado
      first_name: Nome do primeiro DataFrame
      second_name: Nome do segundo DataFrame
      column_title: Título da coluna em comum entre os DataFrames
      graphic_title: Título do gráfico

    Return:
      Gráfico comparativo entre a coluna dos DataFrames
    """
    first_column = get_column_without_nan(first_df, column_title)
    second_column = get_column_without_nan(second_df, column_title)

    first_values = unique_value_list(first_column)
    second_values = unique_value_list(second_column)

    values_in_common = list()
    # Percorre uma das listas de valores
    for value in first_values:
        # Verifica se um valor está na outra lista e não está na values_in_common
        if value in second_values and value not in values_in_common:
            # Adiciona o valor em comum
            values_in_common.append(value)

    def count_values_appearance(values, column):
        """Conta quantas vezes valores aparecem em uma coluna de DataFrame

        Args:
          values: Lista de valores únicos que vão ser contados
          column: Coluna para contagem dos valores

        Return:
          Lista de contagem dos valores na ordem da original (values)
        """
        count = list()
        for value in values:
            # Conta quantas vezes um valor aparece na coluna
            value_count = column.count(value)
            # Adiciona contagem de um valor
            count.append(value_count)
        # Retorna uma lista com a contagem
        return count

    first_count = count_values_appearance(values_in_common, first_column)
    second_count = count_values_appearance(values_in_common, second_column)

    graphic_figure = go.Figure([
        go.Bar(name=first_name, x=values_in_common,
               y=first_count, marker={'color': '#4C9B82'}),
        go.Bar(name=second_name, x=values_in_common,
               y=second_count, marker={'color': '#0F8BAE'})
    ])
    graphic_figure.update_layout(template='plotly_dark')
    return graphic_figure


HAIR_COLUMN_TITLE = 'HAIR'
EYE_COLUMN_TITLE = 'EYE'

hair_graphic = create_comparative_graphic_column_based(dc_wikia_dataframe, mcu_wikia_dataframe, 'DC', 'MCU', HAIR_COLUMN_TITLE)
eye_graphic = create_comparative_graphic_column_based(dc_wikia_dataframe, mcu_wikia_dataframe, 'DC', 'MCU', EYE_COLUMN_TITLE)
