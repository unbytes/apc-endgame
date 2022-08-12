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

# Faz todas as operações sobre uma respectiva coluna de características para plotar o gráfico
def generate_graphic_column_based(df_column, title):
  # Retorna uma lista de cores de uma coluna
  def extract_colors(dataframe, column):
      colors = list() # Lista de cores
      for color in dataframe[column]:
          if color not in colors and type(color) == str: # Verifica se a cor já está na lista e se é válida (str)
              colors.append(color) # Adiciona cor
      return colors

  dc_colors = extract_colors(dc_dataframe, df_column)
  mcu_colors = extract_colors(mcu_dataframe, df_column)

  # Verifica as cores em comum e constroi uma lista
  colors_in_common = list()
  for color in dc_colors:
      if color in mcu_colors and color not in colors_in_common:
          colors_in_common.append(color)
  for color in mcu_colors:
      if color in dc_colors and color not in colors_in_common:
          colors_in_common.append(color)

  # Retorna a lista de contagem das cores
  def count_color_appearance(dataframe, colors, column):
      count = list() # Lista de contagem
      for color in colors:
          count.append(list(dataframe[column]).count(color)) # Adiciona contagem de uma cor
      return count

  dc_count = count_color_appearance(dc_dataframe, colors_in_common, df_column)
  mcu_count = count_color_appearance(mcu_dataframe, colors_in_common, df_column)
 
  # Plotagem do gráfico
  graphic_figure = go.Figure([
      go.Bar(name='DC', x=colors_in_common, y=dc_count),
      go.Bar(name='MCU', x=colors_in_common, y=mcu_count)
  ])
  graphic_figure.update_layout(title_text=title, yaxis_range=[0, max(max(dc_count), max(mcu_count))])
  graphic_figure.show()

generate_graphic_column_based(GRAPHIC_HAIR_COLUMN, 'Cor de cabelo: Personagens da Marvel e DC')
generate_graphic_column_based(GRAPHIC_EYE_COLUMN, 'Cor dos olhos: Personagens Marvel e DC')