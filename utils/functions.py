import math


def get_rows(dataframe):
    """Extrai todas as linhas do DataFrame

    Args:
      dataframe: DataFrame que será utilizado

    Return:
      Matriz com as linhas do DataFrame, lista que contém listas
    """
    matrix = dataframe.values.tolist(
    )                                            # Transforma o DataFrame em uma matriz, ou seja, uma lista de listas
    return matrix


def get_column(dataframe, column_title):
    """Extrai somente uma coluna do DataFrame

    Args:
      dataframe: DataFrame que será retirada a coluna
      column_title: Título da coluna que será retirada

    Return:
      Coluna que foi retirada do DataFrame
    """
    matrix = get_rows(dataframe)
    # Identifica a posição (index) do Título da coluna nas listas
    title_position = list(dataframe).index(column_title)
    column_list = list()
    for values in matrix:
        # Pega o valor da lista na posição da coluna
        value = values[title_position]
        # Adiciona o valor na lista column_list
        column_list.append(value)
    return column_list


def unique_value_list(values):
    """Cria uma lista de valores únicos

    Args:
      values: Lista completa com possíveis valores repetidos

    Return:
      Lista de valores únicos
    """
    unique_list = list()
    for value in values:
        # Verifica se um valor ainda não está na unique_list
        if value not in unique_list:
            # Adicona o valor que ainda não está em unique_list
            unique_list.append(value)
    return unique_list


def isnot_nan(value):
    """Tentar verificar se um valor não é nan

    Args:
        value: Valor a ser verificado: nan -> nan -> None               

    Return:
        Se for possível vericar:
            Valor original, se não for nan
            None, se for nan

        Se não for possível verificar:
            Valor original
    """
    try:
        # Verifica se o valor não é do tipo nan
        if not math.isnan(value):
            return value
    except:                                                                     # Caso o try encontre um erro
        return value


def get_rows_without_nan(dataframe):
    """Deleta os valores nan de todas as linhas do DataFrame

  <<<<<<< HEAD
      Args:
          dataFrame: DataFrame que contém a coluna
          column_title: Título da coluna que será filtrada

      Return:
          Coluna do DataFrame sem os valores nan
      """
    column = get_column(
        dataframe, column_title)                                # Pega a coluna do DataFrame
    # Filtra a coluna
    filtered_column = list(filter(isnot_nan, column))
    return filtered_column


def get_rows_without_nan(dataframe):
    """Deleta os valores nan de todas as linhas do DataFrame

  =======
  >>>>>>> 85501d5f07d34d3c029aae786fc040177379a5f9
    Args:
      dataFrame: DataFrame que será filtrado

    Return:
      Matriz com as linhas do DataFrame sem os valores nan
    """
    dataframe_rows = get_rows(dataframe)
    for row_index, row in enumerate(dataframe_rows):
        filtered_row = list(filter(isnot_nan, row))
        dataframe_rows[row_index] = filtered_row
    return dataframe_rows


def get_rows(dataframe):
    """Extrai todas as linhas do DataFrame

    Args:
      dataframe: DataFrame que será utilizado

    Return:
      Matriz com as linhas do DataFrame, lista que contém listas
    """
    matrix = dataframe.values.tolist(
    )                                            # Transforma o DataFrame em uma matriz, ou seja, uma lista de listas
    return matrix


def get_column_without_nan(dataframe, column_title):
    """Deleta os valores nan da coluna do DataFrame

    Args:
      dataFrame: DataFrame que contém a coluna
      column_title: Título da coluna que será filtrada

    Return:
      Coluna do DataFrame sem os valores nan                                      
    """
    column = get_column(
        dataframe, column_title)                                  # Pega a coluna do DataFrame
    # Filtra a coluna (Retira os valores nan)
    filtered_column = list(filter(isnot_nan, column))
    return filtered_column
