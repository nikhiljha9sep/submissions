import pandas as pd

def get_type_count(file_path):

    df = pd.read_csv(file_path)


    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')],
                            labels=['low', 'medium', 'high'], right=False)


    type_counts = df['car_type'].value_counts().to_dict()


    sorted_type_counts = dict(sorted(type_counts.items()))

    return sorted_type_counts


file_path = 'dataset-1.csv'
result_counts = get_type_count(file_path)
print(result_counts)
