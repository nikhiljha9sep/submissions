import pandas as pd

def filter_routes(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Group by 'route' and calculate the average of the 'truck' column for each route
    average_truck_by_route = df.groupby('route')['truck'].mean()

    # Filter routes where the average of 'truck' column is greater than 7
    selected_routes = average_truck_by_route[average_truck_by_route > 7].index.tolist()

    # Sort the list of selected routes
    sorted_selected_routes = sorted(selected_routes)

    return sorted_selected_routes

# Example usage:
file_path = 'dataset-1.csv'
result_routes = filter_routes(file_path)
print(result_routes)
