import pandas as pd 

# leitura dos dados
mcu_movies_df = pd.read_csv('assets/data/movie_info.csv')

def get_column(dataframe, column):
    matrix = dataframe.values.tolist() #Lista de lista, por isso e um matriz
    #funcao do python que transforma o dataframe em lista
    title_position = list(dataframe).index(column)
    column_list = list()
    for values in matrix:
        column_list.append(values[title_position])
    return column_list

# criação de variaveis para a separação das fases
production_budget = get_column(mcu_movies_df, 'production_budget_in_million_(USD)')
movie_name  = get_column(mcu_movies_df, 'movie_title')
phase_one = production_budget[:6]
phase_two = production_budget[6:12]
phase_three = production_budget[12:23]
phase_four = production_budget[23:]

phase_one_movies = movie_name[:6]
phase_two_movies = movie_name[6:12]
phase_three_movies = movie_name[12:23]
phase_four_movies = movie_name[23:]

# custos dos filmes separados por fases
def list_sum(values):
  summation = 0
  for value in values:
    summation += value
  return summation

TO_BILLION = 1000                                                               
count_phase_one = list_sum(phase_one)/TO_BILLION                                
count_phase_two = list_sum(phase_two)/TO_BILLION
count_phase_three = list_sum(phase_three)/TO_BILLION
count_phase_four = list_sum(phase_four)/TO_BILLION
