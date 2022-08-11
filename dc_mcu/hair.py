from graphic import *

MINIMUM_CHARACTERS = 50

# Contagem das cores dos cabelos (DC)
dc_hair_colors = set(dc_dataframe.HAIR)
dc_hair_color_count = dict()  # Armazenamento da contagem

for hair_color in dc_hair_colors:  # Iterar sobre as cores de cabelo e filtrar
    color_count = list(dc_dataframe.HAIR).count(hair_color)
    if color_count >= MINIMUM_CHARACTERS and type(hair_color) == str:
        dc_hair_color_count[hair_color] = color_count

# Marvel
mcu_hair_colors = set(mcu_dataframe.HAIR)
mcu_hair_color_count = dict()

for hair_color in mcu_hair_colors:
    color_count = list(mcu_dataframe.HAIR).count(hair_color)
    if color_count >= MINIMUM_CHARACTERS and type(hair_color) == str:
        mcu_hair_color_count[hair_color] = color_count

# Gerenciamento de dados
dc_hair_color_number = len(dc_hair_color_count.keys())
mcu_hair_color_number = len(mcu_hair_color_count.keys())

dc_mcu_hair_colors = list(dc_hair_color_count.keys()) + list(mcu_hair_color_count.keys())
dc_mcu_hair_color_count = list(dc_hair_color_count.values()) + list(mcu_hair_color_count.values())

# Organização de dados
hair_color_count = {
    'colors': dc_mcu_hair_colors,
    'count': dc_mcu_hair_color_count,
    'world': ['DC']*dc_hair_color_number + ['MCU']*mcu_hair_color_number
}

# Plotagem do gráfico
fig = px.bar(hair_color_count, x='world', y='count', color='colors', color_discrete_map='identity', barmode='group')
fig.show()
