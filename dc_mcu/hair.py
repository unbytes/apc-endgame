from graphic import *

GRAPHIC_COLUMN = 'HAIR'

# Retorna uma lista de cores de uma coluna
def extract_colors(dataframe, column):
    colors = list() # Lista de cores
    for color in dataframe[column]:
        if color not in colors and type(color) == str:
            colors.append(color) # Adiciona cor
    return colors

dc_colors = extract_colors(dc_dataframe, GRAPHIC_COLUMN)
mcu_colors = extract_colors(mcu_dataframe, GRAPHIC_COLUMN)

# Verifica as cores em comum
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

dc_count = count_color_appearance(dc_dataframe, colors_in_common, GRAPHIC_COLUMN)
mcu_count = count_color_appearance(mcu_dataframe, colors_in_common, GRAPHIC_COLUMN)
 
# Plotagem do gráfico
graphic_figure = go.Figure([
    go.Bar(name='DC', x=colors_in_common, y=dc_count),
    go.Bar(name='MCU', x=colors_in_common, y=mcu_count)
])
graphic_figure.update_layout(yaxis_range=[0, max(max(dc_count), max(mcu_count))])
graphic_figure.show()