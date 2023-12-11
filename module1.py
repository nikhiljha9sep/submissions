

import pandas as pd

def generate_car_matrix(file_path):
    #
    df = pd.read_csv(file_path)


    car_matrix = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)


    car_matrix.values[[range(len(car_matrix))]*2] = 0

    return car_matrix

file_path = 'dataset-1.csv'
result_matrix = generate_car_matrix(file_path)
print(result_matrix)
