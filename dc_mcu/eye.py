from graphic import *

# Contagem das cores dos olhos DC
dc_eye_color_count = dict()
for eye_color in dc_dataframe.EYE:
    if eye_color in dc_eye_color_count.keys():
        dc_eye_color_count[eye_color] += 1
    else:
        dc_eye_color_count[eye_color] = 1
print(dc_eye_color_count)

# Contagem das cores dos olhos Marvel
marvel_eye_color_count = dict()
for eye_color in mcu_dataframe.EYE:
    if eye_color in marvel_eye_color_count.keys():
        marvel_eye_color_count[eye_color] += 1
    else:
        marvel_eye_color_count[eye_color] = 1
print(marvel_eye_color_count)

dc_eye_color_number, marvel_eye_color_number = len(dc_eye_color_count.keys()), len(marvel_eye_color_count.keys())
dc_marvel_eye_colors = list(dc_eye_color_count.keys()) + list(marvel_eye_color_count.keys())
dc_marvel_eye_color_count = list(dc_eye_color_count.values()) + list(marvel_eye_color_count.values())

eyes_color_count = {
    'colors': dc_marvel_eye_colors,
    'count': dc_marvel_eye_color_count,
    'world': ['dc']*dc_eye_color_number + ['marvel']*marvel_eye_color_number
}

fig = px.bar(eyes_color_count, x='world', y='count', color='colors', barmode='group')
fig.show()