def get_column(dataframe, column):
    matrix = dataframe.values.tolist() #Lista de lista, por isso e um matriz
    #funcao do python que transforma o dataframe em lista
    title_position = list(dataframe).index(column)
    column_list = list()
    for values in matrix:
        column_list.append(values[title_position])
    return column_list
