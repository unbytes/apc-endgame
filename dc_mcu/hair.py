from graphic import *

# Contagem das cores dos cabelos (DC)
dc_hair_color_count = dict() # Armazenamento dos dados de cor de cabelo
for hair_color in dc_dataframe.HAIR : # Iterar sobre a coluna hair (cor de cabelo)
    if hair_color in dc_hair_color_count.keys(): # Inicializar chave caso não exista
        dc_hair_color_count[hair_color] += 1 # Soma +1 na cor de cabelo
    else:
        dc_hair_color_count[hair_color] = 1 # Cria chave

# Contagem das cores dos cabelos (Marvel)
mcu_hair_color_count = dict() # Armazenamento dos dados de cor de cabelo
for hair_color in mcu_dataframe.HAIR : # Iterar sobre a coluna hair (cor de cabelo)
    if hair_color in mcu_hair_color_count.keys(): # Inicializar chave caso não exista
        mcu_hair_color_count[hair_color] += 1 # Soma +1 na cor de cabelo
    else:
        mcu_hair_color_count[hair_color] = 1 # Cria chave

# Gerenciamento de dados
dc_hair_color_number, mcu_hair_color_number = len(dc_hair_color_count.keys()), len(mcu_hair_color_count.keys())
dc_mcu_hair_colors = list(dc_hair_color_count.keys()) + list(mcu_hair_color_count.keys())
dc_mcu_hair_color_count = list(dc_hair_color_count.values()) + list(mcu_hair_color_count.values())

# Organização de dados
hair_color_count = {
    'colors': dc_mcu_hair_colors,
    'count': dc_mcu_hair_color_count,
    'world': ['dc']*dc_hair_color_number + ['mcu']*mcu_hair_color_number
}

# Plotagem do gráfico
fig = px.bar(hair_color_count, x='world', y='count', color='colors', barmode='group')
fig.show()